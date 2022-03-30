from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, \
    QLabel, QComboBox, QPushButton, QVBoxLayout, QHBoxLayout, QGroupBox
from PyQt5.QtCore import Qt, QEvent, QSize, QObject, QTimer, \
    QPropertyAnimation, QRect, QEasingCurve
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5 import QtCore, QtGui
import sys

TIME_TO_START_NEXT_BUTTON_ANIMATION_IN_MS = 100
BUTTON_ANIMATION_DURATION_IN_MS = 1200
PUSH_BUTTON_SIZE = QSize(85, 30)

# QEasingCurve.InOutBack
easing_curve_type_dict = {'Linear': QEasingCurve.Linear,                'InQuad': QEasingCurve.InQuad,
                          'OutQuad': QEasingCurve.OutQuad,              'InOutQuad': QEasingCurve.InOutQuad,
                          'OutInQuad': QEasingCurve.OutInQuad,          'InCubic': QEasingCurve.InCubic,
                          'OutCubic': QEasingCurve.OutCubic,            'InOutCubic': QEasingCurve.InOutCubic,
                          'OutInCubic': QEasingCurve.OutInCubic,        'InQuart': QEasingCurve.InQuart,
                          'OutQuart': QEasingCurve.OutQuart,            'InOutQuart': QEasingCurve.InOutQuart,
                          'OutInQuart': QEasingCurve.OutInQuart,        'InQuint': QEasingCurve.InQuint,
                          'OutQuint': QEasingCurve.OutQuint,            'InOutQuint': QEasingCurve.InOutQuint,
                          'OutInQuint': QEasingCurve.OutInQuint,        'InSine': QEasingCurve.InSine,
                          'OutSine': QEasingCurve.OutSine,              'InOutSine': QEasingCurve.InOutSine,
                          'OutInSine': QEasingCurve.OutInSine,          'InExpo': QEasingCurve.InExpo,
                          'OutExpo': QEasingCurve.OutExpo,              'InOutExpo': QEasingCurve.InOutExpo,
                          'OutInExpo': QEasingCurve.OutInExpo,          'InCirc': QEasingCurve.InCirc,
                          'OutCirc': QEasingCurve.OutCirc,              'InOutCirc': QEasingCurve.InOutCirc,
                          'OutInCirc': QEasingCurve.OutInCirc,          'InElastic': QEasingCurve.InElastic,
                          'OutElastic': QEasingCurve.OutElastic,        'InOutElastic': QEasingCurve.InOutElastic,
                          'OutInElastic': QEasingCurve.OutInElastic,    'InBack': QEasingCurve.InBack,
                          'OutBack': QEasingCurve.OutBack,              'InOutBack': QEasingCurve.InOutBack,
                          'OutInBack': QEasingCurve.OutInBack,          'InBounce': QEasingCurve.InBounce,
                          'OutBounce': QEasingCurve.OutBounce,          'InOutBounce': QEasingCurve.InOutBounce,
                          'OutInBounce': QEasingCurve.OutInBounce}


class MainWindow(QMainWindow):
    # Class attributes variables

    def __init__(self) -> None:
        super(MainWindow, self).__init__()

        # Instance variables
        self.timeToStartNextAnimation = 100
        self.animation_time_counter = 0
        self.hideButtons = False
        self.showButtons = False
        self.buttonsAreHidden = False
        self.animation_pointer = 0

        # Create an instance of a QWidget class to
        # be used as central widget.
        self.widget = QWidget(self)
        self.widget.installEventFilter(self)
        self.widget.setMouseTracking(True)
        self.setContentsMargins(10, 10, 0, 0)

        # Create an instance of a QLabel class.
        self.info_label = QLabel("Press the mouse left button to start the animations.\n"
                                 "Change the Animation Settings to get different animations")
        self.info_label.setParent(self.widget)
        self.info_label.setStyleSheet("color: rgb(0, 0, 255); font: 75 10pt FreeSans;")

        # Create an instance of a QLabel class.
        label = QLabel("Hide \nAnimation Type")
        # Create an instance of a QComboBox class.
        self.hideEasingCurveCombo = QComboBox()
        self.hideEasingCurveCombo.addItems([key for key in easing_curve_type_dict])
        self.hideEasingCurveCombo.setCurrentText('InOutBack')
        self.hideEasingCurveCombo.currentTextChanged.connect(lambda text: self.HideComboxCurrentIndexChanged(text))
        # Create an instance of a QVBoxLayout class.
        vertical_layout_1 = QVBoxLayout()
        vertical_layout_1.addWidget(label, alignment=Qt.AlignLeft)
        vertical_layout_1.addWidget(self.hideEasingCurveCombo, alignment=Qt.AlignLeft)
        vertical_layout_1.addStretch(1)

        # Create an instance of a QLabel class.
        label_2 = QLabel("Show \nAnimation Type")
        # Create an instance of a QComboBox class.
        self.showEasingCurveCombo = QComboBox()
        self.showEasingCurveCombo.addItems([key for key in easing_curve_type_dict])
        self.showEasingCurveCombo.setCurrentText('InOutBack')
        self.showEasingCurveCombo.currentTextChanged.connect(lambda text: self.ShowComboxCurrentIndexChanged(text))
        # Create an instance of a QVBoxLayout class.
        vertical_layout_2 = QVBoxLayout()
        vertical_layout_2.addWidget(label_2, alignment=Qt.AlignLeft)
        vertical_layout_2.addWidget(self.showEasingCurveCombo, alignment=Qt.AlignLeft)
        vertical_layout_2.addStretch(1)

        # Create an instance of a QLabel class.
        label_3 = QLabel("Time Between \nAnimations(ms)")
        # Create an instance of a QComboBox class.
        self.startNextAnimCombo = QComboBox()
        self.startNextAnimCombo.addItems(['50', '100', '150', '200', '250', '300', '350', '400', '450', '500'])
        self.startNextAnimCombo.setCurrentText('100')
        self.startNextAnimCombo.setFixedSize(70, 20)
        self.startNextAnimCombo.currentTextChanged.connect(lambda text: self.ChangeTimeToStartNextAnim(text))
        # Create an instance of a QVBoxLayout class.
        vertical_layout_3 = QVBoxLayout()
        vertical_layout_3.addWidget(label_3, alignment=Qt.AlignLeft)
        vertical_layout_3.addWidget(self.startNextAnimCombo, alignment=Qt.AlignLeft)
        vertical_layout_3.addStretch(1)

        # Create an instance of a QLabel class.
        label_4 = QLabel("Animation\nDuration(ms)")
        # Create an instance of a QComboBox class.
        self.animDurationCombo = QComboBox()
        self.animDurationCombo.addItems(['100', '200', '300', '400', '500', '600', '700',
                                         '800', '900', '1000', '1100', '1200', '1300'])
        self.animDurationCombo.setCurrentText('1200')
        self.animDurationCombo.setFixedSize(70, 20)
        self.animDurationCombo.currentTextChanged.connect(lambda text: self.ChangeAnimationDuration(text))
        # Create an instance of a QVBoxLayout class.
        vertical_layout_4 = QVBoxLayout()
        vertical_layout_4.addWidget(label_4, alignment=Qt.AlignLeft)
        vertical_layout_4.addWidget(self.animDurationCombo, alignment=Qt.AlignLeft)
        vertical_layout_4.addStretch(1)

        # Create an instance of a QHBoxLayout class.
        self.horizontal_layout_1 = QHBoxLayout(self.widget)
        self.horizontal_layout_1.addStretch(1)
        self.horizontal_layout_1.addLayout(vertical_layout_1)
        self.horizontal_layout_1.addSpacing(20)
        self.horizontal_layout_1.addLayout(vertical_layout_2)
        self.horizontal_layout_1.addSpacing(20)
        self.horizontal_layout_1.addLayout(vertical_layout_4)
        self.horizontal_layout_1.addSpacing(20)
        self.horizontal_layout_1.addLayout(vertical_layout_3)
        self.horizontal_layout_1.addStretch(1)

        # Create an instance of a QGroupBox class.
        self.GroupBox1 = QGroupBox(self.widget)
        self.GroupBox1.setTitle("Animation Settings")
        self.GroupBox1.setLayout(self.horizontal_layout_1)

        # Create an instance of a QPushButton class.
        self.button_1 = QPushButton("Button 1")
        self.button_1.setFixedSize(PUSH_BUTTON_SIZE)
        self.button_1.setParent(self.widget)

        # Create an instance of a QPushButton class.
        self.button_2 = QPushButton("Button 2")
        self.button_2.setFixedSize(PUSH_BUTTON_SIZE)
        self.button_2.setParent(self.widget)

        # Create an instance of a QPushButton class.
        self.button_3 = QPushButton("Button 3")
        self.button_3.setFixedSize(PUSH_BUTTON_SIZE)
        self.button_3.setParent(self.widget)

        # Create an instance of a QPushButton class.
        self.button_4 = QPushButton("Button 4")
        self.button_4.setFixedSize(PUSH_BUTTON_SIZE)
        self.button_4.setParent(self.widget)

        # Create an instance of a QPushButton class.
        self.button_5 = QPushButton("Button 5")
        self.button_5.setFixedSize(PUSH_BUTTON_SIZE)
        self.button_5.setParent(self.widget)

        # Create a list containing all the buttons
        self.list_of_buttons = [self.button_1, self.button_2, self.button_3, self.button_4, self.button_5]

        # Create an instance of QTimer class to lay out the buttons after
        # a resize event.
        self.resizeTimer = QTimer()
        self.resizeTimer.setSingleShot(True)
        self.resizeTimer.timeout.connect(self.LayoutButtonsHorizontallyManually)

        # Create an instance of QTimer class to start each button animation
        # one after the other with a separation in time (TIME_TO_START_NEXT_BUTTON_ANIMATION_IN_MS).
        self.animationTimer = QTimer()
        self.animationTimer.timeout.connect(self.StartHideOrShowButtonsAnimation)

        # Create a list of animations to show buttons
        self.showButtonAnimationList = list()

        # Create a list of animations to hide buttons
        self.hideButtonAnimationList = list()

        # Window setup.
        self.setFixedSize(550, 250)
        self.setWindowIcon(QIcon(QPixmap("python-logo.png")))
        self.setCentralWidget(self.widget)
        self.setWindowTitle("Animation Example")

    # Override method resizeEvent for class MainWindow.
    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        #
        if self.resizeTimer.isActive():
            self.resizeTimer.stop()
        else:
            self.resizeTimer.start(10)
        #
        QMainWindow.resizeEvent(self, event)

    # Override method eventFilter for class MainWindow.
    def eventFilter(self, source: QObject, event: QEvent) -> bool:
        if event.type() == QtCore.QEvent.MouseButtonPress:
            if isinstance(source, QWidget):
                if event.button() == QtCore.Qt.LeftButton:
                    if self.buttonsAreHidden:
                        self.ShowButtons()
                    else:
                        self.HideButtons()
        else:
            return super(MainWindow, self).eventFilter(source, event)
        return True

    def HideComboxCurrentIndexChanged(self, text) -> None:
        for animation in self.hideButtonAnimationList:
            animation.setEasingCurve(easing_curve_type_dict[text])

    def ShowComboxCurrentIndexChanged(self, text) -> None:
        for animation in self.showButtonAnimationList:
            animation.setEasingCurve(easing_curve_type_dict[text])

    def ChangeTimeToStartNextAnim(self, text) -> None:
        self.timeToStartNextAnimation = int(text)

    def ChangeAnimationDuration(self, text) -> None:
        # Set duration for each button hide animation.
        for animation in self.hideButtonAnimationList:
            animation.setDuration(int(text))
        # Set duration for each button show animation.
        for animation in self.showButtonAnimationList:
            animation.setDuration(int(text))

    @QtCore.pyqtSlot()
    def LayoutButtonsHorizontallyManually(self) -> None:
        #
        button_separation = 20
        #
        total_button_width = (len(self.list_of_buttons) * PUSH_BUTTON_SIZE.width()) + \
                             ((len(self.list_of_buttons) - 1) * button_separation)
        #
        x_position = int((self.geometry().width() - total_button_width) / 2)
        x_position = 0
        #
        y_position = self.geometry().height() - PUSH_BUTTON_SIZE.height() - 50
        #
        button_pointer = 0
        #
        for button in self.list_of_buttons:
            if button_pointer == 0:
                button.setGeometry(x_position,
                                   y_position,
                                   button.width(),
                                   button.height())
            else:
                button.setGeometry(self.list_of_buttons[button_pointer - 1].x() +
                                   self.list_of_buttons[button_pointer - 1].width() + button_separation,
                                   y_position,
                                   button.width(),
                                   button.height())
            button_pointer = button_pointer + 1
        #
        self.info_label.setGeometry(0, 100, self.info_label.width(), self.info_label.height())
        # Create the animations to hide and show the buttons.
        self.CreateAnimationForButtons(self.list_of_buttons)

    @QtCore.pyqtSlot()
    def CreateAnimationForButtons(self, list_of_buttons: list) -> None:
        # Clear the list of button hide animations.
        self.hideButtonAnimationList.clear()
        # Clear the list of button show animations.
        self.showButtonAnimationList.clear()
        # Create the animation to hide the buttons when they are shown.
        for button in list_of_buttons:
            animation = QPropertyAnimation(button, b"geometry")
            animation.setDuration(BUTTON_ANIMATION_DURATION_IN_MS)
            animation.setStartValue(QRect(button.x(),
                                          button.y(),
                                          button.width(),
                                          button.height()))
            animation.setEndValue(QRect(button.x(),
                                        button.y() + 150,  # 150
                                        button.width(),
                                        button.height()))
            animation.setEasingCurve(QEasingCurve.InOutBack)  # InBack
            # Append animation to the list of button hide animations.
            self.hideButtonAnimationList.append(animation)
        # Create the animation to show the buttons when they are hidden.
        for button in list_of_buttons:
            animation = QPropertyAnimation(button, b"geometry")
            animation.setDuration(BUTTON_ANIMATION_DURATION_IN_MS)
            animation.setStartValue(QRect(button.x(),
                                          button.y() + 150,
                                          button.width(),
                                          button.height()))
            animation.setEndValue(QRect(button.x(),
                                        button.y(),
                                        button.width(),
                                        button.height()))
            animation.setEasingCurve(QEasingCurve.InOutBack)  # OutBack
            # Append animation to the list of button show animations.
            self.showButtonAnimationList.append(animation)

    @QtCore.pyqtSlot()
    def StartHideOrShowButtonsAnimation(self) -> None:
        if self.animation_time_counter == 0:
            if self.hideButtons:
                self.hideButtonAnimationList[self.animation_pointer].start()
            if self.showButtons:
                self.showButtonAnimationList[self.animation_pointer].start()
        elif self.animation_time_counter == 1:  # 1 x 100ms
            if self.hideButtons:
                self.hideButtonAnimationList[self.animation_pointer].start()
            if self.showButtons:
                self.showButtonAnimationList[self.animation_pointer].start()
        elif self.animation_time_counter == 2:  # 2 x 100ms
            if self.hideButtons:
                self.hideButtonAnimationList[self.animation_pointer].start()
            if self.showButtons:
                self.showButtonAnimationList[self.animation_pointer].start()
        elif self.animation_time_counter == 3:  # 3 x 100ms
            if self.hideButtons:
                self.hideButtonAnimationList[self.animation_pointer].start()
            if self.showButtons:
                self.showButtonAnimationList[self.animation_pointer].start()
        elif self.animation_time_counter == 4:  # 4 x 100ms
            if self.hideButtons:
                self.hideButtonAnimationList[self.animation_pointer].start()
                self.buttonsAreHidden = True
            if self.showButtons:
                self.showButtonAnimationList[self.animation_pointer].start()
                self.buttonsAreHidden = False
            # Set these flags to false for next time.
            self.hideButtons = False
            self.showButtons = False
            # Stop the animation timer.
            self.animationTimer.stop()
        else:
            pass
        # Increment the animation time to start the next animation.
        if self.hideButtons or self.showButtons:
            self.animation_time_counter = self.animation_time_counter + 1
        # Increment the animation pointer to start the next animation.
        if self.animation_pointer < len(self.hideButtonAnimationList):
            self.animation_pointer = self.animation_pointer + 1

    @QtCore.pyqtSlot()
    def HideButtons(self) -> None:
        if not self.buttonsAreHidden:
            # Update flag.
            self.hideButtons = True
            # Clear the counter.
            self.animation_time_counter = 0
            # Clear animation pointer.
            self.animation_pointer = 0
            # Start the timer to manage the button animations.
            self.animationTimer.start(self.timeToStartNextAnimation)

    @QtCore.pyqtSlot()
    def ShowButtons(self) -> None:
        if self.buttonsAreHidden:
            # Update flag.
            self.showButtons = True
            # Clear the counter.
            self.animation_time_counter = 0
            # Clear animation pointer.
            self.animation_pointer = 0
            # Start the timer to manage the button animations.
            self.animationTimer.start(self.timeToStartNextAnimation)


def main() -> None:
    # Create a QApplication object.
    app = QApplication(sys.argv)
    # Create an instance of the class MainWindow.
    window = MainWindow()
    # Show the window.
    window.show()
    # Start Qt event loop.
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

# PyQt-Animation-Example
This code is a simple example designed to show how to animate objects (widgets) in Python using the module PyQt.
It uses the Qt Animation Framework easing curves to control the values of animated property. In this
example, the geometry of the objects (QPushButtons) are animated.

# Video demostration of the code
https://user-images.githubusercontent.com/5813359/160730290-1aa12166-1393-4c48-81e4-fc8bd1939ed5.mp4

# The Qt Animation Framework 
The animation framework aims to provide an easy way for creating animated and smooth GUIs. 
By animating Qt properties, the framework provides great freedom for animating widgets and other QObjects. 

# Animating Qt Properties
The QPropertyAnimation class can interpolate over Qt properties. It is often this class that should be used 
for animation of values.
A major reason we chose to animate Qt properties is that it presents us with freedom to animate already 
existing classes in the Qt API. 

# Easing curves
Easing curves describe a function that controls how the speed of the interpolation between 0 and 1 should be. 
Easing curves allow transitions from one value to another to appear more natural than a simple constant speed 
would allow. The QEasingCurve class is usually used in conjunction with the QVariantAnimation and 
QPropertyAnimation classes but can be used on its own. It is usually used to accelerate the interpolation from 
zero velocity (ease in) or decelerate to zero velocity (ease out). Ease in and ease out can also be combined 
in the same easing curve.

When using a QPropertyAnimation, the associated easing curve will be used to control the progress of the 
interpolation between startValue and endValue.

# Code to create the animation to hide the buttons.
![image](https://user-images.githubusercontent.com/5813359/160732708-003bdbd8-a0aa-4dc8-84da-ce05dbc87a4b.png)

# Code to create the animation to show the buttons when they are hidden.
![image](https://user-images.githubusercontent.com/5813359/160732895-630e6604-70b2-4309-8ea7-68738ffd95fa.png)


from gpiozero import Led, Button
from signal import pause

print('the program is starting')

led = LED(17)       # define LED pin according to BCM Numbering
button = Button(18) # define Button pin according to BCM Numbering

def onButtonPressed():
	led.on()
	print("Button is pressed, led turned on >>>")

def onButtonReleased():
	led.off()
	print("Button is released, led turned on <<<")

button.when_pressed = onButtonPressed
button.when_released = onButtonReleased

pause()

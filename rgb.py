from gpiozero import DigitalOutputDevice, RGBLED
from gpiozero.pins.pigpio import PiGPIOFactory
import os

factory = PiGPIOFactory(host=os.environ['REMOTE_IP_ADDRESS'])

led = RGBLED(
    red=9,
    green=10,
    blue=11,
    pin_factory=factory
)

try:
    while True:
        print("\nEnter 'help' to see a list of commands.")
        value = input("Enter a valid command:\n$ ")
        value = value.lower()
        if value == 'help':
            print("Commands are:")
            print("[exit]:    End the program.")
            print("[red]:     Display the color red on the LED.")
            print("[green]:   Display the color green on the LED.")
            print("[blue]:    Display the color blue on the LED.")
            print("[magenta]: Display the color magenta on the LED.")
            print("[yellow]:  Display the color yellow on the LED.")
            print("[cyan]:    Display the color cyan on the LED.")
            print("[white]:   Display the color white on the LED.")
            print("[off]:     Turn the LED off.")
        elif value == 'red':
            led.color = (1, 0, 0)
        elif value == 'green':
            led.color = (0, 1, 0)
        elif value == 'blue':
            led.color = (0, 0, 1)
        elif value == 'magenta':
            led.color = (1, 0, 1)
        elif value == 'yellow':
            led.color = (1, 1, 0)
        elif value == 'cyan':
            led.color = (0, 1, 1)
        elif value == 'white':
            led.color = (1, 1, 1)
        elif value == 'orange':
            led.color = (1, 0.5, 0)
        elif value == 'off':
            led.off()
        elif value == 'exit':
            led.off()
            exit()
        else:
            print("Please enter a valid command.")

except KeyboardInterrupt:
    led.off()
    exit()
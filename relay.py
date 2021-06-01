from gpiozero import DigitalOutputDevice
from gpiozero.pins.pigpio import PiGPIOFactory
import os

factory = PiGPIOFactory(host=os.environ['REMOTE_IP_ADDRESS'])

class Relay(DigitalOutputDevice):
    def __init__(self, *args, **kwargs):
        super(Relay, self).__init__(*args, **kwargs)

relay_1 = Relay(22, pin_factory=factory)

try:
    while True:
        print("\nEnter 'help' to see a list of commands.")
        value = input("Enter a valid command:\n$ ")
        value = value.lower()
        if value == 'help':
            print('Commands are:')
            print("'on':   Switch on main power using battery 1, charge battery 2.")
            print("'off':  Switch off main power, charge battery 2.")
            print("'exit': Switch off main power, charge battery 2, and exit program.")
        elif value == 'on':
            relay_1.on()
            print('Relay switched on.')
        elif value == 'off':
            relay_1.off()
            print('Relay switched off.')
        elif value == 'exit':
            relay_1.off()
            print("Ending program.")
            exit()
        else:
            print("* Please enter a valid command.")

except KeyboardInterrupt:
    relay_1.off()
    print('\nEnding program.')
    exit()

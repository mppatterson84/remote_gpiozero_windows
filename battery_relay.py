from gpiozero import DigitalOutputDevice
from gpiozero.pins.pigpio import PiGPIOFactory
import os

factory = PiGPIOFactory(host=os.environ['REMOTE_IP_ADDRESS'])

class Relay(DigitalOutputDevice):
    def __init__(self, *args, **kwargs):
        super(Relay, self).__init__(*args, **kwargs)

relay_1 = Relay(16, pin_factory=factory)
relay_2 = Relay(20, pin_factory=factory)
relay_3 = Relay(21, pin_factory=factory)

try:
    print('* Battery 2 is charging.')
    while True:
        print("\nEnter 'help' to see a list of commands.")
        value = input("Enter a valid command:\n$ ")
        value = value.lower()
        if value == 'on' or value == 'one':
            relay_1.off()
            relay_2.on()
            relay_3.off()
            print('* Battery 1 in use. Battery 2 is charging.')
        elif value == 'off' or value == 'charge two':
            relay_1.off()
            relay_2.off()
            relay_3.off()
            print('* Main power switched off.')
            print('* Battery 2 is charging.')
        elif value == 'two':
            relay_1.on()
            relay_2.on()
            relay_3.on()
            print('* Battery 2 in use. Battery 1 is charging.')
        elif value == 'charge one':
            relay_1.on()
            relay_2.off()
            relay_3.on()
            print('* Main power switched off.')
            print('* Battery 1 is charging.')
        elif value == 'help':
            print('Commands are:')
            print("'on':         Switch on main power using battery 1, charge battery 2.")
            print("'off':        Switch off main power, charge battery 2.")
            print("'one':        Switch on main power using battery 1, charge battery 2.")
            print("'two':        Switch on main power using battery 2, charge battery 1.")
            print("'charge one': Switch off main power, charge battery 1.")
            print("'charge two': Switch off main power, charge battery 2.")
            print("'exit':       Switch off main power, charge battery 2, and exit program.")
        elif value == 'exit':
            relay_1.off()
            relay_2.off()
            relay_3.off()
            print("Ending program.")
            exit()
        else:
            print("* Please enter a valid command.")

except KeyboardInterrupt:
    relay_1.off()
    relay_2.off()
    relay_3.off()
    print('\nEnding program.')
    exit()

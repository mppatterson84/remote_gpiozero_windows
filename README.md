# Remote GPIO

A basic example of remote gpio on windows pc to a raspberry pi.

Follow the instructions from the gpiozero documentation.
https://gpiozero.readthedocs.io/en/stable/remote_gpio.html

These are the steps I followed:

## Preparing the Raspberry Pi

1. Install pigpio.

   `$ sudo apt install pigpio`

2. Enable 'Remote GPIO' in the Raspberry Pi configuration.

3. To automate running the daemon at boot time, run:

   `$ sudo systemctl enable pigpiod`

4. Find the Raspberry Pi's ip address.

   `$ hostname -I`

## Preparing the control computer

1. Create a new project folder and navigate there.

   `C:\Users\User\projects>mkdir remote_gpiozero`

   `C:\Users\User\projects>cd remote_gpiozero`

2. Create and start an environment.

   `C:\Users\User\projects\remote_gpiozero>pipenv shell`

3. Install gpiozero and pigpio.

   `(remote_gpiozero-xxxxxxxx) C:\Users\User\projects\remote_gpiozero>pipenv install gpiozero pigpio`

4. Create a file and import PiGPIOFactory.

   `from gpiozero.pins.pigpio import PiGPIOFactory`

Create a variable and set the Raspberry Pi's network address to the PiGPIOFactory.

   `factory = PiGPIOFactory(host='192.168.1.19')`

5. When setting a devices pins, set `pin_factory` to the remote factory as an additional parameter.

   `led = RGBLED(red=9, green=10, blue=11, pin_factory=factory)`

Here's an example:

`base.py`

```python
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import RGBLED
from time import sleep

factory = PiGPIOFactory(host='192.168.1.19')

led = RGBLED(red=9, green=10, blue=11, pin_factory=factory)

led.color = (1, 1, 1)  # white
sleep(1)
led.color = (0, 0, 0)  # off
```

Run the file:
   `(remote_gpiozero-xxxxxxxx) C:\Users\User\projects\remote_gpiozero>python base.py`

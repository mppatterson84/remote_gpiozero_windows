from gpiozero import Motor, PWMLED
import pygame
import subprocess
from time import sleep
import os
from gpiozero.pins.pigpio import PiGPIOFactory
factory = PiGPIOFactory(host=os.environ['REMOTE_IP_ADDRESS'])

# Lights
redpwm = PWMLED(9, pin_factory=factory)
greenpwm = PWMLED(10, pin_factory=factory)
bluepwm = PWMLED(11, pin_factory=factory)
roof_light = PWMLED(22, pin_factory=factory)
#roof_light = Motor(22, 23)

# Motors
steering = Motor(26, 20, pin_factory=factory)
motor_rear = Motor(16, 19, pin_factory=factory)
motor_front = Motor(12, 6, pin_factory=factory)

#initializes pygame
pygame.init()

controller = ''

try:
    while controller == '':
        try:
            #creates a controller object
            controller = pygame.joystick.Joystick(0)
            #initializes the controller
            controller.init()
            print("car started")
            print("press ctrl + c to exit")
            roof_light.toggle()
        except:
            print('Please connect a controller. Restart in 10 seconds.')
            roof_light.pulse()
            sleep(10)
            subprocess.call(["lxterminal", "--command=python3 gamepad_car.py"])
            exit()
except KeyboardInterrupt:
    print("ending program")
    pygame.quit()
    exit()

speed = 1.0

try:
    while True:
        events = pygame.event.get()
        for event in events:
            if controller.get_axis(0) < 0:
                print(controller.get_axis(0))
                steering.forward(-controller.get_axis(0))
            elif controller.get_axis(0) > 0:
                print(controller.get_axis(0))
                steering.backward(controller.get_axis(0))
            elif controller.get_axis(0) == 0:
                steering.stop()
                
            if controller.get_axis(2) != 0.0 and controller.get_axis(2) > -0.50: #L2
                print(controller.get_axis(2))
                print("L2")
                motor_front.backward((controller.get_axis(2)+1)/2)
                motor_rear.backward((controller.get_axis(2)+1)/2)
            elif controller.get_axis(5) != 0.0 and controller.get_axis(5) > -0.50: #R2
                print(controller.get_axis(5))
                print("R2")
                motor_front.forward((controller.get_axis(5)+1)/2)
                motor_rear.forward((controller.get_axis(5)+1)/2)
            else:
                motor_front.stop()
                motor_rear.stop()
                
            if event.type == pygame.JOYBUTTONDOWN:
                if controller.get_button(0):
                    if speed >= 0.70:
                        speed-=0.10
                    print("Cross (X) Pressed")
                    print(speed)
                elif controller.get_button(1):
                    print("Circle Pressed")
                elif controller.get_button(2):
                    print("Triangle Pressed")
                    if controller.get_button(10):
                        print('shutdown')
                        subprocess.call(["lxterminal", "--command=sudo shutdown -h now"])
                elif controller.get_button(3):
                    if speed <= 0.90: 
                        speed+=0.10
                    print("Square Pressed")
                    print(speed)
                elif controller.get_button(4):
                    print("L1 Pressed")
                elif controller.get_button(5):
                    print("R1 Pressed")
                    motor_front.backward()
                elif controller.get_button(6):
                    print("L2 Pressed")
#                     print(controller.get_axis(2))
#                     motor_front.backward(speed)
#                     motor_rear.backward(speed)
                elif controller.get_button(7):
                    print("R2 Pressed")
#                     print(controller.get_axis(5))
#                     motor_front.forward(speed)
#                     motor_rear.forward(speed)
                    if controller.get_button(5):
                        print("R1 Pressed")
                        motor.backward()
                elif controller.get_button(8):
                    print("SHARE Pressed")
                elif controller.get_button(9):
                    print("OPTIONS Pressed")
                elif controller.get_button(10):
                    print("Power (PS) Button Pressed")
                elif controller.get_button(11):
                    print("Left Analog (L3) Pressed")
                elif controller.get_button(12):
                    print("Right Analog (R3) Pressed")
                    roof_light.toggle()
                    
                if speed == 1.0:
                    greenpwm.value = 0.10
                    redpwm.value = 0.0
                elif speed >= 0.9:
                    greenpwm.value = 0.07
                    redpwm.value = 0.03
                elif speed >= 0.8:
                    greenpwm.value = 0.04
                    redpwm.value = 0.06
                elif speed >= 0.7:
                    greenpwm.value = 0.02
                    redpwm.value = 0.08
                elif speed >= 0.6:
                    greenpwm.value = 0.0
                    redpwm.value = 0.10
                
            elif event.type == pygame.JOYBUTTONUP:
                print("Button Released")
                motor_rear.stop()
                motor_front.stop()
                steering.stop()

except KeyboardInterrupt:
    print("ending program")
    greenpwm.value = 0
    redpwm.value = 0
    bluepwm.value = 0
    roof_light.value = 0
    controller.quit()
    pygame.quit()
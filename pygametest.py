#imports pygame module
import pygame
#initialises the pygame module including the joystick
pygame.init()
pygame.joystick.init
from time import sleep
from pygame.constants import JOYBUTTONDOWN

if pygame.joystick.get_init()== True:
    print("The pygame module has been initialised sucsessfully!")
else:
    print("ERR: Something has gone wrong with the initialisation of the pygame module")
#prints amount of joysticks connected
print("There are " + str(pygame.joystick.get_count())+" controllers conected")
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
jstick=pygame.joystick.Joystick
print(joysticks)
print(jstick)
"""
while True:
    if JOYAXISMOTION== True:
        print(JOYAXISMOTION)
    elif JOYBALLMOTION == True:
        print(JOYBALLMOTION)
    elif JOYBUTTONDOWN == True:
        print(JOYBUTTONDOWN)
    elif JOYBUTTONUP == True:
        print(JOYBUTTONUP)
    elif JOYHATMOTION == True:
        print(JOYHATMOTION)
        """

#the following code i did not make
#all redit to this absolute legend\/ \/ \/ \/
#https://github.com/kevinmcaleer/xbox_controller/blob/main/xbox_controller.py

joysticks = []
for i in range(0, pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
    joysticks[-1].init()

# Print out the name of the controller
print(pygame.joystick.Joystick(0).get_name())

# Xbox Joystick Axis:
# Axis 0 up down, down value is -1, up value is 1
# Axis 1 Left, Right, Left value is: -1, right value is 1
# center is always 0

# Main Loop
while True or KeyboardInterrupt:

    # Check for joystick events
    for event in pygame.event.get():
        if event.type ==JOYBUTTONDOWN:
            if event.button == 0:
                #print("button 0 down")
                print("A")
            if event.button == 1:
                #print("button 1 down")
                print("B")
            if event.button == 2:
                #print("button 2 down")
                print("X")
            if event.button == 3:
                #print("button 4 down")
                print("Y")
            if event.button == 5:
                #print("button 5 down")
                print("RB")
            if event.button == 6:
                print("button 6 down")
            if event.button == 7:
                print("button 7 down")
            if event.button == 8:
                print("button 8 down")
        if event.type == pygame.JOYAXISMOTION:
            if event.axis < 2: # Left stick
                if event.axis == 0: # left/right
                    if event.value < -0.5:
                        print("left			" + str(round(event.value,2)))
                    if event.value > 0.5:
                        print("right			" + str(round(event.value,2)))
                    if event.value > -0.15 and event.value < 0.15:
                        print("horisontal center	" + str(round(event.value,2)))
                if event.axis == 1: # up/down
                    if event.value < -0.5:
                        print("up			" + str(round(event.value,2)))
                    if event.value > 0.5:
                        print("down			" + str(round(event.value,2)))
                    if event.value < -0.25 and event.value > 0.25:
                        print("vertical center	" + str(round(event.value,2)))
  
  
  
  
  

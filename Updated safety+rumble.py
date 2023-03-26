# My code is based off of someone elses code.                   |   |   |   |
# Their code laid a really strong foundation to build from.    \|/ \|/ \|/ \|/  
# All credit to this absolute legend. github link below        
# https://github.com/kevinmcaleer/xbox_controller/blob/main/xbox_controller.py

# *** SAFETY NOTES ***
# *** SAFETY NOTES ***
# *** SAFETY NOTES ***
# SAFETY NOTE, YES SERIOUSLY, A SAFETY NOTE, FROM TED:
# This code was writen at home with an Xbox Series X controler used for testing
# Xbox One controler may have different axis or button presets
# PLEASE CHECK AND TEST BEFORE DRIVING

# FOLLOW UP SAFETY NOTE, YES SERIOUSLY ANOTHER ONE:
# This program only takes the input of the first controller
# Co-pilot capabilities are not as of yet available
# *** SAFETY NOTES ***
# *** SAFETY NOTES ***
# *** SAFETY NOTES ***

# Notes
# Axes: Only tested with an Xbox Series X controller
# Axis: O = Left Stick Horisontal
# Axis: 1 = Left Stick Vertical
# Axis: 2 = Right Stick Vertical
# Axis: 3 = Right Stick Horisontal
# Axis: 4 = Left Trigger
# Axis: 5 = Right Trigger
# All axes go from a scale of 1 to -1

# Buttons
# Button 0  = A
# Button 1  = B
# Button 2  = X 
# Button 3  = Y
# Button 4  = View/Back
# Button 5  = Xbox/Logo
# Button 6  = Menu/Start
# Button 7  = Left Stick
# Button 8  = Right Stick
# Button 9  = Left Bumper
# Button 10 = Right Bumper
# Button 11 = D-Pad North (Up)
# Button 12 = D-Pad South (Down)
# Button 13 = D-Pad West (Left)
# Button 14 = D-Pad East (Right)
# Button 15 = Share/Screenshot

# I refer to the D-Pad buttons as North, South, East, and West
# Think of it the way you look at a map
# North = Up
# South = Down
# West = Left
# East = Right
# I did this because up and down refer to button positions so i cant have buttons of the same name

# It took me a bit to figure this out
# It says 16 buttons and 6 axes and the buttons only go up to 15 and the axes only go up to 5
# I knew it started counting at 0 but I hadn't realised thats what was going on for a while
# We aren't missing a 16th button or 6th axis, I just forgot how to count for a sec
# Thanks 3AM me
# Anytime

# Usefull bits of pygame code that I havent used yet
"""
get_button()
get_init()
quit()
init()
"""
# Things to learn:
# The sys import library


# ISSUES:
# Event based axis tracking after using it for a while takes a bit to catch up
#       Fixed: object based does a constant call and displays in real time
#       displays constantly regardless of if there is change
#       also makes all the data available at once
# Button tracking so far only tracks button down and not button up
#       I added button up to the import call but have yet to use it
#       Maybe use the get button boolean built into the pygame library
#       This may be a nonissue because depending on what operation (nextline)
#       the button is used for the data on what the button state is might be irrelivant

# Actual coding stuff

# Imports the pygame library and initialises it
import pygame
import sys
from pygame.constants import JOYBUTTONDOWN, JOYBUTTONUP, JOYDEVICEADDED, JOYDEVICEREMOVED
pygame.init()
pygame.joystick.init
# Initialising the list to call later in the code
joysticks = []
for i in range(0, pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
    joysticks[-1].init()
        
# Placeholder kill command
def kill(Error):
    #if we loose signal turn itself off
    #full brakes turn off throttle put steering to either middle or curve intentionally so it goes in sircles instead of crashi
    #print("PLACEHOLDER KILL COMMAND DOES NOT CURRENTLY HAVE A FUNCTION other than killing the code")
    #print("set throttle to 0 amnd prakes to max")
    # Using sys.exit instead of exit because it doesent ask before killing
    sys.exit("ERROR CODE HERE: " + str(Error))

def Startup_Message():
    # Prints amount of controllers connected
    print("There are " + str(pygame.joystick.get_count())+" controllers conected")
    # For every controler conected prints out the requested and relevant info for it
    for i in range(0, pygame.joystick.get_count()):
        # Prints the controller number
        print("Controler #" + str(i + 1))
        # Prints the power level of the controller
        print("Controler #" + str(i + 1) + "'s current power level is "\
        + str(pygame.joystick.Joystick(0).get_power_level()))
        # Prints what type of controller it is
        print("Controler #" + str(i + 1) + " is a "\
        + str(pygame.joystick.Joystick(0).get_name()))
        # Prints amount of buttons and axes on the controller
        print("Controler #" + str(i + 1) + " has "\
        + str(pygame.joystick.Joystick(0).get_numbuttons()) + " buttons, and "\
        + str(pygame.joystick.Joystick(0).get_numaxes()) + " axes.")
        # Prints other useless information that I havent figured out what to do with yet
        print("Iteration: " + str(i) +\
        ", Instance ID: " + str(pygame.joystick.Joystick(i).get_instance_id())+\
        ", GUID: " + str(pygame.joystick.Joystick(i).get_guid()))



# If controler connects, disconects, isn't initialised, or the amount of controlers is wrong, throw a fit and dont let the code start
def Initial_Safety_Controller_Check():

    if pygame.joystick.get_init()== False:
        kill("Something has gone wrong with the initialisation of the pygame module"\
        + "\nPlease check if you have the Pygame library instelled on this device")
    if pygame.joystick.get_count() == 0:
        kill("A controller is required to use this code")

def Mid_Safety_Controller_Check():
        if event.type == pygame.JOYDEVICEREMOVED:
            kill("WHAT THE FUCK ARE YOU DOING MY GUY! KEEP THE CONTROLLER CONNECTED TO THE GO KART!\n"\
            + "YA KNOW... THE GO KART. THE MODDED TO HELL CAGE WITH WHEELS THAT YALL STRAPPED A COMPUTER TO!?!?\n"\
            + "LISTEN... IF YOU CANT KEEP THE CONTROLER CONECTED I'M JUST GONNA SHUT DOWN THE GO KART\n"\
            + "BECAUSE YOU CLEARLY CAN'T BE TRUSTED WITH IT")

# Simpler faster and More effective method of getting axes data
def Object_Based_Axes():
    # Creates a list for the axes data
    axes_list= [*range(0, pygame.joystick.Joystick(0).get_numaxes(), 1)]
    # Writes every axis to its respective spot on the list 
    for i in range (pygame.joystick.Joystick(0).get_numaxes()):
        axes_list[i]=(round(pygame.joystick.Joystick(0).get_axis(i),2))
    # A slightly slower but more human readable way of printing the controller axis values
    #print('\t'.join(map(str, axes_list)))
    # Faster way of printing values but the numbers move more cause they dont have tabs in between them
    print(axes_list)
    return (axes_list)

# Button Down Detection
def Event_Based_Buttons_Down():
            if event.button == 0:
                print("A  Down")
                pygame.joystick.Joystick(0).rumble(1,1,0)
            if event.button == 1:
                print("B  Down")
            if event.button == 2:
                print("X  Down")
            if event.button == 3:
                print("Y  Down")
            if event.button == 4:
                print("View Button Down")
            if event.button == 5:
                print("Xbox Logo Down")
            if event.button == 6:
                print("Menu Button Down")
            if event.button == 7:
                print("Left Stick Down")
            if event.button == 8:
                print("Right Stick Down")
            if event.button == 9:
                print("Left Bumper Down")
            if event.button == 10:
                print("Right Bumper Down")
            if event.button == 11:
                print("D-Pad North Down")
            if event.button == 12:
                print("D-Pad South Down")
            if event.button == 13:
                print("D-Pad West Down")
            if event.button == 14:
                print("D-Pad East Down")
            if event.button == 15:
                print("Share Button Down")
# Button Up Detection
def Event_Based_Buttons_Up():
            if event.button == 0:
                print("A  Up")
                pygame.joystick.Joystick(0).stop_rumble()
            if event.button == 1:
                print("B  Up")
            if event.button == 2:
                print("X  Up")
            if event.button == 3:
                print("Y  Up")
            if event.button == 4:
                print("View Button Up")
            if event.button == 5:
                print("Xbox Logo Up")
            if event.button == 6:
                print("Menu Button Up")
            if event.button == 7:
                print("Left Stick Up")
            if event.button == 8:
                print("Right Stick Up")
            if event.button == 9:
                print("Left Bumper Up")
            if event.button == 10:
                print("Right Bumper Up")
            if event.button == 11:
                print("D-Pad North Up")
            if event.button == 12:
                print("D-Pad South Up")
            if event.button == 13:
                print("D-Pad West Up")
            if event.button == 14:
                print("D-Pad East Up")
            if event.button == 15:
                print("Share Button Up")

#rumble test works but only works with onw motor at a time and doesent update in real time
#this is due to the event based button tracking only issuing once
#object oriented button tracking will take more resources but may improve this
#this functionality is unnecicary and thus a nonissue
def rumble_test():
    if event.type ==JOYBUTTONDOWN:
        if event.button == 9:
            pygame.joystick.Joystick(0).rumble(abs(Object_Based_Axes()[1]), 0, 0)
    if event.type ==JOYBUTTONUP:
        if event.button == 9:
            pygame.joystick.Joystick(0).stop_rumble()

    if event.type ==JOYBUTTONDOWN:
        if event.button == 10:
            pygame.joystick.Joystick(0).rumble(0, abs(Object_Based_Axes()[2]), 0)
    if event.type ==JOYBUTTONUP:
        if event.button == 10:
            pygame.joystick.Joystick(0).stop_rumble()

        """
            if pygame.joystick.Joystick(0).get_button(9):
                print(pygame.joystick.Joystick(0).get_button(9))
                print (Object_Based_Axes()[1]) 
                pygame.joystick.Joystick(0).rumble(Object_Based_Axes()[1], 0, 10000)

                        #break
        
        while pygame.joystick.Joystick(0).get_button(9):
            print(pygame.joystick.Joystick(0).get_button(9))
            print(Object_Based_Axes()[1])
            pygame.joystick.Joystick(0).rumble(Object_Based_Axes()[1], 0, 10)
        """

def events():
    Mid_Safety_Controller_Check()
    if event.type ==JOYBUTTONDOWN:
        Event_Based_Buttons_Down()
    if event.type ==JOYBUTTONUP:
        Event_Based_Buttons_Up()

# Deleted janky old code because it took up too much space

# Main Start
Startup_Message()
Initial_Safety_Controller_Check()
# Main Loop
while True or KeyboardInterrupt:
    Object_Based_Axes()
    for event in pygame.event.get():
        events()     

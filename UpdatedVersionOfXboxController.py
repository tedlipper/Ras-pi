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
rumble()
stop_rumble()
get_init()
quit()
init()
"""

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
from pygame.constants import JOYBUTTONDOWN, JOYBUTTONUP
pygame.init()
pygame.joystick.init

# Lets the user know if there was an issue with the library
if pygame.joystick.get_init()== True:
    print("The pygame module has been initialised sucsessfully!")
    print("Setup complete!")
else:
    print("ERR: Something has gone wrong with the initialisation of the pygame module")
    print("Please check if you have the Pygame library instelled on this device")

def Startup_Message():
    # Prints amount of controllers connected
    print("There are " + str(pygame.joystick.get_count())+" controllers conected")
    # For every controler conected prints out the requested and relevant info for it
    for i in range(0, pygame.joystick.get_count()):
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

# Simpler faster and More effective method of getting axes data
def Object_Based_Axes():
    # Creates a list for the axes data
    axes_list= [*range(0, pygame.joystick.Joystick(0).get_numaxes(), 1)]
    # Writes every axis to its respective spot on the list 
    for i in range (pygame.joystick.Joystick(0).get_numaxes()):
        axes_list[i]=(round(pygame.joystick.Joystick(0).get_axis(i),2))
    # A slightly slower but more human readable way of printing the controller axis values
    print('\t'.join(map(str, axes_list)))
    # Faster way of printing values but the numbers move more cause they dont have tabs in between them
    #print(axes_list)

# Botton Dettection
def Event_Based_Buttons():
    # Calls every time theres a controler event (something happens on controller)
    for event in pygame.event.get():
        # Only activates if the event is button down
        if event.type ==JOYBUTTONDOWN:
            # Various if statements manualy defining each button output
            if event.button == 0:
                print("A  Down")
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


# Old icky code that I'm only keeping around because I'm convinced something is gonna go wrong with the new code
# And also it's usefull to have around for reference
# Large chunks of it were removed for optimisation before I ended up deciding to scrap it and use a different approach
# The main issue with the event based axix system was that it outputed one at a time and thus was bad at (next line)
# like everything the axis controlls need to be good at
# Also the center event took up a bunch of updates doing bassically nothing so i paragraph commented them (next line)
# to remove them without deleting them.
# It's been awhile since I used this code so I'm not going to bother commenting line by line
def Event_Based_Axes():
    for event in pygame.event.get():
        if event.type == pygame.JOYAXISMOTION:                
            if event.axis == 0: # left/right
                if event.value < -0.5:
                    print("Left Stick	left			" + str(round(event.value,2)))
                if event.value > 0.5:
                    print("Left Stick	right			 " + str(round(event.value,2)))
                    """
                  if event.value < 0.15 and event.value > -0.15:
                        if event.value < 0:
                            print("Left Stick	horisontal center	" + str(round(event.value,2)))
                        elif event.value < 0:
                            print("Left Stick	horisontal center	 " + str(round(event.value,2)))
                        else:
                            print("Left Stick	horisontal center        " + str(round(event.value,2)))
                    """
            if event.axis == 1: # up/down
                if event.value < -0.5:
                    print("Left Stick	up			" + str(round(event.value,2)))
                if event.value > 0.5:
                    print("Left Stick	down			 " + str(round(event.value,2)))
                    """
                    if event.value < 0.1 and event.value > -0.1:
                        if event.value < 0:
                            print("Left Stick	vertical center		" + str(round(event.value,2)))
                        elif event.value < 0:
                            print("Left Stick	vertical center		 " + str(round(event.value,2)))
                        else:
                            print("Left Stick	vertical center		 " + str(round(event.value,2)))
                    """ 
            if event.axis == 2: # left/right
                if event.value < -0.5:
                    print("Right Stick	left			" + str(round(event.value,2)))
                if event.value > 0.5:
                    print("Right Stick	right			 " + str(round(event.value,2)))
                    """
                    if event.value < 0.1 and event.value > -0.1:
                        if event.value < 0:
                            print("Right Stick	horisontal center	" + str(round(event.value,2)))
                        elif event.value < 0:
                            print("Right Stick	horisontal center	 " + str(round(event.value,2)))
                        else:
                            print("Right Stick	horisontal center	 " + str(round(event.value,2)))
                    """
            if event.axis == 3: # up/down
                if event.value < -0.5:
                    print("Right Stick	up			" + str(round(event.value,2)))
                if event.value > 0.5:
                    print("Right Stick	down			 " + str(round(event.value,2)))
                    """
                    if event.value < 0.15 and event.value > -0.15:
                        if event.value < 0:
                            print("Right Stick	vertical center		" + str(round(event.value,2)))
                        elif event.value < 0:
                            print("Right Stick	vertical center		 " + str(round(event.value,2)))
                        else:
                            print("Right Stick	vertical center		 " + str(round(event.value,2)))
                    """
            if event.axis == 4: #Left Trigger
                if event.value > -1:
                    print("Left	trigger				 " + str(round((round(event.value,2)+1)*50))+"%")
            if event.axis == 5: #Right Trigger
                if event.value > -1:
                    print("Right	trigger	    			 " + str(round((round(event.value,2)+1)*50))+"%")
"""
# This was just prototype code that printed the raw data of the events without giving them a string
# It aws still only able to print one at a time because it was event based
# This is what caused me to switch to object based axis
        if event.type == pygame.JOYAXISMOTION:
            if event.axis == 0: # LS
                print ("0: "+(str(round(event.value,2))))
            if event.axis == 1: # LS
                print ("1: "+(str(round(event.value,2))))
            if event.axis == 2: # RS
                print ("2: "+(str(round(event.value,2))))
            if event.axis == 3: # RS
                print ("3: "+(str(round(event.value,2))))
            if event.axis == 4: # LT
                print ("4: "+(str(round(event.value,2))))
            if event.axis == 5: # RT
                print ("5: "+(str(round(event.value,2))))
            if event.axis == 6: # I have no fucking clue
                print ("HHHHHHHHHUUUUUuuuuhhhhhhh")
                print(str(round(event.value,2)))
"""

# Main Start
Startup_Message()
# Main Loop
while True or KeyboardInterrupt:
    Event_Based_Buttons()
    Object_Based_Axes()

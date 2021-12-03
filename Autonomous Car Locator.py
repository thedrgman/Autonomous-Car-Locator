"""
Autonomous Car Locator

This is a program that helps autonomous cars to find out the location and direction
of other autonomous cars. It is all based on what is provided by the car and from what the car detects.

By David Gameiro

"""

import random


def locator():
    
    """
    self_car = {
            "speed" : 50, #the speed of the current car
            "compass" : "N", #the direction of the current car 
            "gps" : 36.00000, #the current GPS location of the current car
            "id" : 1423456 #the ID number of the car
        },

        car1 = {
            "speed" : 45, #Speed of car1
            "compass" : "N", #Direction of car1
            "gps" : 36.01836, #GPS of car1
            "id" : 1423414 #the ID number of the car
        },

        car2 = {
            "speed" : 45, #Speed of car1
            "compass" : "N", #Direction of car1
            "gps" : 36.01836, #GPS of car1
            "id" : 2463485 #the ID number of the car
        }
    """

    cars = [
        {
            "speed" : 50, #the speed of the current car
            "compass" : "N", #the direction of the current car
            "id" : 1423456, #the ID number of the car
            "gps" : 36.00000 #the current GPS location of the current car
        },
        {
            "speed" : 45, #Speed of car1
            "compass" : "N", #Direction of car1
            "id" : 1423414, #the ID number of the car
            "gps" : 36.01836 #GPS of car1
        },
        {
            "speed" : 45, #Speed of car1
            "compass" : "N", #Direction of car1
            "id" : 2463485, #the ID number of the car
            "gps" : 36.01836 #GPS of car1
        }
    ]

    sensor = ["front", "right", "rear", "left"] #4 available sensors on the car, on all 4 sides
    position = random.choice(sensor) #where is the other car located relative to yours
    

    def info_input(): #this is to gather the speed and compass direction of your car and the other car
        i = 0
        while len(cars) > i:
            if i == 0:
                print("YOUR CAR")
                speed = speed_type()
                cars[0][0] = speed
                print("The current speed of your car is " + str(cars[0][0]) + "mph\n")
                compass = compass_type()
                cars[0][1] = compass
                print("The current direction of your car is " + cars[0][1] + "\n")
            else:
                print("Car " + str(i))
                speed = speed_type()
                cars[i][0] = speed
                print("The current speed of Car " + str(i) + " is " + str(cars[i][0]) + "mph\n")
                print("Both cars can only be traveling the same or opposite directions.")
                print("Please only choose the same direction or the opposite on.")
                compass = compass_type()
                cars[i][1] = compass
                print("The current direction of Car " + str(i) + " is " + cars[i][1] + "\n")
                cars[i][2] = random.randrange(1420,62416,2)
            i += 1
            

    def speed_type(): #if the input for the speed is not a number then it keeps asking for the speed
        val_type = "str"
        while val_type != "int":
            speed = input("What is the speed of the car? ")
            val_type = check_user_input(speed)
        speed = int(speed)
        return speed


    def compass_type(): #if the input for the compass direction is not a number then it keeps asking
        while True: #This loop through until an input is given that is one of the options
            val_type = "int"
            while val_type != "str":
                compass = input("What is the direction that the car is traveling? [N], [S], [E}, [W] ")
                val_type = check_user_input(compass)
            compass = compass.upper()
            if compass == "N" or compass == "S" or compass == "E" or compass == "W":
                break #this verfies that the input is only as specifed, and then ends the loop, if not it continues
            else:
                continue
        return compass

    def check_user_input(input):
            try:
                # Convert it into integer
                val = int(input)
                val_type="int"
            except ValueError:
                try:
                    # Convert it into float
                    val = float(input)
                    val_type = "float"
                except ValueError:
                    val_type = "str"
            return val_type

    
    info_input()
    
    j = 1
    while len(cars) > j:
        print("The ID number of the car is " + str(cars[j][2]))
        
        def speed_compare():
            relative_speed = "faster" #the relative speed your car is going compared to other cars
            if cars[0][0] > cars[j][0]:
                print("Your car is going faster than Car " + str(j))
                relative_speed = "faster"
            elif cars[0][0] < cars[j][0]:
                print("Your car is going slower than Car "  + str(j))
                relative_speed = "slower"
            else:
                print("Your car is going the same speed as Car "  + str(j))
                relative_speed = "same"
            return relative_speed


        def compass(): #used to compare the traveling direction of the two cars
            if cars[0][1] == cars[j][1]:
                print("You and Car " + str(j) + " are both going the same direction")
                direction = "same" 
            elif cars[0][1] == "N" and cars[j][1] == "S":
                print("You and Car " + str(j) + " are both going the opposite direction")
                direction = "opposite"
            elif cars[0][1] == "E" and cars[j][1] == "W":
                print("You and Car " + str(j) + " are both going the opposite direction")
                direction = "opposite"
            elif cars[0][1] == "S" and cars[j][1] == "N":
                print("You and Car " + str(j) + " are both going the opposite direction")
                direction = "opposite"
            elif cars[0][1] == "W" and cars[j][1] == "E":
                print("You and Car " + str(j) + " are both going the opposite direction")
                direction = "opposite"
            return direction
      

        def sensors(): #Which sensors are being triggered on your car, or where is the car is in relation to you
            if position == "front":
                print("The car is in front of your car")
            elif position == "right":
                print("The car is to the right of your car")
            elif position == "left":
                print("The car is to the left of your car")
            else:
                print("The car is behind your car")
            return position

        direction = compass()
        relative_speed = speed_compare()

        def visual_before(): #displays what the current layout of the road is
            print("\nCURRENT ROAD LAYOUT")
            if direction == "same" and position == "front":
                print("|   |   ||   |   |")
                print("|   |   ||   | " + str(j) + " |")
                print("|   |   || Y |   |")
                print("|   |   ||   |   |")
            elif direction == "same" and position == "rear":
                print("|   |   ||   |   |")
                print("|   |   ||   | Y |")
                print("|   |   || " + str(j) + " |   |")
                print("|   |   ||   |   |")
            elif direction == "same" and position == "right":
                print("|   |   ||   |   |")
                print("|   |   ||   |   |")
                print("|   |   || Y | " + str(j) + " |")
                print("|   |   ||   |   |")
            elif direction == "same" and position == "left":
                print("|   |   ||   |   |")
                print("|   |   ||   |   |")
                print("|   |   || " + str(j) + " | Y |")
                print("|   |   ||   |   |")
            elif direction == "opposite":
                print("|   |   ||   |   |")
                print("|   | " + str(j) + " ||   |   |")
                print("|   |   || Y |   |")
                print("|   |   ||   |   |")


        def prediction(): #if the same conditions continue then this will be the predicted road layout
            print("\nPREDICTED FUTURE LAYOUT")
            if direction == "same" and (relative_speed == "same" or relative_speed == "slower") and position == "front":
                print("The other car will remain in front of you.")
                print("|   |   ||   |   |")
                print("|   |   ||   | " + str(j) + " |")
                print("|   |   || Y |   |")
                print("|   |   ||   |   |")
            elif direction == "same" and (relative_speed == "same" or relative_speed == "faster") and position == "rear":
                print("The other car will remain behind you.")
                print("|   |   ||   |   |")
                print("|   |   ||   | Y |")
                print("|   |   || " + str(j) + " |   |")
                print("|   |   ||   |   |")
            elif direction == "same" and relative_speed == "same" and position == "right":
                print("The other car will remain to the right of you.")
                print("|   |   ||   |   |")
                print("|   |   ||   |   |")
                print("|   |   || Y | " + str(j) + " |")
                print("|   |   ||   |   |")
            elif direction == "same" and relative_speed == "same" and position == "left":
                print("The other car will remain to the left of you.")
                print("|   |   ||   |   |")
                print("|   |   ||   |   |")
                print("|   |   || " + str(j) + " | Y |")
                print("|   |   ||   |   |")
            elif direction == "same" and relative_speed == "faster" and position == "front":
                print("You will pass the other car and be in front of them.")
                print("|   |   ||   |   |")
                print("|   |   || Y |   |")
                print("|   |   ||   | " + str(j) + " |")
                print("|   |   ||   |   |")
            elif direction == "same" and relative_speed == "faster" and position == "left":
                print("You will pass the other car and be in front of them.")
                print("|   |   ||   |   |")
                print("|   |   ||   | Y |")
                print("|   |   || " + str(j) + " |   |")
                print("|   |   ||   |   |")
            elif direction == "same" and relative_speed == "faster" and position == "right":
                print("You will pass the other car and be in front of them.")
                print("|   |   ||   |   |")
                print("|   |   || Y |   |")
                print("|   |   ||   | " + str(j) + " |")
                print("|   |   ||   |   |")
            elif direction == "same" and relative_speed == "slower" and position == "right":
                print("The other car will be in front of you.")
                print("|   |   ||   |   |")
                print("|   |   ||   | " + str(j) + " |")
                print("|   |   || Y |   |")
                print("|   |   ||   |   |")
            elif direction == "same" and relative_speed == "slower" and position == "left":
                print("The other car will be in front of you.")
                print("|   |   ||   |   |")
                print("|   |   || " + str(j) + " |   |")
                print("|   |   ||   | Y |")
                print("|   |   ||   |   |")
            elif direction == "same" and relative_speed == "slower" and position == "rear":
                print("The other car will pass you.")
                print("|   |   ||   |   |")
                print("|   |   || " + str(j) + " |   |")
                print("|   |   ||   | Y |")
                print("|   |   ||   |   |")
            elif direction == "opposite":
                print("The other car will be behind you.")
                print("|   |   ||   |   |")
                print("|   |   || Y |   |")
                print("|   | " + str(j) + " ||   |   |")
                print("|   |   ||   |   |")    

        visual_before()
        prediction()
        print("\n\n\n")
        j += 1
         
locator()

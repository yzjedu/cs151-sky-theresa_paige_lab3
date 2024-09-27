# Programmers:Paige and Theresa
# Course:CS*151
# Due Date:10/02/2024
# Lab Assignment:Lab3
# Problem Statement:What type of speed does a ski jumper need to achieve on the ramp to make
# a good distance on their jump?
# Data In: Hill type and jumpers speed
# Data Out: The time in the air, distance traveled, points earned, and a statement on how well they did
# Credits: Class resources

import math

height = 0
points_per_meter = 0
par_distance = 0

hill_type = input("Is the hill type normal or large?")

if hill_type == "normal":
    height = 46
    points_per_meter = 2
    par_distance = 90
elif hill_type == "large":
    height = 70
    points_per_meter = 1.8
    par_distance = 120
else:
    print('Not acceptable.')

print(height, points_per_meter, par_distance)

jumper_speed = int(input('What is the speed of the jumper?'))

time_in_air = math.sqrt((2 * height) / 9.8)
distance = jumper_speed * time_in_air
points = 60 + (distance - par_distance) * points_per_meter

print(time_in_air)

if points >= 61:
    print('Great job for doing better than par!')
elif points < 10:
    print('What happened??')
else:
    print('Sorry you didnt go that far.')

print('Your distance was:', distance, 'and you got', points, 'points.')
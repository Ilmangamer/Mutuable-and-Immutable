


import numpy as np

""""
Can you split a string this string?: World,Earth,America,Canada
Given an article, can you split it based on phrases?¨

"""

# splitting a string

The_String = " World,Earth,America,Canada"

print(The_String.split(","))


"""
Make a program that creates a random number and stores it into x.
Make a program that prints 3 random numbers.
Create a program that generates 100 random numbers and find the frequency of each number.
"""

import random

mylist = [3, 4, 6, 7, 9, 20, 44, 55, 23]

x = random.randrange(0, 100)
print(x)


def randnumbs():
    numb1 = random.randrange(40)
    numb2 = random.randrange(30)
    numb3 = random.randrange(100)
    return numb1, numb2, numb3
    
print(randnumbs())

"""

for i in range(0, 100):
    print(random.randrange(i))

"""
# generate 100 random numbers


from progress.bar import Bar

bar = Bar("Processing", max = 20)

for i in range(20):
    bar.next()
    # Do this

bar.finish()


def func():
    for i in (range(0,10)):
        print(i)
func()

6+1
5+2
4+3
3+4
2+5
1+6
0+7

print(3* 'uni' + 'um')

def func(x):
    return x + 1

f = func
print(f(2) + func(2))

for i in range(3):
    print(i)

import datetime

now = datetime.datetime.now()

print("Today is", now.date())

# Only run this code in the morning
if now.hour < 17:
    if now.month >= 6:
        print("We're in the second half of", now.year, "already!")
    else:
        print("This year isn't even 6 months old.")


# find the sum of the list and determine if it is then the requirement
point_scored = [2, 33, 6, 20, 94, 55]

if len(point_scored) > 3:
    points = 0

    for score in point_scored:
        points += score

    if points > 90:
        print("you have", points, "points")

    else:
        if points < 90:
            print("Not enoough points")

# temperature proram
# Make sure to break program when writing q
# What will happen with when numeric increase / decrease

temperature_prompt = "guess the temperature for the weather today(Press q to exit)"

while True:
    try:
        input_temp_guess = input(temperature_prompt)
    except ValueError as ve:
        print("There is an error, please try again ", str(ve))
    



    if input_temp_guess.lower() == "q":
        break

    if input_temp_guess.isnumeric():
        value = int(input_temp_guess)
        if value < 80:
            double_value = value * 2
            print(double_value)

        elif value >= 80:
            sub_value = value - 70
            print(sub_value)

        
    if input_temp_guess.isalpha():
        if len(input_temp_guess) > 2:
            print("Not texts")
            break


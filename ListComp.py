# List comprehension

shoplist = ['apple', 'shoes', 'myspace', 'leave idoits']

newshoplist = []

for i in shoplist:
    if "s" in i:
        newshoplist.append(i)

print(newshoplist)

# cleaner code

meals = ['Hamburger', 'Pizza', 'Sandwich', 'Burrito']

iteration_OF_meal = [i for i in meals if "a" in i]

print(iteration_OF_meal)





# iterable for the iterable in meals if it deteceted a in the iteration.
fruitss = ['pineapple', 'banana']
apple = [i for i in fruitss if i != "banana"]

print(apple)

basket = ['bread', 'buns', 'apple']
noggin = [i for i in basket if i != 'apple']
print(noggin)


# create 100 random numbers
import random

freq = 0

for i in range(100):
    randnumbs = random.randint(1, 100)
    freq = freq + 1
    print(f"Here is 100 random numbers: {randnumbs}, and here is the frequense of them {freq}")


# asks a phone number

ms_oh = (2,3,56,7,8,3)
ms_who = (3,4,7,2,24,5)

try:
    what_is_your_phon_numb = int(input("What is your phone number?: "))
except ValueError as ve:
    print("Invalid")









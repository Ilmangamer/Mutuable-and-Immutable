
# proglang = (input("What is your preferred programming language?"))

my_prog_lang_list = {'c': 1, 'python': 1, 'c++': 1, 'c#': 1, 'java': 0, 'javascript': 0, 'rust': 0, 'perl': 0, 'sql': 0, 'go': 0, 'golang': 0}
try:
    proglang = input("What is your preferred programming language? ")
except ValueError as ve:
    print("Wrong, please answer the question")


if proglang.lower().strip() in my_prog_lang_list:
    for i in my_prog_lang_list:
        print(i)
    print('you might be on the right track, Here is a list of examples you can choose between.')

elif proglang not in my_prog_lang_list:
    print("Wrong, please answer the question")

try:
    proglang = input("What is your preferred programming language? ").strip().lower()
except ValueError as ve:
    print("Wrong, please answer the question", str.ve())


try:
    if my_prog_lang_list[proglang] == 0:
        print("This programming language is so buttjuice ")
except KeyError as ke:
    print("Wrong, please answer the question")

try:    
    if my_prog_lang_list[proglang] == 1:
        print("This is more of a respectable programming language ")
except KeyError as ve:
    print("Wrong please try again")



# it is not in an if statement
# .values() prints out all the values regardless
# so it won't make sense
# my_prog_lang_list[new_input] -> indicates a key


#Allmonths = January.get(), February.get(), March.get(), April.get(), May.get(), June.get(), July.get(), August.get(), September.get(), October.get(), November.get(), December.get()

##Leastmonth = ""
#Mostmonth = ""
#if Leastmonth.get() < Allmonths.get():
     #print(Leastmonth)
#if Mostmonth.get() > Allmonths.get():
     #print(Mostmonth)
#else:
   # print('Invalid syntax')

def multiply(a, b):
    return a*b

print(multiply(5, 4)) 

# Task: Make a loop which iterates over elements in a lisy

canlist = ["cat", "house", "dogs", "pumpkins"]

for u in canlist(1):
     print(canlist[1])


str1 = "This is a string"
print(str1.replace("is", "hen"))
print(str1.replace("is", "hen", 4))



stringg = "Here is a string eh lol"

y = stringg.find("e", 2, 5)

print(y)

txt = "Hello, welcome to my world."

x = txt.find("e", 5, 10)

print(x)



valid = True
lemon = "What are you looking for? Pig"

while valid:
     what_is_the_word = input("plese guess: ")
     what_is_the_word.isalpha()
     
     if what_is_the_word.isnumeric():
          print("invalid input, try again. ERRor")
          
     if what_is_the_word == "Pig":
          print(lemon.find("Pig"))
          break
          
else:
     print("false, try again")     
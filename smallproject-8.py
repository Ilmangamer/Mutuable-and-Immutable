# profram that shows and solves the summation of 64 +32

def concatenating():
    conca1 = 32
    conca2 = 64
    try:
         N = conca1 + conca2
         print(N)
         return N

    except Exception:
        print('exception')
    
    finally:
        print(f'This goes for function concatenate: {N} ^^')
            
    
concatenating() 



var = 'hello'
print(var)

# In another useful, but wise way
INT = 32
INTT = 64
Sum = INT + INTT
print(Sum)

a = 2.5 - 8
print(abs(a))


def para(x, y):
    return x + y

print(f"here comes para: |")
print(para(32, 64))
print('para above')

# String replace

txt = "Hi, it is me again"



print(txt.replace("Hi, it is me agaain", "No, it is not you"
))


print(txt.replace("No, it is not you", "Let's be certain with immutable and mutable"
))

# Unable to reassign string
# Strings are immutable

#var1 = "Fischer"
#print(type(var1))
#var1[0] = "Panorama"
#print(var1[0]


x = "Pancake"

for i in range(0, 6):
    print (x[i]), print("="), print(id(x[i])
    )

4
def double_sum(x, y):
    return (x + y) * 2
print(double_sum(15, 20))

def even():
    for i in range(10):
        if i % 2 == 0:
            return i
            
even()


# Make a program that will display your favourite actor

def Bae_Ro_Nae():
    I = "I " 
    L = "Love "
    a = "Bae "
    b = "Ro " 
    c = "Nae"
    d = (I + L + a + b + c)
    return d
print(Bae_Ro_Nae())

# a join example

DICT = {"name": "JohnDoe", "country":"Hungary"}
var = " JOIN_EXAMPLE "
i = var.join(DICT)
print(i)



# Try to print the word ‘lucky’ inside s.
x = "lucky"+ "s"  
print(x)

# Try to print the day, month, year in the form “Today is 2/2/2016”
from datetime import date 

a = date(2021, 4, 30).ctime()
print(f"Today's date is: {a}")


#def AmericanDate():
    #l = date.today()
   # l[::-1]
   # return l
#AmericanDate()

def test():
    x = "cool"
    print(x[-1] + x[-2] + x[-4] + x[-3])

print(test())
#print(f"Th date for today is: {0}")
# Next replace a string

# It seems like you need a new string to count the number of times you want the string to display.
def replaceable():
    meine = ["Here is a string ",  "Here is another string "]
    string =  "Here is a string"
    string2 = "Here is another string"
    
    print(string.replace("Here is a string", "Weell replaced"))
    b = print(string.replace("Here is a string", "Weell replaced", 3))
    string4 = "i joined youuuuuuu "
    a = string4.join(meine)
    return a, b

print(replaceable())


"""Try the replace program
Can a string be replaced twice?
Does replace only work with words or also phrases?
String find

Find out if string find is case sensitive
"""
x = 'silent' 
print(x[2] + x[1] + x[0] + x[5] + x[3] + x[4])

def inreverse():
    reverse = "Hello world"
    return reverse[::-1]

print(inreverse())


for i in range(1, 100):
    print(i)




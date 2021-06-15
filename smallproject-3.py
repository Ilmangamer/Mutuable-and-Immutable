#def print_nums(x):
    #for i in range(x):
        #print(i)
#print_nums(10)

n = 0
x = n
res = 0
for i in range(x):
    res += i
print(res)

def func(x):
    res = 0
    for i in range(x):
        res+=i
        print(f"here is the 0 for func(x): {res}")
    return res       
print(func(4))

# res += i, is the same as res = res + i
# This will happen in 4 steps. Since it has been given a parameter of 4. If not this parameter it is invalid code.
# in the first step res = 0 add this with i which starts iterating with 0.
#Second step is res= 0 iterates and concatenates with 1
# res = 1, iterates and concatenates with 2
# res = 3, iterates and concatenates with 3
# The sum is 6
# It stops here due to python counts from 0.  
# The reason why you get None is because in python you have to return something in a function. That is why
#it will implicitly return None.
# To check how the loop works, you can format the value.

    


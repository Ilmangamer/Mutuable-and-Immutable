nums = {"a", "b", "c", "d", "e", "f"}
nums.add("z")
a = (id(nums))
print(f"Here goes for nums 1: {a}")

nums = {"a", "b", "c", "d", "e", "f"}
nums.add("z")
a = id(nums)
print(f"Here goes for nums 2: {a}")


# type(print) is the type of print, which is builtin_function_or_method
# type(print()) calls print and gets the type of the result, 
# which is NoneType because the result is None and the type of None is NoneType


#numslist = [0, 1, 2, 3, 4, 5]
#numslist.append(9)
#print(id(len(numslist)))

print(type(print()))

#set fun
"""
union operator - "|", combines two set to form a new one
containing items in either. When you combine integers it will combine the grreater calues from the 
other set.
"""

"""
The intersection operator & gets items only in both
"""

""" The differnce operator - gets items in the first set 
but not the second
"""

"""
And lastly the symmetric difference operator ^ gets items in either set, but not both.

"""


"""
NOTE this source is a bit uncorrect check another source.
"""
fiverr = {1,2,3,4, 5, 6}
sec = {1,5, 6, 7, 8,25, 45}

newset = {90,40,50,60}
oldset = {100, 200, 300, 400, 500}

print(fiverr | sec)

does_it_comb_greatest = {0, 1, 3, 4}
or_does_it_not = {5,6,7,8}
print(does_it_comb_greatest | or_does_it_not)
print(fiverr & sec)
print(fiverr - sec)
print(newset ^ oldset)



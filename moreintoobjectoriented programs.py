"""1.String Upper Case
Outline:
Write a program to create a class IOString which consists of a constructor that gives a default value to variable str1.
Next up create a method that gets a string as input from the user.
Create another method that will print the string in the upper case.
Next up create an object and call methods to get everything implemented."""

"""class Iostring():
    def __init__(self):
        self.str1=""
    def userinput(self):
        self.str1=input("Enter your name: ")
    def case(self):
        print("Your name is ",self.str1.upper())
#Creating object
new = Iostring()
new.userinput()
new.case()"""

"""2.Employee in and Out
Outline:
Write a program to create a class with the named employee and create a constructor and destructor.
Then, write a function to create an object for that class and delete the object.
Make sure you call the function to get everything implemented!"""

"""class Employee:
    def __init__(self):
        print("Emplyoee created")
    def __del__(self):
        print("Destructor called")
def Create_obj():
    print("Making Object...")
    obj = Employee()
    print("Function end...")
    return obj

print("Calling Create_obj() function...")
obj = Create_obj()
print("Program End...")"""

"""3.Pair of Elements
Outline:
Write a Python program to create a class that will find the numbers in the tuple that add up to a sum and return the position of elements.
 The value of the sum can be taken as input from the user.
   Tuple - (10,20,30,40,50,60,70)"""


class pair_elements:
    def twosum(self,nums,target):
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return(lookup[target - num], i)
            lookup[num] = i

value = int(input("Enter sum for which you want to make this search: "))
print("index1=%d , index2=%d" %
      pair_elements().twosum((10,20,30,40,50,60,70),value))
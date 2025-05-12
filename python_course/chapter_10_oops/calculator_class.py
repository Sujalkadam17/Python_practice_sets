import math 

class calculator:
    def __init__(self):
        #self.num = num 
        pass # pass is used to define an empty class or function
    def square(self,num):
        return num ** 2

    def cube(self,num):
        return num ** 3

    def square_root(self,num):
        return math.sqrt(num)


cal = calculator()
print(f"Square of 4 is {cal.square(4)}")
print(f"cube of 5 is {cal.cube(5)}")
print(f"Square root of 144 is {cal.square_root(144)}")
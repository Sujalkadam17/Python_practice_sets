# := walrus operator used to assign a value to a variable as part of an expression
if( n:= len([1,2,3,4,17])) > 3:
    print(f"List is having : {n} elements")

a = 7 #normal variable
num : int = 10 # definition of variable type
name : str = "Leo"
#defining a function
def add( n1 : int , n : int) -> int:
    return n1 + n

print(add( a, num)) # calling a function

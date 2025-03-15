#add two numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print(f"sum of {a} + {b} is {a+b}")

#remainder
print(f"Remainder of {a} divided by {b} is {a%b}")

#check data type of the variable taken from input method

var = input("Enter a variable: ")
print(type(var))

# comparison

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num1} is smaller than {num2}")
else:
    print(f"{num1} is equal to {num2}")
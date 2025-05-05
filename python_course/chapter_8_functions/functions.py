#functi0n to find the greatest of three numbers
def great_of_three(a,b,c):
    if a >= b and a>=c :
        print(f"{a} is greater than {b} and {c}")
    elif b >= a and b >= c:
        print(f"{b} is greater than {a} and {c}")
    else:
        print(f"{c} is greater than {a} and {b}")

great_of_three(int(input("Enter first number :")),int(input("Enter second number :")),int(input("Enter third number :")))

#function to print multiplication table for given number

def mul_table(n):
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}")
    
mul_table(int(input("Enter a number :")))
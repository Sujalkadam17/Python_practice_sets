#printing right angle star pattern
#first method
n = int(input("Enter the number :"))
for i in range(n):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
# second method 
for i in range(n):
    print(" "*(n-i),end=" ")
    print("*"*(i+1),end=" ")
    print()


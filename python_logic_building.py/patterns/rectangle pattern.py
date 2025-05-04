#rectangle pattern
n = int(input("Enter the number :"))
#first method
for i in range(n):
    if i == 0 or i == n-1:
        print("* "*(n-1),end=" ")
    else:
        print("*",end=" ")
        print(" "*(n-2),end=" ")
        print("*",end=" ")
    print()

#second method
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#third method
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1:
            print("*",end=" ")
        elif j == 0 or j == n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

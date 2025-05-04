n = int(input("Enter the number :"))
#pyramid pattern
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print(" *"*i,end=" ")
    print()
    
# second method for pyramid pattern
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end=" ")
    print()

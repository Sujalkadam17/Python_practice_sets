n = int(input("Enter a number :"))
a = n # stored for another logic
rev = 0 
while n > 0:
    rev = rev * 10 + n % 10 
    n = n // 10
print("Reverse of the number is :", rev)

# another logic for reverse number
print(str(a)[::-1])

    
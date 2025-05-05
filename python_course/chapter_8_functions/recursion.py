#recursive function to find the sum of natural numbers
def sum(n):
    if n == 1:
        return 1
    return n + sum(n-1)

def fact(n):
    if n == 1 or n == 0:
        return 1
    return n * fact(n-1)

n = int(input("Enter the number :"))

print("sum of natural numbers :",sum(n))
print(f"facorial of {n} is",fact(n))
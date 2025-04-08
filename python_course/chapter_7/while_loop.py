#greet all the person names in lsit whose name starts with s
#using while loop

l = ["Sujal","Leo","Rohit","Virat","Shubham","Hardik"]
i = 0
while(i < len(l)):
    if l[i].startswith("S"):
        print("Hey There !",l[i])
    i += 1


#check whether a number is prime or not using while loop

num = int(input("Enter a number :"))
count = 2
while():
    if num % count == 0:
        print(num,"is not a prime number")
        break
    else:
        print(num,"is a prime number")
    count += 1

#sum of first n natural numbers using while loop

n = int(input("Enter a number :"))
sum = 0
count = 1

while(count <= n):
    sum += count
    count += 1
print(f"Sum of first{n}natural numbers is{sum}")

    

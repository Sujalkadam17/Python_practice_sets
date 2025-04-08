#print multiplication table of a given number using for loop
num = int(input("Enter a number: "))

for i in range(11):#or i in range(1,11)
    print(i*num)

#greet all the person names in lsit whose name starts with s'''

l = ["Sujal","Leo","Rohit","Virat","Shubham","Hardik"]

for i in l:
    if i.startswith("S"):
        print("Hey There !",i)


#check whether a number is prime or not using for loop
num = int(input("Enter a number :"))
for i in range(2,num):
    if num % i == 0:
        print(num,"is not a prime number")
        break
else:
    print(num,"is a prime number")


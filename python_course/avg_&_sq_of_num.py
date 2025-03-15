size =int(input("Enter range of numbers "))
val = 0
li =[]
for i in range(1,size+1):
    li.append(int(input(f"Enter {i}st number: ")))

print("Average of your numbers is :",sum(li)/len(li))

#square of a number entered by user

n = int(input("Enter a number to get its square: "))
print(f"Square of {n} is {n**2}")
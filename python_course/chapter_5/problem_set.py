
#to sum of all elements in list
nums = [1,23,1,32,21,23,]
print(sum(nums))

#to count no. of times 0 occured in following tuple
a = (7,0,8,0,0,9)
print(a.count(0))

# to store seven fruits in a list entered by user
fruits = []
for i in range(7):
    fruits.append(input(f"Enter {i+1}st fruit:"))


# taking marks of 6 students and print in sorted manner
marks = []
for i in range(6):
    marks.append(input(f"Enter marks of {i+1} st student : "))

marks.sort()
print(marks)

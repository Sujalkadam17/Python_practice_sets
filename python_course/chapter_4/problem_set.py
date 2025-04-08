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

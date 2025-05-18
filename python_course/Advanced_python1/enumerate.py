#write a program to print 3rd 5th and 7th element of a list using enumerate

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for idx , i in enumerate(lst):
    if idx in [2, 4, 6]:
        print(f"Element at index {idx+1} is {i}")

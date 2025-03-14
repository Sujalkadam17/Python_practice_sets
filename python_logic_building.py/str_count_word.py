str = input("Enter a string :")
print("Total words in the string is :",len(str.split()))

# another logic for counting words in string but not accurate as it counts spaces also
count = 1
for i in str:
    if i == " ":
        count += 1
print("Total words in the string is :",count)

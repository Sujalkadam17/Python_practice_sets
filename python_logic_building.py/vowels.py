str = input("Enter a string :")
vowels ="aeiouAEIOU"
count = 0
vow =""

for i in str:
    if i in vowels:
        count +=1
        vow += i+" "
print(f"Total vowels in the string is : {count} and vowels are : {vow}")

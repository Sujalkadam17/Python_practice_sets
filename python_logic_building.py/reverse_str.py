str =input("Enter a string :")
print("Reverse of the string is :",str[::-1])
# another logic for reverse string
rev = ""
for i in str:
    rev = i + rev
print("Reverse of the string is :",rev)
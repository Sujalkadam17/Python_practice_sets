str = input("Enter a string :")
str = str.replace(" ","")
print("String after removing spaces is :",str)

# another logic for removing spaces from string
str = input("Enter a string :")
str = "".join(str.split())
print("String after removing spaces is :",str)

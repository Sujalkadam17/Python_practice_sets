import datetime as dt

str = input("Enter your name: ")

print("Good Afternoon,",str,"!")

print(f'''Dear <|{str}|>, 
      you are selected !
      Date: <|{dt.datetime.now()}|>''')

#finding double spaces between words

str = input("Enter a string: ")

if "  " in str:
    print("Double spaces found")

    #replacing double spaces with single space
    str.replace("  "," ")
    print("After replacing double spaces with single space: ",str)
else:
    print("Double spaces not found")




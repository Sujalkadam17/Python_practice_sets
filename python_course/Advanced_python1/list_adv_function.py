from functools import reduce
table_7 = [x*7 for x in range(1,11)]
print(table_7)

#to convert table in vertical string of numbers
table_7 = reduce(lambda x,y: str(x) + "\n" + str(y), table_7)
print(table_7)

#above table is like these
check = "hii \nhello \nhow are you"
check2 = "hey" + "\n" + "hello" + "\n" + "how are you"
print(check)
print(check2)
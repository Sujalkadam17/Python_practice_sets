def pattern(n):
    for i in range(n,0,-1):
        print("* "*i,end=" ")
        print()
pattern(int(input("Enter the number :")))

#function to remove name from list
def list_name_remove(name,lst):
    for i in lst:
        if i.lower() == name.lower():
            list.remove(i)
    return list
name = input("Enter the name :")
list = ['Sujal','LEO','ROHIT','Virat','Starc','Surya','Hardik','Nikky P','Boult']
print("List before removing name :",list)
print("List after removing name :",list_name_remove(name,list))

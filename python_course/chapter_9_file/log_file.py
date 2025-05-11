
 #to find line number where python is present 
with open("log_file.txt","r+") as f:
    content = f.read()
    f.seek(0)
    no = 0
    lines = f.readlines()
    print(lines,type(lines))
    for i in lines:
        no += 1
        if "python" in i:
            print("Python is present in the file")
            print(f"Line number is {no}")
            break

'''
#to check if python is present in the file 
with open("log_file.txt","r+") as f:
    content = f.read()
    #print(content)
    lst = content.split()
    for i in lst:
        if i.lower() == "python":
            print("Python is present in the file")

            break
    else:
        print("Python is not present in the file")
'''

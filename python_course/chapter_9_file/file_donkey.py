with open("file_donkey.txt", "r+") as f:
    f.seek(0)   # Move the file pointer to the beginning
    content = f.read().lower()
    lst = content.split()
    print(lst)
    lst = ["######" if word == "donkey" else word for word in lst]
    print(lst)
    f.seek(0)  # Move the file pointer to the beginning
    f.write(" ".join(lst)) # Write the modified content back to the file
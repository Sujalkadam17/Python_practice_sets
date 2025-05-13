import shutil #using shutil module
import os #using os module

source = r"c:\Users\Sujal Amit Kadam\OneDrive\Documents\Desktop\python\Ultimate_python\chapter_9_file\rename_text_file.txt"
dest = r"c:\Users\Sujal Amit Kadam\OneDrive\Documents\Desktop\python\Ultimate_python\chapter_9_file\file_for_rename.txt"

##### please comment out any one of the following methods to avoid error #####

#method 1 rename file using shutil module

try:
    if shutil.move(source , dest):
        print("File renamed successfully")
except Exception as e:
    print("File not renamed")
    print(e)

#method 2 rename file using os module
try:
    if os.rename(source,dest):
        print("File renamed successfully")  
except Exception as e:
    print("File not renamed")
    print(e)
        
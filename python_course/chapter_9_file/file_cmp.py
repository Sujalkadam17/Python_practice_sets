import filecmp
def is_file_same(file1,file2):
    return filecmp.cmp(file1,file1,shallow=False)

file1 = r"c:\Users\Sujal Amit Kadam\OneDrive\Documents\Desktop\python\Ultimate_python\chapter_9_file\log_file.txt"
file2 = r"c:\Users\Sujal Amit Kadam\OneDrive\Documents\Desktop\python\Ultimate_python\chapter_9_file\log_file_copy.txt"

if is_file_same(file1,file2):
    print("Files are same")
else:
    print("Files are not same")
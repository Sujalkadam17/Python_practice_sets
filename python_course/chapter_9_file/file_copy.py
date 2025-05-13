import shutil #copy file using shutil module
import os #copy file using os module

# Copy file using shutil module
shutil.copy("log_file.txt","log_file_copy.txt")

# Copy file using os module and also giving path
os.system(r'copy "log_file.txt" "c:\Users\Sujal Amit Kadam\OneDrive\Documents\Desktop\python\Ultimate_python\log_file_copy_by_os.txt"')


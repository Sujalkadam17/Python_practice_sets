class Student:
    def __init__(self, name, age):
        self.name = name  # Data member 
        self.age = age    # Data member 
 
    def display(self):  # Function 
        print(f"Student Name: {self.name}, Age: {self.age}") 
 
# Creating an object 
s1 = Student("Leo", 20) 
s1.display()  # Calling function using object 

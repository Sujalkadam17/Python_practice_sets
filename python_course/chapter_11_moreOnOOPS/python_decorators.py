class person:
    def __init__(self):
        self._name = None
        self._age = None

#property method must be written before setter 
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    #setter 
    @name.setter
    def name(self, nme):
        self._name = nme

    @age.setter
    def age(self, val):
        if val < 0:
            print("Age cannot be negative")
        else:
            self._age = val

    @age.deleter
    def age(self):
        self._age = None
        print("Age deleted")

obj = person()
obj.name = "Sujal"
obj.age = 20
print(f"Name is {obj.name} and age is {obj.age}")
obj.age = 5
print(f"Name is {obj.name} and age is {obj.age}")
del obj.age
print(f"Name is {obj.name} and age is {obj.age}")




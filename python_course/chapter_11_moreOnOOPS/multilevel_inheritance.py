class animals:
    def __init__(self):
        print("This is an Animal")

class pet(animals):
    def __init__(self):
        super().__init__()
        print("Pet animal")

class dog(pet):
    def __init__(self):
        super().__init__()
        print("Dog is a pet animal")
        
    @staticmethod
    def bark():
        print("Bow Bow !")

ob = dog()
ob.bark()

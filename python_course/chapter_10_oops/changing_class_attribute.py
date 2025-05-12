class Myclass:
    a = 17
    @staticmethod 
    def greet():
        print("Hello Sujal !")
obj = Myclass()
obj.a = 23
print(obj.a)  # 23
obj.greet()  # Hello Sujal !
print(Myclass.a)  # 17
class BCA:
    def __init__(slf,name): #checking using slf instead self no impact it works 
        slf.name = name
    def fy(slf):
        print(f"Welcome {slf.name} to FYBCA")
        print("Wish you all the best for your future")
    def sy(slf ,name):
        print(f"Welcome {name} to SYBCA")
        print("Wish you all the best for your future")


ob = BCA("Sujal")
ob.fy()
ob.sy("Leo")


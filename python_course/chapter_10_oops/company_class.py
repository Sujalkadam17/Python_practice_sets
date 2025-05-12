class programmer:
    company = "microsoft"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin

suj = programmer("Sujal", 100000, 1711)
print(suj.name, suj.salary,suj.pin,suj.company)
leo = programmer("leo", 120000, 1232)
print(leo.name, leo.salary,leo.pin,leo.company)

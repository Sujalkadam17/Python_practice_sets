#function to onvert celsius to fahrenheit
def cel_to_far(celsius):
    return (celsius*1.8) + 32

#function to convert fahrenheit to celsius
def far_to_cel(fahrenheit):
    return (fahrenheit - 32) / 1.8

#function to convert celsius to kelvin
def cel_to_kel(celsius):
    return celsius + 273.15

cel = int(input("Enter celcius to convert into fahrenheit:"))
far = int(input("Enter fahrenheit to convert into celsius:"))

print(f"{cel} celsius to fahrenheit",cel_to_far(cel))
print(f"{far} fahrenheit to celsius",far_to_cel(far))
print(f"{cel} celsius to kelvin",cel_to_kel(cel))
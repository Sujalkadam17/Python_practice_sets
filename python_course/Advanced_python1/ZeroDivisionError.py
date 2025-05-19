try:
    a = int(input("Enter value of a :"))
    b = int(input("Enter value of b :"))
    if b == 0 :
        raise ZeroDivisionError("Infinite")
    print(f"division of {a} / {b} = {a / b}")

except Exception as e:
    print(e)

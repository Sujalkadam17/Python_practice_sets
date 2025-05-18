#generating and storing multiplication table in a file using list comprehension
def generate_table_store(n):
    #table = [i*n for i in range(1, 11)]
    table = [f"{n} x {i} = {i*n}" for i in range(1, 11)]
    with open(r"c:\Users\Sujal Amit Kadam\OneDrive\Documents\Desktop\python\Ultimate_python\advanced_python\Table.txt","w") as f:
        f.write("\n".join(table))

n = int(input("Enter a number to generate multiplication table: "))
generate_table_store(n)
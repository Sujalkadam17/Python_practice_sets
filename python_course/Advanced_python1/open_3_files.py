try:
    with(
        open("file1.txt", "r") as f1,
        open("file2.txt", "r") as f2,
        open("file3.txt", "r") as f3
        ):
        print(f1.read())
        print(f2.read())
        print(f3.read())
            
except FileNotFoundError as e:
    print(f"Error: {e}")

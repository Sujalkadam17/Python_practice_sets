# The code reads a file named "poem.txt" and checks if the word "twinkle" is present in each line. 
# If found, it prints the line; otherwise, it prints "Word not found" and breaks the loop.
with open("poem.txt") as f:
    lines = f.readlines()
    for l in lines :
        if "twinkle" in l.lower():
            print(l.strip())
        
           
        

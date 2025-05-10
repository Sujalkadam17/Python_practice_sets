import random 
def game():
    return random.randint(0, 100) # Random high score between 0 and 100

score = game()
with open("high_score.txt", "r+") as f:
    f.seek(0)
    curr_high_score = int(f.readline().strip() or 0)
    if score > curr_high_score:
        print(f"New high score! {score}")
        f.seek(0)  # Move the file pointer to the beginning
        f.truncate()  # Clear the file content
        f.write(f"{score}\n")  # Write the new high score
        f.write(f"High score {score}")
    else:
        print("No new high score")
        print(f"{f.readline()}") 


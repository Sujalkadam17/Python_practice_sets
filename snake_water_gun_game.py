#Snake water gun game
import random # to generate random choices for the computer

print("Welcome to Snake🐍 Water🌊 Gun🔫 Game!")
print("📜Rules:")
print("1️⃣ Snake🐍 beats Water🌊")
print("2️⃣ Water🌊 beats Gun🔫")
print("3️⃣ Gun🔫 beats Snake🐍")
start = input("🟢Press Enter to start the game...")

info = {
    's': 'Snake 🐍',
    'w': 'Water 🌊',
    'g': 'Gun 🔫'
}

while True:
    print("\n🆕 Round!\n")
    computer = random.choice(['s', 'w', 'g'])
    print("Enter 's' for snake🐍, 'w' for water🌊, 'g' for gun🔫")
    user = input("\nEnter your choice: ").lower() #lower() to handle case sensitivity
    print("\nYour choice:", info[user])
    print("Computer choice:", info[computer])

    if user == computer:
        print("It's a Draw !")
    else:
        if (user == 's' and computer == 'w') or (user == 'w' and computer == 'g') or (user == 'g' and computer == 's'):
            print(" You Won ! 🥳")
        elif (user == 's' and computer == 'g') or (user == 'w' and computer == 's') or (user == 'g' and computer == 'w'):
            print(" You Lose ! 😢")
        else:
            print("Invalid input! Please enter 's', 'w', or 'g'.")
    user = input("Press Enter to play again or type 'exit' to quit: ").lower()
    if user == 'exit':
        print("Thanks for playing!")
        break

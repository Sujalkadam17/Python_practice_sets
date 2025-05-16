import pyttsx3 
engine = pyttsx3.init()
engine.say("Welcome Buddy... Type here To Read Aloud")
engine.runAndWait()

while True:
    engine.setProperty('rate', 150)  # Speed of speech
    text = input("Type here To Read Aloud : ")
    if text == "exit":
        break

    print("Type 'exit' to stop the program")
    engine.say(text)
    engine.runAndWait()

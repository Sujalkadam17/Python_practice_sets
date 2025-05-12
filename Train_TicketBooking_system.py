class Train:
    def __init__(self,lst):
        self.lst = lst #storing the list of tickets in the class
    def book_ticket(self):

        src =  input("📍 Enter source station: ")
        dest = input("📍 Enter destination station: ")
        date = input("📅 Enter travel date (DD/MM/YYYY): ")
        name = input("ℹ️  Enter passenger name: ")
        dict = {
            "source": src,
            "destination": dest,    
            "date" : date,
            "name" : name,
            "status": "Booked"
        }
        self.lst.append(dict) #appending booked tickets into list
        print("Ticket booked successfully! ✅")
        print("Happy Journey ! 😊")
        


    def cancel_ticket(self):
        name = input("Enter passenger name to cancel ticket: ")
        for ticket in self.lst:
            if ticket["name"].lower() == name.lower(): #lower() to handle case insensitivity
                self.lst.remove(ticket) # removing canceled ticket from list
                print("Ticket cancelled successfully!📩")
                
    def view_ticket(self):
        if not self.lst: #if list is empty
            print("No tickets booked.❌")
        else:
            name = input("🔄️ Enter passenger name to view ticket: ")
            for ticket in self.lst:
                if ticket["name"].lower() == name.lower():
                    print(f"🔄️ Booked Tickets for {name}:\n 📍 Source : {ticket['source']} --> 📍 Destination : {ticket['destination']}\n 📅 Date : {ticket['date']}\n ℹ️  Passenger Name : {ticket['name']}\n 📩 Status : {ticket['status']}\n")

lst = [] #for storing ticket information
tr = Train(lst) #instantiating the class

while True: #while loop to keep program running

#exception handling 
    try:
        print("Welcome to the train ticket booking system 🚆")
        print("1. Book Ticket 📲")
        print("2. Cancel Ticket ❌")
        print("3. View Ticket 📩")
        print("4. Exit 🏠" )

        choice = int(input("Enter your choice: "))
        if choice == 1:
            tr.book_ticket()
        elif choice == 2:
            tr.cancel_ticket()
        elif choice == 3:
            tr.view_ticket()
        elif choice == 4:
            break
        else:
            print("Invalid choice, please try again.")

    # to handle value error
    except ValueError:
        print("Invalid input! Please enter a number.")

    #to handle other exception
    except Exception as e:
        print("An error occurred:", e)
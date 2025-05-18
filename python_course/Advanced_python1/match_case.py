def day( n ) -> str:
    match n:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid day. Please enter a number between 1 and 7"
        
num = int(input("Enter a number between 1 and 7: "))
print(day(num))

def https_request(req):
    match req:
        case "GET":
            return "GET request received"
        case "POST":
            return "POST request received"
        case "PUT":
            return "PUT request received"
        case "DELETE":
            return "DELETE request received"
        case _:
            return "Invalid request type"
        
req = input("Enter HTTP request type (GET, POST, PUT, DELETE): ")
print(https_request(req))

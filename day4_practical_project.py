class Room:
    def __init__(self, room_number, room_type, price):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.is_booked = False

    def book_room(self):
        if self.is_booked:
            print(f"Room {self.room_number} is already booked.")
            return False
        
        self.is_booked = True
        print(f"Room {self.room_number} has been successfully booked.")

    def display_details(self):
        status = "Booked" if self.is_booked else "Available"
        print(f"Room Number: {self.room_number}")
        print(f"Type of Room: {self.room_type}")
        print(f"Price: ₹{self.price}")
        print(f"Status: {status}")

room = Room(101, "Deluxe", 5000)

room.display_details() # Display initial details
room.book_room() #Book the room
room.display_details() #Display details after booking
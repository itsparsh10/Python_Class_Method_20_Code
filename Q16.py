#Build a hotel reservation system with classes for rooms, guests, and reservations.
# Implement methods for checking room availability, booking rooms, and generating invoices.
class Room:
    def __init__(self, room_number, capacity, rate_per_night):
        self.room_number = room_number
        self.capacity = capacity
        self.rate_per_night = rate_per_night
        self.is_booked = False

    def check_availability(self):
        return not self.is_booked

    def book_room(self):
        if not self.is_booked:
            self.is_booked = True
            return True
        else:
            return False


class Guest:
    def __init__(self, guest_name, email):
        self.guest_name = guest_name
        self.email = email


class Reservation:
    def __init__(self, guest, room, nights):
        self.guest = guest
        self.room = room
        self.nights = nights

    def generate_invoice(self):
        total_cost = self.room.rate_per_night * self.nights
        return f"Invoice for {self.guest.guest_name}:\nRoom: {self.room.room_number}\nNights: {self.nights}\nTotal Cost: {total_cost}"


class Hotel:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def find_available_rooms(self):
        return [room for room in self.rooms if room.check_availability()]

    def book_room(self, guest, nights):
        available_rooms = self.find_available_rooms()
        if available_rooms:
            room_to_book = available_rooms[0]
            if room_to_book.book_room():
                reservation = Reservation(guest, room_to_book, nights)
                return reservation
        return None


def main():
    # Create a hotel
    my_hotel = Hotel()

    # Add rooms to the hotel
    room1 = Room(101, 2, 100)
    room2 = Room(102, 4, 150)
    my_hotel.add_room(room1)
    my_hotel.add_room(room2)

    # Create a guest
    a=input("Enter your name: ")
    b=input("Enter your email address: ")
    guest1 = Guest(a,b)
    print("Welcome to OYO hotels!")
    while True:
        print("1.Check available rooms")
        print("2.Book Room")
        print("3.Exit")
        a=int(input("Enter your choice: "))
        if a==1:
            # Check available rooms
            available_rooms = my_hotel.find_available_rooms()
            print("Available Rooms:", [room.room_number for room in available_rooms])
        elif a==2:
            # Book a room for the guest
            reservation1 = my_hotel.book_room(guest1, nights=3)
            if reservation1:
                print("Room booked successfully!")
                print(reservation1.generate_invoice())
            else:
                print("No available rooms.")
        elif a==3:
            print("Thank You!")
            break
        else:
            print("Invalid choice")
    
if __name__ == "__main__":
    main()
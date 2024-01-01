# Create a conference room booking system with classes for rooms, reservations,
# and users. Include methods for checking room availability, booking time slots, and
# sending notifications.
# Create a conference room booking system with classes for rooms, reservations,
# and users. Include methods for checking room availability, booking time slots, and
# sending notifications.
from datetime import datetime, timedelta

class Room:
    def __init__(self, room_number, capacity):
        self.room_number = room_number
        self.capacity = capacity
        self.schedule = {}

    def check_availability(self, start_time, end_time):
        for booked_start, booked_end, _ in self.schedule.values():
            if start_time < booked_end and end_time > booked_start:
                return False
        return True

    def book_room(self, user, start_time, end_time):
        if self.check_availability(start_time, end_time):
            reservation_id = len(self.schedule) + 1
            self.schedule[reservation_id] = (start_time, end_time, user)
            return reservation_id
        else:
            return None

class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

class ConferenceRoomBookingSystem:
    def __init__(self):
        self.rooms = {}
        self.users = {}

    def add_room(self, room_number, capacity):
        room = Room(room_number, capacity)
        self.rooms[room_number] = room

    def add_user(self, user_id, name, email):
        user = User(user_id, name, email)
        self.users[user_id] = user

    def check_room_availability(self, room_number, start_time, end_time):
        if room_number in self.rooms:
            room = self.rooms[room_number]
            return room.check_availability(start_time, end_time)
        else:
            return False

    def book_room(self, user_id, room_number, start_time, end_time):
        if user_id in self.users and room_number in self.rooms:
            user = self.users[user_id]
            room = self.rooms[room_number]
            reservation_id = room.book_room(user, start_time, end_time)
            if reservation_id is not None:
                self.notify_user(user, room, start_time, end_time)
                return f"Reservation successful! Reservation ID: {reservation_id}"
            else:
                return "Room not available for the specified time slot."
        else:
            return "Invalid user ID or room number."

    def notify_user(self, user, room, start_time, end_time):
        print(f"Notification sent to {user.name} ({user.email}):")
        print(f"You have successfully booked Room {room.room_number} from {start_time} to {end_time}.")

def main():
    booking_system = ConferenceRoomBookingSystem()

    booking_system.add_room("A101", 20)
    booking_system.add_room("A102", 20)
    booking_system.add_room("A103", 20)

    print("Welcome to conference room booking system!")
    a = input("Enter your name: ")
    b = input("Enter your email: ")

    while True:
        print("1. Check room availability")
        print("2. Book a room")
        print("3. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            room_number = input("Enter room number: ")
            c = int(input("Enter start year(YYYY): "))
            d = int(input("Enter start month(MM): "))
            e = int(input("Enter start day(DD): "))
            f = int(input("Enter start hour(HH)(24H): "))
            g = int(input("Enter start minute(MM): "))
            h = int(input("Enter number of hours to stay: "))
            i = int(input("Enter number of minutes to stay: "))

            start_time = datetime(c, d, e, f, g)
            end_time = start_time + timedelta(hours=h, minutes=i)

            available = booking_system.check_room_availability(room_number, start_time, end_time)
            if available:
                print(f"Room {room_number} is available for the specified time slot.")
            else:
                print(f"Room {room_number} is not available for the specified time slot.")

        elif choice == 2:
            booking_system.add_user(1, a, b)
            room_number = input("Enter room number: ")
            c = int(input("Enter start year(YYYY): "))
            d = int(input("Enter start month(MM): "))
            e = int(input("Enter start day(DD): "))
            f = int(input("Enter start hour(HH)(24H): "))
            g = int(input("Enter start minute(MM): "))
            h = int(input("Enter number of hours to stay: "))
            i = int(input("Enter number of minutes to stay: "))

            start_time = datetime(c, d, e, f, g)
            end_time = start_time + timedelta(hours=h, minutes=i)

            result = booking_system.book_room(1, room_number, start_time, end_time)
            print(result)

        elif choice == 3:
            print("Thank you!")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

from abc import ABC, abstractmethod


# Abstraction: every passenger type must provide a discount
class Passenger(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_discount_percent(self):
        pass


# Inheritance + Polymorphism: each type gives its own discount
class RegularPassenger(Passenger):
    def get_discount_percent(self):
        return 0


class StudentPassenger(Passenger):
    def get_discount_percent(self):
        return 10


class Flight:
    def __init__(self, code, airline, source, destination, seats, fare):
        self.code = code
        self.airline = airline
        self.source = source
        self.destination = destination
        self.__seats = seats          # private (encapsulation)
        self.fare = fare

    def get_seats(self):
        return self.__seats

    def book_seats(self, count):      # only way to reduce seats
        if 0 < count <= self.__seats:
            self.__seats -= count
            return True
        return False


class Booking:
    def __init__(self, booking_id, flight, passenger, tickets, subtotal, discount, total):
        self.booking_id = booking_id
        self.flight = flight
        self.passenger = passenger
        self.tickets = tickets
        self.subtotal = subtotal
        self.discount = discount
        self.total = total


class FlightBookingSystem:
    def __init__(self):
        self.flights = [
            Flight("PN101", "Kiran Air", "Pune", "Delhi", 20, 4000),
            Flight("MB202", "Sky Jet", "Mumbai", "Bengaluru", 15, 3500),
            Flight("PH303", "Indus Wings", "Pune", "Hyderabad", 10, 2800),
        ]
        self.bookings = []
        self.next_id = 1001

    def display_flights(self):
        print("\nCode   Airline      Source    Destination  Seats  Fare")
        for f in self.flights:
            print(f"{f.code:<7}{f.airline:<13}{f.source:<10}{f.destination:<13}{f.get_seats():<7}Rs.{f.fare}")

    def find_flight(self, code):
        for f in self.flights:
            if f.code == code.strip().upper():
                return f
        return None

    def validate_booking_details(self, flight, name, age, tickets):
        if flight is None:
            return "Invalid flight code."
        if name.strip() == "":
            return "Name cannot be blank."
        if age <= 0:
            return "Age must be greater than 0."
        if tickets <= 0:
            return "Tickets must be greater than 0."
        if tickets > flight.get_seats():
            return "Not enough seats available."
        return None

    def calculate_fare(self, flight, passenger, tickets):
        subtotal = flight.fare * tickets
        discount = subtotal * passenger.get_discount_percent() / 100
        return subtotal, discount, subtotal - discount

    def confirm_booking(self, flight, passenger, tickets):
        subtotal, discount, total = self.calculate_fare(flight, passenger, tickets)
        flight.book_seats(tickets)
        booking = Booking(f"BK{self.next_id}", flight, passenger, tickets, subtotal, discount, total)
        self.next_id += 1
        self.bookings.append(booking)
        return booking

    def display_summary(self, b):
        print(f"Booking ID: {b.booking_id}")
        print(f"Flight: {b.flight.code} | {b.flight.source} to {b.flight.destination}")
        print(f"Passenger: {b.passenger.name} (Age {b.passenger.age})")
        print(f"Tickets: {b.tickets}")
        print(f"Base fare per ticket: Rs.{b.flight.fare}")
        print(f"Subtotal: Rs.{b.subtotal:.0f}")
        print(f"Discount ({b.passenger.get_discount_percent()}%): Rs.{b.discount:.0f}")
        print(f"Final amount: Rs.{b.total:.0f}")

    def book_flight(self):
        code = input("Enter flight code: ")
        name = input("Enter passenger name: ")
        try:
            age = int(input("Enter age: "))
            p_type = input("Passenger type (Regular/Student): ").strip().lower()
            tickets = int(input("Enter number of tickets: "))
        except ValueError:
            print("Booking failed: Please enter numbers for age and tickets.")
            return

        if p_type not in ("regular", "student"):
            print("Booking failed: Passenger type must be Regular or Student.")
            return

        flight = self.find_flight(code)
        error = self.validate_booking_details(flight, name, age, tickets)
        if error:
            print("Booking failed:", error)
            print("No booking was created. Available seats remain unchanged.")
            return

        if p_type == "student":
            passenger = StudentPassenger(name.strip(), age)
        else:
            passenger = RegularPassenger(name.strip(), age)

        booking = self.confirm_booking(flight, passenger, tickets)
        print("\nBooking confirmed!")
        self.display_summary(booking)

    def view_booking(self):
        if not self.bookings:
            print("No booking found yet. Please book a flight first.")
        else:
            self.display_summary(self.bookings[-1])

    def run(self):
        while True:
            print("\nWelcome to Kiran Air Booking")
            print("1. View Flights\n2. Book Flight\n3. View Booking\n4. Exit")
            choice = input("Enter choice: ").strip()
            if choice == "1":
                self.display_flights()
            elif choice == "2":
                self.book_flight()
            elif choice == "3":
                self.view_booking()
            elif choice == "4":
                print("Thank you for using Kiran Air Booking!")
                break
            else:
                print("Invalid choice. Enter 1 to 4.")


if __name__ == "__main__":
    FlightBookingSystem().run()
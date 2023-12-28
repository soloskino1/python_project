import random

class Flight:
    def __init__(self, flight_number, destination, capacity):
        # Initialize the flight parameters
        self.flight_number = flight_number
        self.destination = destination
        self.capacity = capacity
        self.available_seats = capacity
        self.bookings = []

    def display_info(self):
        # Display information about the flight schedule
        print(f"Flight {self.flight_number} to {self.destination}")
        print(f"List of available Seats: {self.available_seats}/{self.capacity}")
        print("Bookings:")
        for booking in self.bookings:
            print(f"  - {booking}")

    def book_seat(self, passenger_name, email):
        # Book a seat for a passenger
        if self.available_seats > 0:
            seat_number = random.randint(1, self.capacity)
            self.bookings.append({
                'passenger_name': passenger_name,
                'email': email,
                'seat_number': seat_number
            })
            self.available_seats -= 1
            print(f"The seat number {seat_number} is booked for {passenger_name}")
        else:
            print("Sorry, no available seats.")

    def cancel_booking(self, passenger_name):
        # Cancel a booking for a passenger
        for booking in self.bookings:
            if booking['passenger_name'] == passenger_name:
                self.bookings.remove(booking)
                self.available_seats += 1
                print(f"Booking canceled for {passenger_name}")
                break
        else:
            print(f"No booking found for {passenger_name}")


class FlightBookingSystem:
    def __init__(self):
        # Initialize the flight booking system with an empty list of flights
        self.flights = []

    def add_flight(self, flight):
        # Add a flight to the system
        self.flights.append(flight)

    def display_available_flights(self):
        # Display information about all available flights
        print("Available Flights:")
        for flight in self.flights:
            flight.display_info()
            print()

    def search_flight_by_destination(self, destination):
        # Search for flights based on destination
        matching_flights = [flight for flight in self.flights if flight.destination.lower() == destination.lower()]
        if matching_flights:
            print(f"Flights to {destination}:")
            for flight in matching_flights:
                flight.display_info()
                print()
        else:
            print(f"No flights found to {destination}")


if __name__ == "__main__":
    flight_booking_system = FlightBookingSystem()

    # Add some flights
    flight1 = Flight("AY001", "New York", 150)
    flight2 = Flight("AN002", "Paris", 100)
    flight3 = Flight("AP003", "London", 120)

    flight_booking_system.add_flight(flight1)
    flight_booking_system.add_flight(flight2)
    flight_booking_system.add_flight(flight3)

    # Display available flights
    flight_booking_system.display_available_flights()

    # Prompt user to search for flights
    destination = input("Enter destination to search for flights: ")
    flight_booking_system.search_flight_by_destination(destination)

    # Prompt user to book a seat
    flight_number = input("Enter the flight number to book a seat: ")
    selected_flight = next((flight for flight in flight_booking_system.flights if flight.flight_number == flight_number), None)

    if selected_flight:
        passenger_name = input("Enter your name: ")
        email = input("Enter your email address: ")
        selected_flight.book_seat(passenger_name, email)

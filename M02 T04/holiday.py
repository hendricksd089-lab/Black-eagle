PRICE_PER_NIGHT = 140
PRICE_PER_DAY_CAR = 60

FLIGHT_PRICES = {
    "new york": 650,
    "london": 550,
    "paris": 600,
    "tokyo": 900,
}


def hotel_cost(num_nights):
    """Return total hotel cost for num_nights nights."""
    return num_nights * PRICE_PER_NIGHT


def plane_cost(city_flight):
    """Return flight cost for the given city name (case-insensitive).
    Returns 0 for unknown destinations.
    """
    if not isinstance(city_flight, str):
        return 0
    return FLIGHT_PRICES.get(city_flight.lower().strip(), 0)


def car_rental_cost(rental_days):
    """Return total car rental cost for rental_days days."""
    return rental_days * PRICE_PER_DAY_CAR


def holiday_cost(num_nights, city_flight, rental_days):
    """Return combined holiday cost (hotel + flight + car)."""
    return hotel_cost(num_nights) + plane_cost(city_flight) + car_rental_cost(rental_days)


def _get_non_negative_int(prompt):
    """Prompt the user until a non-negative integer is entered."""
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a non-negative number.")
                continue
            return value
        except ValueError:
            print("That's not a valid number. Please enter an integer.")


def main():
    print("Welcome to the Holiday Budget Calculator!")
    print("Available flight destinations: New York, London, Paris, Tokyo")

    city_flight = input("Enter the city you will be flying to: ").strip()
    num_nights = _get_non_negative_int("Enter the number of nights you will be staying at the hotel: ")
    rental_days = _get_non_negative_int("Enter the number of days you will be renting a car: ")

    flight_cost = plane_cost(city_flight)

    if flight_cost == 0:
        print(f'\nError: "{city_flight}" is not a valid destination choice. Please run the program again.')
        return

    total_cost = holiday_cost(num_nights, city_flight, rental_days)

    print("\n==================================")
    print("HOLIDAY COST RECEIPT")
    print("==================================")
    print(f"Destination:       {city_flight.title()}")
    print(f"Flight Cost:       ${flight_cost}")
    print(f"Hotel Cost:        ${hotel_cost(num_nights)}")
    print(f"Car Rental Cost:   ${car_rental_cost(rental_days)}")
    print("==================================")
    print(f"Total Holiday Cost: ${total_cost}")
    print("==================================")


if __name__ == "__main__":
    main()

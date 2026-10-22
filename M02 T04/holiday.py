from builtins import print


def hotel_cost(num_nights):
    price_per_night = 140
    return num_nights * price_per_night


def plane_cost(city_flight):
    city = city_flight.lower().strip()

    if city == "new york":
        return 650
    elif city == "london":
        return 550
    elif city == "paris":
        return 600
    elif city == "tokyo":
        return 900
    else:
        return 0


def car_rental_cost(rental_days):
    price_per_day = 60
    return rental_days * price_per_day


def holiday_cost(num_nights, city_flight, rental_days):
    total_hotel = hotel_cost(num_nights)
    total_flight = plane_cost(city_flight)
    total_car = car_rental_cost(rental_days)

    return total_hotel + total_flight + total_car


print("Welcome to the Holiday Budget Calculator!")
print("Available flight destinations: New York, London, Paris, Tokyo")

city_flight = input("Enter the city you will be flying to: ")
num_nights = int(input("Enter the number of nights you will be staying at the hotel: "))
rental_days = int(input("Enter the number of days you will be renting a car: "))

flight_cost = plane_cost(city_flight)

if flight_cost == 0:
    print(f'\nError: "{city_flight}" is not a valid destination choice. Please run the program again.')
else:
    total_cost = holiday_cost(num_nights, city_flight, rental_days)

    print("\n==================================")
    print("HOLIDAY COST RECEIPT")
    print("==================================")
    print(f"Destination:   {city_flight.title()}")
    print(f"Flight Cost:      ${flight_cost}")
    print(f"Hotel Cost:      ${hotel_cost(num_nights)}")
    print(f"Car Rental Cost: ${car_rental_cost(rental_days)}")
    print("==================================")
    print(f"Total Holiday Cost: ${total_cost}")
    print("==================================")
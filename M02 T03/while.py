numbers = []

while True:
    try:
        number = float(input("Enter a number (-1 to stop): "))

        if number == -1:
            break
        if number == 0:
            print("0 is not a valid input.")
            continue

        numbers.append(number)

    except ValueError:
        print("Please enter a valid number.")

if numbers:
    count = len(numbers)
    total_sum = sum(numbers)
    average = total_sum / count
    print(f"\nYou entered {count} numbers.")
    print(f"The average of the entered numbers is: {average}")
else:
    print("\nNo numbers were entered, so the average cannot be calculated.")
            

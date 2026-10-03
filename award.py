cycling_time = float(input("Enter cycling time in minutes:"))
swimming_time = float(input("Enter swimming time in minutes: "))
running_time = float(input("Enter running time in minutes: "))

total_time = cycling_time + swimming_time + running_time

if total_time <= 100:
    award = "Honorary Colours"
elif 101 <= total_time <= 110:
    award = "Honorary Scroll"
else:
    award = "No Award"

    print("Total time:", total_time, "minutes")
    print("Award:", award)
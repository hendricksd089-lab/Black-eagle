rows = int(input("Enter number of rows: "))

for i in range(1, rows * 2):
    if i <= rows:
        print("*" * i)
    else:
        print("*" * (rows * 2 - i))
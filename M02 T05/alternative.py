user_string = input("Enter a string for character alternation:")

char_result = ""
for index in range(len(user_string)):
    if index % 2 == 0:
        char_result += user_string[index].upper()
    else:
        char_result += user_string[index].lower()

        print("Character-alternated string:", char_result)
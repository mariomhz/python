user_input = input("Enter a name in the format LASTNAME, FIRSTNAME: ")
last_name, first_name = map(str.strip, user_input.split(","))
print(f"Converted name: {first_name} {last_name}")
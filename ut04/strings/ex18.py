user_input = input("enter a string: ")
upper_case = sum(1 for char in user_input if char.isupper())
lower_case = sum(1 for char in user_input if char.islower())
print(f"uppercase letters: {upper_case}, lowercase letters: {lower_case}")
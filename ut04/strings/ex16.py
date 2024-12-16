user_input = input("enter a string: ").lower()
print("the string is a palindrome." if user_input == user_input[::-1] else "the string is not a palindrome.")
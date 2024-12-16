user_input = input("enter a sentence: ")
vowels = set("aeiouAEIOU")
found_vowels = set(user_input) & vowels
print(f"the vowels found were: {', '.join(found_vowels)}")
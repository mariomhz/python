import random
import string
letters = ''.join(random.choices(string.ascii_uppercase, k=100))
print("generated string: ", letters)
counts = {letter: letters.count(letter) for letter in string.ascii_uppercase}
for letter, count in counts.items():
    print(f"{letter}: {count}")
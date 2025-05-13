import random
import string

def generate_email(input):
    input = input.lower().replace(" ", "")
    options = [
        f"{input}{random.randint(10, 99)}",
        f"{random.randint(1, 99)}{input}",
        f"{input}{random.randint(100, 999)}",
        f"{input}{random.choice(string.ascii_lowercase)}{random.randint(1, 99)}"
    ]
    return random.choice(options) + "@gmail.com"

def generate_pass(length=50):
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return password

name_input = input("enter an input: ")
email = generate_email(name_input)
password = generate_pass()

print(f"email: {email}")
print(f"password: {password}")
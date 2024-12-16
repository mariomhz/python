isbn = input("Enter a 13-digit ISBN: ")
if len(isbn) != 13 or not isbn.isdigit():
    print("Invalid ISBN format.")
else:
    total = sum(int(isbn[i]) * (1 if i % 2 == 0 else 3) for i in range(12))
    check_digit = (10 - (total % 10)) % 10
    print("Valid ISBN." if check_digit == int(isbn[-1]) else "Invalid ISBN.")
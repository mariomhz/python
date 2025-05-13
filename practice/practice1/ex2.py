def is_palindrome(s: str) -> bool:
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print(is_palindrome("racecar"))
print(is_palindrome("hello"))
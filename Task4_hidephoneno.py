import re

def hide_numbers(text):
    check_phone = r'(\+84\d+|\d{10})'
    return re.sub(check_phone, "[REDACTED]", text)

s = input()
print(hide_numbers(s))
# Password Strength Checker
# DecodeLabs Internship - Project 1

password = input("Enter your password: ")

length = len(password)

has_upper = False
has_lower = False
has_digit = False
has_symbol = False

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif not char.isalnum():
        has_symbol = True

score = 0

if length >= 8:
    score += 1

if has_upper:
    score += 1

if has_lower:
    score += 1

if has_digit:
    score += 1

if has_symbol:
    score += 1

print("\n----- Password Analysis -----")
print("Length:", length)
print("Uppercase:", has_upper)
print("Lowercase:", has_lower)
print("Numbers:", has_digit)
print("Symbols:", has_symbol)

if score <= 2:
    print("\nPassword Strength: Weak")
elif score <= 4:
    print("\nPassword Strength: Medium")
else:
    print("\nPassword Strength: Strong")
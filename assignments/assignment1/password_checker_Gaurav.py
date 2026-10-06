# Assignment 1 — Password Strength Checker

# Characters that count as special characters
special_characters = "!@#$%&*?"

# Passwords that are too common to be safe (all in lowercase)
common_passwords = ["password", "password1", "password123", "password123!", "passord",
                    "passord123", "123456", "12345678", "qwerty", "qwerty123", "iloveyou", "admin"]

# The password your program should check. To try a different test password,
# move the "#" from that line to the active one.
password = "Sunshine26"
#password = "hello"
#password = "Ban405!"
#password = "sunshine"
#password = "abcdefghij1"
#password = "abcdefghijk1"
#password = "Ban405rock!"
#password = "Blåbær!2"
#password = "correct horse battery"
#password = "Password123!"
#password = "PASSWORD123!"

# Write your code below

# Part 1
def analyse_password(text):
    caps = 0
    small = 0
    nums = 0
    specials = 0

    for letter in text:
        caps += letter.isupper()
        small += letter.islower()
        nums += letter.isdigit()
        specials += letter in special_characters

    return caps, small, nums, specials


# Part 2
def show_checks(text, caps, small, nums, specials):
    checks = [
        len(text) >= 8,
        caps > 0,
        small > 0,
        nums > 0,
        specials > 0
    ]

    messages = [
        ("[OK]   At least 8 characters",
         "[FAIL] At least 8 characters"),
        ("[OK]   At least one uppercase letter",
         "[FAIL] At least one uppercase letter"),
        ("[OK]   At least one lowercase letter",
         "[FAIL] At least one lowercase letter"),
        ("[OK]   At least one digit",
         "[FAIL] At least one digit"),
        ("[OK]   At least one special character (!@#$%&*?)",
         "[FAIL] At least one special character (!@#$%&*?)")
    ]

    for passed, message in zip(checks, messages):
        if passed:
            print(message[0])
        else:
            print(message[1])


# Part 3
def calculate_points(text, counts):
    caps, small, nums, specials = counts

    if len(text) < 8:
        length_score = 0
    elif len(text) < 12:
        length_score = 1
    else:
        length_score = 2

    type_score = 0
    for amount in counts:
        if amount > 0:
            type_score += 1

    return length_score + type_score


def rate_password(text, points):
    if text.lower() in common_passwords:
        return "very weak"

    if len(text) < 8 or points <= 2:
        return "weak"

    if points <= 4:
        return "medium"

    return "strong"


counts = analyse_password(password)

print()
print("Length:             ", len(password))
print("Uppercase letters:  ", counts[0])
print("Lowercase letters:  ", counts[1])
print("Digits:             ", counts[2])
print("Special characters:", counts[3])
print()

show_checks(password, *counts)
print()

total = calculate_points(password, counts)
level = rate_password(password, total)

print("Score:", total, "/ 6")
print("Rating:", level)


# Part 4
def has_space(text):
    return " " in text


passwords_checked = 0
accepted = False

while not accepted:
    entered_password = input("\nChoose a password (or press Enter to quit): ")

    if entered_password == "":
        print("No password chosen. Passwords checked:", passwords_checked)
        break

    passwords_checked += 1
    counts = analyse_password(entered_password)

    print()
    print("Length:             ", len(entered_password))
    print("Uppercase letters:  ", counts[0])
    print("Lowercase letters:  ", counts[1])
    print("Digits:             ", counts[2])
    print("Special characters:", counts[3])
    print()

    show_checks(entered_password, *counts)
    print()

    total_score = calculate_points(entered_password, counts)
    password_level = rate_password(entered_password, total_score)

    print("Score:", total_score, "/ 6")
    print("Rating:", password_level)

    if password_level == "strong" and not has_space(entered_password):
        print()
        print("Password accepted! Passwords checked:", passwords_checked)
        accepted = True
    elif password_level == "strong" and has_space(entered_password):
        print()
        print("Password rejected! Passwords cannot contain spaces.")

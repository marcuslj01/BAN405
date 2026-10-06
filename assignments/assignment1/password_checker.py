# Assignment 1 — Password Strength Checker

# Characters that count as special characters
special_characters = "!@#$%&*?"

# Passwords that are too common to be safe (all in lowercase)
common_passwords = ["password", "password1", "password123", "password123!", "passord",
                    "passord123", "123456", "12345678", "qwerty", "qwerty123", "iloveyou", "admin"]

# The password your program should check. To try a different test password,
# move the "#" from that line to the active one.

# Write your code below

def count_char_types(password):
    uppercase = 0
    lowercase = 0
    digit = 0
    special_chars = 0
    for character in password:
        if character.isupper():
            uppercase += 1
        elif character.islower():
            lowercase += 1
        elif character.isdigit():
            digit += 1
        elif character in special_characters:
            special_chars += 1

    return [uppercase, lowercase, digit, special_chars]

def calculate_score(password):
    score = 0
    is_common = False
    too_short = False

    if str(password).lower() in common_passwords:
        is_common = True
        score = -1 

    # Length points
    if len(password) >= 12: # if length is 12 or more
        score += 2
    elif len(password) >= 8: # if length is 8-11
        score += 1
    else:
        too_short = True
   

    # Type points
    char_types_count = count_char_types(password)
    for count in char_types_count:
        if count > 0:
            score += 1

    return score, is_common, too_short
        
def rate_score(score):
    if score >= 5:
        return "strong"
    elif score >= 3:
        return "medium"
    elif score >= 0:
        return "weak"
    elif score == -1:
        return "very weak"

def check_password(password):
    score, is_common, too_short = calculate_score(password)
    rating = rate_score(score)

    if too_short:
        return f"Score: {score}/6 \nRating: weak"
    if is_common:
        return f"Score: {score}/6 \nRating: very weak"

    return f"Score: {score}/6 \nRating: {rating}"
    
    

# password = "Sunshine26" # OK
# password = "hello" # OK
# password = "Ban405!" # OK
# password = "sunshine" # OK
# password = "abcdefghij1" # OK
# password = "abcdefghijk1" # OK
# password = "Ban405rock!" # OK
# password = "Blåbær!2" # OK
# password = "correct horse battery"# OK
# password = "Password123!" # OK
# password = "PASSWORD123!" # OK

# print(check_password(password))

""" Part 4 """
def get_password():
    checked = 0
    while True:
        password = input("Choose a password (or press Enter to quit): ")
        if password == "": # if pressed enter
            return f"No password chosen. Passwords checked: {checked}"
        

        response = check_password(password)
        print(response)

        if "strong" in response.lower(): # if the word strong is returned
            checked += 1
            return f"Password accepted! Passwords checked: {checked}"
        else:
            checked += 1

print(get_password())

# Assignment 1 — Password Strength Checker

# Characters that count as special characters
special_characters = "!@#$%&*?"

# Passwords that are too common to be safe (all in lowercase)
common_passwords = ["password", "password1", "password123", "password123!", "passord",
                    "passord123", "123456", "12345678", "qwerty", "qwerty123", "iloveyou", "admin"]

# The password your program should check. To try a different test password,
# move the "#" from that line to the active one.
#password = "Sunshine26"
#password = "hello"
#password = "Ban405!"
#password = "sunshine"
#password = "abcdefghij1"
#password = "abcdefghijk1"
#password = "Ban405rock!"
#password = "Blåbær!2"
#password = "correct horse battery"
password = "Password123!"
#password = "PASSWORD123!"

# Write your code below

#Part 1 ---------- Analyze the password

#This first part can be done quite easily with a for loop:

#Firstly defining the booleans before the loop:
uppercase = 0
lower = 0
digit = 0
special = 0

for character in password:
    if character.isupper(): #Checks for uppercase
        uppercase += 1
    if character.islower(): #Checks for lowecase
        lower += 1
    if character.isdigit(): #Checks for digits
        digit += 1
    if character in special_characters: #Checks for special characters
        special += 1
   

print("Length of password is:", len(password))
print("Uppercase letters:", uppercase)
print("Lowercase letters:", lower)
print("Digits:", digit)
print("Special character:", special)

#Tried here to get the same result as the output suggestion in the task 

#Part 2 ----------- Check the rules

#This can also be done with a simple for loop:

#First lets define our rules:

not_common = password.lower() not in common_passwords
lenght_ok = len(password)>=8
lenght_12 =len(password)>=12
has_upper = uppercase>=1
has_lower = lower>=1
has_digit = digit>=1
has_special = special>=1

if not_common: #I added this line later as i did not read it correctly the first time - It seams to work
    print("[Ok] Password is not too common")
else:
    print("[Fail] Password is to common")
if lenght_ok:
    print("[Ok] Contains at least 8 charachters")
else:
    print("[FAIL] Does not contain 8 charachters")
if has_upper:
    print("[Ok] Contains an uppercase charachter")
else:
    print("[Fail] Does not contain an uppercase character")
if has_lower:
    print("[Ok] Contains an lowercase charachter")
else:
    print("[Fail] Does not contain an lowercase character")
if has_special:
    print("[Ok] Contains an special charachter")
else:
    print("[Fail] Does not contain an special character (!@#$%&*?)")
    
#This probably could have been done in an easier way, but it outputs the same as the output example:

#Part 3 --------- Score and rate the password

#Firstly creating a variable which counts True and false ie: Score from 1-6
if not_common: #If common score should be 1
    score = sum([
    has_digit, 
    has_lower, 
    has_special, 
    has_upper, 
    has_special, 
    lenght_ok,
    lenght_12])
else:
    score = 1 #I am guessing that this was the last score point - length over 12 - It is at least what i use in my program

#Printing with correct formating
print(f"Score: {score}/6")

#Giving a rating based on what the password scores:
if not not_common:
    print("Rating: Very week")
elif score >= 5:
    print("Rating: High")
elif score >= 3:
    print("Rating: Medium")
else:
    print("Rating: week") #Might be better to use "fail here", but i was uncertain

#Here i did some testing and found that this rating had to use elif istead of if on the medium score line, as this
#ended up printing both medium and high for the high passwords - Great to get a suggestion to dobbelcheck with diffrent passwords here

#Part 4 -------- Choose a password

#So as i did not use functions this part gets a bit ugly: Either way it is basicly the same code as the previous task
#All indented under a while loop so that everthing runs over and over until the password is accepted or the user presses enter 
#Without inputing anything - I added a without entering anything as i think that could be a mistake some users make

passwords_checked = 0

while True:
    password = input("Please input your choosen password or without inputing anything press Enter to quit: ")

    if password =="":
        break

    passwords_checked += 1

    uppercase = 0
    lower = 0
    digit = 0
    special = 0

    for character in password:
        if character.isupper(): #Checks for uppercase
            uppercase += 1
        if character.islower(): #Checks for lowecase
            lower += 1
        if character.isdigit(): #Checks for digits
            digit += 1
        if character in special_characters: #Checks for special characters
            special += 1
        
    
    not_common = password.lower() not in common_passwords
    lenght_8 = len(password)>=8
    lenght_12 =len(password)>=12
    has_upper = uppercase>=1
    has_lower = lower>=1
    has_digit = digit>=1
    has_special = special>=1
    
    if not_common: #I added this line later as i did not read it correctly the first time - It seams to work
        print("[Ok] Password is not too common")
    else:
        print("[Fail] Password is to common")
    if lenght_ok:
        print("[Ok] Contains at least 8 charachters")
    else:
        print("[FAIL] Does not contain 8 charachters")
    if has_upper:
        print("[Ok] Contains an uppercase charachter")
    else:
        print("[Fail] Does not contain an uppercase character")
    if has_lower:
        print("[Ok] Contains an lowercase charachter")
    else:
        print("[Fail] Does not contain an lowercase character")
    if has_special:
        print("[Ok] Contains an special charachter")
    else:
        print("[Fail] Does not contain an special character (!@#$%&*?)")


    if not_common: 
        score =sum([
        has_digit, 
        has_lower, 
        has_special, 
        has_upper, 
        lenght_12, 
        lenght_ok])
    else:
        score = 0

    print(f"Score: {score}/6")

    if not not_common:
        print("Rating: Very week")
    elif score >= 5:
        print("Rating: High")
    elif score >= 3:
        print("Rating: Medium")
    else:
        print("Rating: Low")

    if score >= 5:
        print(f"\nPassword accepted! Passwords checked: {passwords_checked}") #Just a way of saying the password got accepted and breaking the loop
        break

if password == "": #As if this happens the while loop gets broken i found this to be the best place to print the no password chosen line
    print(f"No password chosen. Passwords checked: {passwords_checked}")
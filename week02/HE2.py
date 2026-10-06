import random

# EX 1
# 1a) = B, B C
# 1b) = false, true
# 1c) = true, false
# 1d) = B, true
# 1e) = false, false, false
# 1f) = false
# 1g) = true, false, true

# Three broken conditions
# 1 mangler to = tegn

# 2 må være score < 101 eller score <= 100. Score > 100 gir scores
# over 100. Må også ha score >= 0 for å få med scores som er 0.
# Rekkefølgen på ulikhetene har ikke noe å si. or må også blir and.

# 3 hvis name er en tom streng, vil man få indexerror.
# Kan sjekke lengden av navnet først i en ytre if, og
# deretter ta en indre if som sjekker name[0]
# ELLER endre rekkefølgen for hva som kommer før og etter "and", siden
# man sjekker først venstre siden for and

# EX 2


def check_password(password):
    longenough = len(password) >= 8
    if not longenough:
        return print("Too short.")

    hasupper = any(char.isupper() for char in password)
    onlyletters = password.isalpha()
    firstdigit = password[0].isdigit()

    print(f"  at least 8 characters:      {longenough}")
    print(f"  has an uppercase letter:    {hasupper}")
    print(f"  not only letters:           {not onlyletters}")
    print(f"  does not start with digit:  {not firstdigit}")

    if firstdigit:
        return print("1Long enough, but it breaks at least one of the other rules.")

    elif onlyletters:
        return print("2 Long enough, but it breaks at least one of the other rules.")

    elif not hasupper:
        return print("3 Long enough, but it breaks at least one of the other rules.")

    return print("Strong password")


check_password("CopyCat1337")
check_password("copycat")
check_password("12345678")
check_password("Bergen!!")
check_password("")


# Exercise 3: Temperature conversion, in either direction
def convert(temperature, start_scale):
    if start_scale.upper().strip() == "C":
        return print(f"{temperature} C in Fahrenheit is: {9 / 5 * temperature + 32}")
    elif start_scale.upper().strip() == "F":
        return print(f"{temperature} F in Celsius is:  {5 / 9 * (temperature - 32)}")


replay = "y"

while replay == "y":
    scale = input("What do you want to convert from? F or C? ")

    while scale.strip().upper() != "F" and scale.strip().upper() != "C":
        scale = input(
            "Selection not valid. What do you want to convert from? Type F or C? "
        )

    temp = input("What temperature do you want to convert? ")
    while not temp.isdigit():
        temp = input(
            "Selection not valid. What temperature do you want to convert? Type a number i.e. 45, 100 or similar. "
        )

    convert(float(temp), scale)
    replay = input("Continue? y/n ")

print("Okay, Bye bye")

# Mangler den siste sanity checken, men orker bare ikke.


# Exercise 4: RNG


print("Halla, dette er en rng. Med kun hele tall, og ikke negative tall.")
low_num = input("Skriv inn positivt nederste tall: ")
high_num = input("Skriv inn positivt øvre tall: ")

if low_num.isdigit() and high_num.isdigit():
    low_num = int(low_num)
    high_num = int(high_num)

    if low_num < 0 or high_num < 0:
        print("Cannot be negative numbers.")
    else:
        if low_num > high_num:
            print("Highest number must be greater than lowest number.")
        else:
            print(f"Random number is: {random.randint(low_num, high_num)}")
else:
    print("must be whole numbers")


# Exercise 5: The prisoners dilemma
okay = True

choiceA = input("Prisoner A: 1 to stay silent, or 2 to confess: ")
if choiceA != "1" and choiceA != "2":
    okay = False
    print("Invalid input for A")

choiceB = input("Prisoner B: 1 to stay silent, or 2 to confess: ")
if choiceB != "1" and choiceB != "2":
    okay = False
    print("Invalid input for B")

choices = {1: "stay silent", 2: "confess"}

if okay:
    print(
        f"A chose to {choices[int(choiceA)]} and B chose to {choices[int(choiceB)]}"
    )  # Dette er litt dårlig måte, men orker ikke noe annet
    if choiceA == "1" and choiceB == "1":
        print("A and B gets 1 year prison")
    elif choiceA == "1" and choiceB == "2":
        print("A gets 3 years, B goes free")
    elif choiceA == "2" and choiceB == "1":
        print("A goes free, B gets 3 years")
    elif choiceA == "2" and choiceB == "2":
        print("Both gets 2 years")

# Ex 6
finished = "n"
while finished == "n":
    year = input("Type a year: ")
    while not year.isdigit() or int(year) < 0:
        year = input("Type a year (non negative numbers only): ")

    year = int(year)

    # leap year hvis det er delelig på 4 og ikke på 100

    # eller leap hvis det er delelig med 400
    is_leap = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

    if is_leap:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

    finished = input("finished? y/n ")

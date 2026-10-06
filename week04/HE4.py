#
# a) None, doesnt return anything

# b) 10, since it returns it right away. 
# return total must be outside the loop

# c) 99, then 10

# d)
# [4,9,0], [4,9,0] # MERK: Lister BLIR påvirket av ting inni en funksjon ig.
# 5, 4

# e) 
# 5
# 2
# 0.5 # siden begge params er navngitt betyr ikke rekkefølge noe
# typeerror, fordi a ikke er satt

#f
# float("12,50") # prediction: valueerror pga , og ikke . : korrekt!
# [1, 2, 3][3] #p: indexerror, pga 3 index ikke finnes    :korrekt
# {"a": 1}["b"] #keyerror                                 :korrekt
# 10 / 0 #zerodivision error                              :korrekt
# "3" + 3 #typeerror                                      :korrekt

#g
# def read_number(text):
#     try:
#         return flooat(text) # her er det en nameerror
#     except ValueError: # men hvis vi setter valueerror som er det vi forventer (at inputen er feil)
#         return None # så ser vi i konsollen at nameerror fortsatt dukker opp, fordi alle andre errors ikke blir handled og dermed kan avbryte!


# print(read_number("42"))

# 1 - meant to report whether a list contains any negative value

"""
def has_negative(values):
    for value in values:
        if value < 0:
            return True
        else:
            return False


print(has_negative([4, 9, -2]))

Her er problemet at den vil returnere false med en gang den møter et positivt tall uten å gå gjennom alt.
Vi kan bare fjerne else greia inni loopen og sette den utenfor
"""
# def has_negative(values):
#     for value in values:
#         if value < 0:
#             return True
#     return False


# print(has_negative([4, 9, -2]))

# 2 - meant to return the average, or 0 for an empty list

"""
def average(values):
    try:
        return sum(values) / len(values)
    except:
        return 0


print(average([4, 9, 2]))
print(average([]))
print(average(["4", "9"]))

Vi mangler å spesifisere hva slags except vi skal catche.
I dette tilfellet er det jo egentlig zerodiverrors vi vil ha tak i, sånn som for den nederste.


"""
# def average(values):
#     try:
#         return sum(values) / len(values)
#     except ZeroDivisionError:
#         return 0


# print(average([4, 9, 2]))
# print(average([]))
# print(average(["4", "9"]))

def eff_interest_rate(r, n=1):
    """
    Params:
    - r = nominal annual rate
    - n = number of times per year the interest is compounded (1 is default)

    Returns:
    - effective annual rate
    """
    R = (1+(r/n))**n - 1
    return round(R,2)

R1 = eff_interest_rate(0.059,4)
R2 = eff_interest_rate(r=0.06,n=2)

print(f"Tilbud A (5.9% kvartalsvis): {R1:.2%}")
print(f"Tilbud B (6% halvårlig):     {R2:.2%}")

if R1 > R2:
    print("Tilbud 1 er best med", R1)
else:
    print("Tilbud 2 er best med", R2)


# EX 3
from random import randint 

def random_character(characters):
    """
    Params:
    - characters: string of characters to pick from

    Returns:
    - random character of the characters
    
    """
    if characters != "":
        return characters[randint(0,len(characters)-1)]
    else:
        return None

def make_code(length):
    """ 
    Params:
    - lenght: int of how long the code shall be

    Returns
    - A random code with numbers as a string
    
    """
    code = ""
    for i in range(length):
        char = random_character("0123456789")
        code += char
    return code

print(make_code(6))
print(make_code(1))
print(make_code(0))
print(random_character("abcdefghijklmnopqrstuvwxyz"))

# Ex4
def line_total(quantity, unit_price):
    return quantity * unit_price

def format_line(item, quantity, unit_price):
    return f"{item:<20}{quantity:>5}{unit_price:>10.2f}{line_total(quantity, unit_price):>12.2f}"

def recipt_totals(quantities, unit_prices):
    total = 0
    for i in range(len(quantities)):
        total += quantities[i]*unit_prices[i]
    return [total, total*0.25, total+total*0.25]

def print_receipt(items, quantities, unit_prices):
    subtotal, vat, total = recipt_totals(quantities, unit_prices)

    print("*"*40)
    for i in range(len(items)):
        print(format_line(items[i], quantities[i], unit_prices[i]))
    print(f"Subtotal: {subtotal:.2f}")
    print(f"VAT (25%): {vat:.2f}")
    print(f"Total: {total:.2f}")
    print("*"*40)

def main():
    items = ["Espresso machine", "Coffee beans", "Oat milk"]
    quantities = [1, 2, 3]
    unit_prices = [4999.00, 149.90, 24.50]
    print_receipt(items, quantities, unit_prices)

main()

# ex5
def get_scale():
    while True:
        text = input("Scale (C or F): ").lower()
        if text == "c":
            return "C"
        elif text == "f":
            return "F"

def get_temperature():
    while True:
        temp = input("Temperature: ")
        try:
            return float(temp)
        except TypeError:
            print("That is not a number. Please try again.")

def convert_temperature(temperature, scale):
    if scale == "C":
        return 9/5*temperature+32
    elif scale == "F":
        return 5/9*(temperature-32)

def main():
    print("""
    *********** Temperature Conversion Program ***********
    This program converts temperatures (Fahrenheit/Celsius)
    ******************************************************

    Enter "F" to convert from Fahrenheit to Celsius
    Enter "C" to convert from Celsius to Fahrenheit
    """)
    scale = get_scale()
    temperature = get_temperature()
    print(convert_temperature(temperature, scale))

main()

# EX 6:
rows = ["12.5", "14.0", "-999", "", "13.2", "n/a", "11.0", "  9.8  ", "-999"]

MISSING_CODE = -999.0

def parse_reading(text):
    """Return the reading as a float, or None if the text isn't a valid number."""
    text = text.strip()
    if text == "":
        return None
    try:
        return float(text)
    except ValueError:
        return None

groups = {"usable": [], "missing": [], "unreadable": []}

for row in rows:
    number = parse_reading(row)
    if number is None:
        groups["unreadable"].append(row)
    elif number == MISSING_CODE:
        groups["missing"].append(row)
    else:
        groups["usable"].append(number)

usable = groups["usable"]
if usable:
    print(f"total of usable readings: {sum(usable):.1f}")
    print(f"average of usable readings: {sum(usable)/len(usable):.1f}")
else:
    print("no usable readings")

print("Antall i de tre gruppene")
print("usable count:", len(groups["usable"]))
print("missing count:", len(groups["missing"]))
print("unreadable count:", len(groups["unreadable"]))
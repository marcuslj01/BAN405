# Halla, la oss gjøre denna

# 1a) = 30
# 1b) = python
# 1c) = [70, 85, 90]
# 1d) = "a", "b", "c", "d"]
# 1e) = ["b", "c"] index error
# 1f) = 7, 8

# EXERCISE 2
booking = "   nhh-2026-oslo-bergen-0087   "

# 1. Display the length of the string as it arrived.
print(len(booking))

# 2. Remove the leading and trailing spaces,
# and store the cleaned string in a variable called reference.
# Display its length as well.
reference = booking.strip()
print(len(reference))

# 3. Using slicing on reference, extract and display the year,
# the origin, the destination and the booking number.
year = reference[4:8]
origin = reference[9:13].upper()
destination = reference[14:20].upper()
booking_number = reference[21:25]

# 4. Display a summary line built with an f-string, in the form:
# Booking 0087: OSLO to BERGEN in 2026
# Note the capitalization — you will need a string method for that.

print(f"Booking {booking_number}: {origin} to {destination} in {year}")

# EXERCISE 3
items = ["Espresso machine", "Coffee beans", "Oat milk"]
quantities = [1, 2, 3]
unit_prices = [4999.00, 149.90, 24.50]

total = 0
for i in range(len(items)):
    total += quantities[i] * unit_prices[i]

# receipt
print("*" * 40)
print(f"{'Item':<20} {'Quantity':<5} {'Price':<5} {'Line total':>10}")
for i in range(len(items)):
    print(
        f"{items[i]:<15} {quantities[i]:<5} {unit_prices[i]:<5.2f} {quantities[i] * unit_prices[i]:>10.2f}"
    )
print(f"\nTotal: {total}")
print(f"VTA: {total * 0.25}")
print("*" * 40)

# Exercise 4
# 1
cities = {
    "london": [18.5, 19, 17.8, 20.1, 21.3],
    "paris": [21, 22.5, 20.2, 23.1, 24],
    "rome": [26.1, 27.3, 25, 26.7, 28.4],
}

# 2
paris_wednesday_temp = cities["paris"][2]
print(paris_wednesday_temp)

# 3
london_avg = round(sum(cities["london"]) / len(cities["london"]), 1)
print("average in london:", london_avg)

paris_avg = round(sum(cities["paris"]) / len(cities["paris"]), 1)
print("paris avg:", paris_avg)

rome_avg = round(sum(cities["rome"]) / len(cities["rome"]), 1)
print("rome avg:", rome_avg)

# 4
warmest = max(cities["london"] + cities["paris"] + cities["rome"])
warmest_city = None

for city, temps in cities.items():
    if warmest in temps:
        warmest_city = city
        break

print(f"The warmest city is {warmest_city} with {warmest} degrees celsius")


# EX 5
def celsius_temp(temperatur):
    return round(5 / 9 * (temperatur - 32), 2)


fahrenheit_temp = input("Halla mann. Skriv inn en temparatur i celsius: ")
print(
    f"fett. Det er det samme som {celsius_temp(float(fahrenheit_temp))} celsiusgrader!"
)

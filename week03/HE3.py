# EX
# 1a) 100,200,300 because the prices list is not being changed.
# 1b) total should be outside the forloop. Therefore it willdisplay 4

# 1c) range(0,3)
# [0,1,2,3]
# 4

# 1d) because which is either F or C, and therefore the whileloop will always run.

# 1e)
# 1,2,5,6

# 1f)
# 1, 4, 9 and then [None*3] because we print it, and therefore do not store the information

# 1g)
# ["a", "", "b"]l, ["a","b"], [""]


# 1 - meant to add up the whole numbers from 1 to 10
total = 0

# for num in range(1, 10):  # Error: 10 will not be included
for num in range(1, 11):  # Corrected version
    total += num

print(total)

# 2 - meant to report whether the list contains a negative number
values = [4, 9, 2, 7]

for value in values:
    if value < 0:
        print("Found a negative number.")
    else:
        print("No negative numbers.")

# This version checks each value and reports for each
# one of them. It does not say whether or not there are
# ANY negative numbers in the list

# Fixed version:# 2 - meant to report whether the list contains a negative number
values = [4, 9, 2, 7]

negative = False
for value in values:
    if value < 0:
        negative = True
    else:
        continue
print(negative)


# EXERCISE 2:
print("Halla, N må være positivt tall: ")
n = int(input("Skriv en N for faen: "))
sum1 = 0
for i in range(n + 1):
    sum1 += i
print(sum1)

sum2 = 0
j = 1
while j <= n:
    sum2 += j
    j += 1

print(sum2)

print(sum(range(n + 1)))

# Exercise 3:
import random

length = ""

while not length.isdigit():
    length = input("type a length in numbers: ")

code = []

for i in range(int(length)):
    code.append(str(random.randint(0, 9)))

print("".join(code))

code2 = [str(random.randint(0, 9)) for i in range(int(length))]
print("".join(code2))

# EX 4
items = ["Espresso machine", "Coffee beans", "Oat milk", "Banan"]
quantities = [1, 2, 3, 4]
unit_prices = [4999.00, 149.90, 24.50, 70000]

subtotal = 0
largest = 0
largest_i = 0

print("*" * 40)
for i in range(len(items)):
    print(
        f"{i + 1:<3}{items[i]:<20}{quantities[i]:<5}{unit_prices[i]:>10.2f}{quantities[i] * unit_prices[i]:>12.2f}"
    )

    if quantities[i] * unit_prices[i] > largest:
        largest = quantities[i] * unit_prices[i]
        largest_i = i
    subtotal += quantities[i] * unit_prices[i]
print("Subtotal: ", subtotal)
print("VAT: ", subtotal * 0.25)
print("*" * 40, "\n")

print("largest item: ", items[largest_i])

# EX 5
# Lett, gjorde dette sist

# EX 6
phonebook = {}

name = "Georg"
while name != "":
    name = input("Name: ")
    if name == "":
        continue
    phonenumber = input("Number: ")

    phonebook[name] = phonenumber

print("***** Phonebook *****")
for i, (key, value) in enumerate(phonebook.items(), start=1):
    print(f"{i}. {key}: {value}")

digits = "halla"
while digits != "":
    digits = input("Search for a number: ")
    if digits == "":
        continue

    results = []

    for key, value in phonebook.items():
        if value.startswith(digits):
            results.append(key)

    print("No results" if len(results) == 0 else results)

# EX 7
text = """The quick brown fox jumps over the lazy dog.
Bergen is the second largest city in Norway, and it rains
there rather a lot. Programming is mostly a matter of
breaking a large problem into smaller problems."""

# 1 Amount of words:
print("Amount of words: ", len(text.split()))

# 2 The longest word
longest = ""
for word in text.split():
    if len(word.strip(",.")) > len(longest):
        longest = word.strip(",.")

print("The longest word is: '", longest, "' with ", len(longest), " characters")

# 3 Average word length to one decimal
total_chars = 0

for word in text.split():
    total_chars += len(word.strip(",."))

average_length = round(total_chars / len(text.split()), 1)

print("Average word length is", average_length)

# 4 Amount of words > 4 letters
four_letter_words = 0

for word in text.split():
    if len(word.strip(",.")) > 4:
        four_letter_words += 1
    else:
        continue

print("Number of more than 4 letter words: ", four_letter_words)

# 5 table for vowels
chars = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

for w in text.split():
    for c in chars:
        if c in w.lower():
            chars[c] += 1


for k, v in chars.items():
    print(k, ":", v)

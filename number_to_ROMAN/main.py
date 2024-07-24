import sys

number = int(sys.argv[1])

roman_numerals = {
    "M": 1000,
    "CM": 900,
    "D": 500,
    "CD": 400,
    "C": 100,
    "IC": 90,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1,
}

roman_number = []

roman_keys = list(roman_numerals.keys())
roman_index = 0
while number > 0:
    current_key = roman_keys[roman_index]
    current_value = roman_numerals[current_key]
    if number >= current_value:
        number -= current_value
        roman_number.append(current_key)
    else:
        roman_index += 1

print("".join(roman_number))

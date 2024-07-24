import sys

number = sys.argv[1]

numbers = {
    "1": [" ", "|", "|"],
    "2": [" _ ", " _|", "|_ "],
    "3": [" _ ", " _|", " _|"],
    "4": ["   ", "|_|", "  |"],
    "5": [" _ ", "|_ ", " _|"],
    "6": [" _ ", "|_ ", "|_|"],
    "7": [" _ ", "  |", "  |"],
    "8": [" _ ", "|_|", "|_|"],
    "9": [" _ ", "|_|", " _|"],
    "0": [" _ ", "| |", "|_|"],
}


top = [numbers[n][0] for n in number]
middle = [numbers[n][1] for n in number]
bottom = [numbers[n][2] for n in number]


print("".join(top))
print("".join(middle))
print("".join(bottom))

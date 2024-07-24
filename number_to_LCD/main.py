import sys

number = sys.argv[1]
width = int(sys.argv[2])
height = int(sys.argv[3])

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


top = []
h_exp_h = []
middle = []
h_exp_l = []
bottom = []


def expand_LCD_w(lcd, w):
    if len(lcd) < 3:
        return lcd
    return lcd[0] + lcd[1] * width + lcd[-1]


def expand_LCD_h(lcd):
    if len(lcd) < 3:
        return lcd
    return lcd[0] + " " + lcd[-1]


for n in number:
    top.append(expand_LCD_w(numbers[n][0], width))
    h_exp_h.append(expand_LCD_w(expand_LCD_h(numbers[n][1]), width))
    middle.append(expand_LCD_w(numbers[n][1], width))
    h_exp_l.append(expand_LCD_w(expand_LCD_h(numbers[n][2]), width))
    bottom.append(expand_LCD_w(numbers[n][2], width))


print("".join(top))
for i in range(1, height):
    print("".join(h_exp_h))
print("".join(middle))
for i in range(1, height):
    print("".join(h_exp_l))
print("".join(bottom))

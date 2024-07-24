from getpass import getpass

word = ""
while len(word) != 5:
    word = getpass(prompt="Set word (5 chars): ")
    if len(word) != 5:
        print("The word needs to contain exactly 5 chars")

word = word.upper()
print(word)

attempts = 0

guess = ""
while word != guess:
    guess = input("Introduce guess: ")
    if len(guess) != 5:
        print("Guess needs to be exactly 5 chars long.")
        continue
    guess = guess.upper()


print("You guessed it!!")

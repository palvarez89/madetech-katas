from getpass import getpass

word = ""
while len(word) != 5:
    word = getpass(prompt="Set word (5 chars): ")
    if len(word) != 5:
        print("The word needs to contain exactly 5 chars")

word = word.upper()

attempts = 0

guess = ""
while word != guess:
    guess = input("Introduce guess: ")
    if len(guess) != 5:
        print("Guess needs to be exactly 5 chars long.")
        continue
    guess = guess.upper()
    attempts += 1
    if word != guess:
        score = ""
        for i, s in enumerate(guess):
            if list(word)[i] == s:
                score = score + "2"
            elif s in word:
                score = score + "1"
            else:
                score = score + "0"
        print(f"                 {score}")


print(f"You guessed it after {attempts} attempt(s)")

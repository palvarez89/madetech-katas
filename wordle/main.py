from getpass import getpass


def set_target():
    target = ""
    while len(target) != 5:
        target = getpass(prompt="Set word (5 chars): ")
        if len(target) != 5:
            print("The word needs to contain exactly 5 chars")
    return target


def calculate_score(target, guess):

    internal_score = {}
    score = ""
    for i, s in enumerate(guess):
        current_score = internal_score.get(s, {})
        if not current_score:
            current_score = {"pos_failed": [], "pos_correct": []}

        if list(target)[i] == s:
            score = score + "2"
            current_score["pos_correct"].append(i)
        elif s in target:
            score = score + "1"
            current_score["pos_failed"].append(i)
        else:
            score = score + "0"
        internal_score[s] = current_score
        print(internal_score)
    return score


def main():
    word = set_target()
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
            score = calculate_score(word, guess)
            print(f"                 {score}")

    print(f"You guessed it after {attempts} attempt(s)")


if __name__ == "__main__":
    main()

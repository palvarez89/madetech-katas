from getpass import getpass

word = ""
while len(word) != 5:
    word = getpass(prompt="Set word (5 chars): ")
    if len(word) != 5:
        print("The word needs to contain exactly 5 chars")

word = word.upper()
print(word)

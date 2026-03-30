import random

words = ["python", "code", "table", "array", "loop"]
word = random.choice(words)

hidden = []
i = 0

# créer le mot caché
while i < len(word):
    hidden.append("_")
    i = i + 1

tries = 6

while tries > 0 and "_" in hidden:
    print("\nWord:", " ".join(hidden))
    print("Tries left:", tries)

    letter = input("Enter a letter: ")

    if letter in word:
        i = 0
        while i < len(word):
            if word[i] == letter:
                hidden[i] = letter
            i = i + 1
    else:
        print("Wrong letter")
        tries = tries - 1

if "_" not in hidden:
    print("\nYou won!")
else:
    print("\nYou lost!")

print("The word was:", word)
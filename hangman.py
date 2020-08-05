


guess_counter = 0
max_guesses = 5

word = input("What word would you like to guess?")
hidden_word = ""

for i in word:
    hidden_word = hidden_word + "_"


print("\n\n\n\n\n\n\n\n\n\n\n\n\nThis is your hidden word: ")
print(hidden_word)


while guess_counter < max_guesses:
    guess = input("What is your guess?")
    index=0
    x=0
    for index in word:
        if guess == word[x]:
            print("yes!")
        else:
            print("nope!")
        x += 1


    guess_counter += 1

print(hidden_word)

print("this is an update")


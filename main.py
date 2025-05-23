import random
import hangman_art
import hangman_words

word_list = hangman_words.word_list
lives = 6

logo = hangman_art.logo
print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for letter in chosen_word:
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
wrong_letters = []

while not game_over:
    print(
        f"**************************** {lives}/6 LIVES LEFT ****************************"
    )
    guess = input("Guess a letter: ").lower()

    # letting the user know that they have entered a letter they've already guessed
    if guess in correct_letters or guess in wrong_letters:
        print(f"You have already guessed letter '{guess}'")
        continue

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # letting the user know that the letter is not in the chosen_word

    if guess not in chosen_word:
        wrong_letters.append(guess)
        lives -= 1
        print(f"You guessed letter '{guess}', that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True

            print("*********************** YOU LOSE **********************")
            print(f"The correct word was: {chosen_word}")

    if "_" not in display:
        game_over = True
        print("**************************** YOU WIN!!! ****************************")

    stages = hangman_art.stages
    print(stages[lives])

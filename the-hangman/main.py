import random
from hangman_words import word_list
from hangman_art import stages, logo


def main():

    end_game = False
    chosen_word = random.choice(word_list)
    lives = 6

    display = ['_' for i in chosen_word]
    print(display)
    print(stages[lives])

    letters = set()
    
    while not end_game:

        guess = input("Guess a letter: ").lower()

        if guess in display or guess in letters:
            print(f'\nYou already guessed {guess}\n')
            continue

        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        if guess not in chosen_word:
            print(f"You guessed the letter {guess} that's not in the word. You lose a life \n")
            print(display)
            
            lives-=1
            if lives == 0:
                end_game = True
                print(stages[livesi])
                print("\nYou lose!!!\n")
                break
            
            print(f"\nRemaining lifes {lives} \n")

        if '_' not in display:
            end_game = True
            print(f"\nThe word was: {chosen_word} \nYou win!!!\n")
            
            break

        print(display)
        print(stages[lives])
        letters.add(guess)

    return 

if __name__ == '__main__':
    print(logo)
    main()

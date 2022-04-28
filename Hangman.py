import random

print('H A N G M A N')
list_of_words = ['python', 'java', 'swift', 'javascript']
a = 0
b = 8
alphabet = {'e', 'p', 'n', 'u', 'h', 'g', 'f', 'y', 'a', 'w', 'm', 'b', 'x', 'c', 'o', 'r', 's', 'd', 'i', 'l', 't',
            'j', 'k', 'z', 'q', 'v'}
entered_letters = set()
lost_count = 0
won_count = 0
loop = True

while loop:
    chosen_word = random.choice(list_of_words)

    word_hint = list('-' * len(chosen_word))  # word_hint it is what a player sees: -----
    decision = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
    if decision == 'play':
        while a < b:
            print()
            print(''.join(word_hint))   # word_hint (list to string type):
            # when a player won:
            if ''.join(word_hint) == chosen_word:
                print(f'You guessed the word {chosen_word}!')
                print('You survived!')
                won_count += 1
                entered_letters.clear()
                a = 0
                break
            letter = input(f'Input a letter: ')

            if len(letter) != 1:
                print('Please, input a single letter.')
                continue

            if letter not in alphabet:
                print('Please, enter a lowercase letter from the English alphabet.')
                continue

            if letter not in entered_letters:
                entered_letters.add(letter)
            else:
                print("You've already guessed this letter.")
                continue

            if letter not in chosen_word:
                print("That letter doesn't appear in the word.")
                a += 1
                # when 8 attempts are over:
                if a == b:
                    print()
                    print('You lost!')
                    lost_count += 1
                    a = 0
                    entered_letters.clear()
                    break
            # when a player guessed correct letter:
            else:
                for i in range(0, len(chosen_word)):
                    if letter == chosen_word[i]:
                        word_hint[i] = letter

    elif decision == 'results':
        print(f'You won: {won_count} times.')
        print(f'You lost: {lost_count} times.')

    elif decision == 'exit':
        loop = False

import random
print('H A N G M A N')

menu = ''

while menu != 'play' or menu != 'exit':
    menu = input('Type "play" to play the game, "exit" to quit: ')
    if menu == 'play':

        words = ['python', 'java', 'kotlin', 'javascript']
        chosen_word = random.choice(words)
        #print(chosen_word)
        listed = []
        for i in range(len(chosen_word)):
            listed.append('-')
        shown_word = ''.join(listed)
        guess_list = []

        chance = 8

        while chance > 0:
            print()
            print(shown_word)
            guess_letter = input('Input a letter:')
            
            if len(guess_letter) > 1:
                print('You should input a single letter')
            elif guess_letter.islower() is False:
                print('It is not an ASCII lowercase letter')
            elif guess_letter in guess_list:
                print('You already typed this letter')
            else:
                if guess_letter in chosen_word:
                    for x in range(len(chosen_word)):
                        if guess_letter == chosen_word[x]:
                            listed[x] = guess_letter
                            shown_word = ''.join(listed)

                elif guess_letter not in guess_list:
                    chance -= 1
                    if chance == 0:
                        break
                    else:
                        if guess_letter not in shown_word:
                            print('No such letter in the word')

            guess_list.append(guess_letter)

            if shown_word == chosen_word:
                break

        if shown_word == chosen_word:
            print('You guesssed the word ' + shown_word+'!\nYou survived!')
        elif guess_letter in shown_word:
            print('No improvements\nYou are hanged!')
        else:
            print('No such letter in the word\nYou are hanged!')

        menu = ''
    else:
        break
import random

playing = True


def print_board(num):
    match num:
        case 6:
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('\n'*3)
        case 5:
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('_____o_____')
            print('\n'*3)
        case 4:
            print('     __________')
            print('     |        |')
            print('     |')
            print('     |')
            print('     |')
            print('     |')
            print('     |')
            print('     |')
            print('_____o_____')
            print('\n'*3)
        case 3:
            print('     __________')
            print('     |        |')
            print('     |        O')
            print('     |        ')
            print('     |        ')
            print('     |        ')
            print('     |        ')
            print('     |      ')
            print('_____o_____')
            print('\n'*3)
        case 2:
            print('     __________')
            print('     |        |')
            print('     |        O')
            print('     |        |')
            print('     |        |')
            print('     |        |')
            print('     |        ')
            print('     |      ')
            print('_____o_____')
            print('\n'*3)
        case 1:
            print('     __________')
            print('     |        |')
            print('     |        O')
            print('     |      --|--')
            print('     |        |')
            print('     |        |')
            print('     | ')
            print('     | ')
            print('_____o_____')
            print('\n'*3)
        case 0:
            print('     __________')
            print('     |        |')
            print('     |        O')
            print('     |      --|--')
            print('     |        |')
            print('     |        |')
            print('     |        /\\')
            print('     |       /  \\')
            print('_____o_____')
            print('\n'*3)


def randomWord():
    wordSet = ['championship', 'toothworker', 'politics', 'orange', 'speech', 'series', 'secretary', 'community', 'stranger', 'system', 'grandmother', 'country', 'effort', 'writing', 'oven', 'sympathy', 'appointment', 'quality', 'road', 'control', 'idea', 'diamond', 'buyer',
               'reputation', 'artisan', 'emotion', 'policy', 'sister', 'information', 'setting', 'menu', 'entry', 'delivery', 'supermarket', 'republic', 'patience', 'technology', 'sector', 'weakness', 'math', 'volume', 'agreement', 'funeral', 'meaning', 'perspective', 'player', 'conversation', 'anxiety']
    num = random.randint(1, 48)
    return wordSet[num]


def wordBlank(word):
    return ['_']*len(word)


def player_input():
    letter = ''
    # Add a function to detect if that number is already taken
    while not (letter.isalpha() and len(letter) == 1):
        letter = (input('Please enter the letter you want to check ')).lower()

    return letter


def valid(letter, word):
    valid = False
    for i in word:
        if letter == i:
            valid = True
            break
    return valid


def displayLetter(word, letterArr):
    result = wordBlank(word)
    wordList = list(word)
    for i in word:
        for j in letterArr:
            if j in i:
                for k in range(word.count(i)):
                    result[
                        [k for k, n in enumerate(wordList) if n == j][k]] = j  # This comprehesive list give the index location so the result can correctly replace with j
    print(result)


def winCon(wordSet, letterSet):
    return set(wordSet) == set(letterSet)


# THE GAME
while True:
    # Number of life starting the game
    life = 6
    # Print an opening statement
    print('Let play some Hangman!')

    word = randomWord()
    print(wordBlank(word))
    slot = []

    while playing:
        while life > 0:
            keyword = player_input()
            if valid(keyword, word):
                slot.append(keyword)
                print('----------------------------')
                print('lol XD')
                print_board(life)
                print('----------------------------')
                displayLetter(word, slot)
            else:
                life -= 1
                print_board(life)

            if winCon(word, slot):
                print('You guessed correctly and survived the Hangman')
                playing = False
                break
        else:
            print(f'The word is {word}')
            print("Game Over")
            break

    new_game = input(
        "Enter 'y' to play again ")

    if new_game[0].lower() == 'y':
        playing = True
        continue

    else:
        print("The End")
        break

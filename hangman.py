
words_list = ['hello','night','dream','test']

print('-'*40)
print('-'*40)
print("WELCOME TO HANGMAN....let's play!")
print('-'*40)
print('-'*40)
      
def pickword(words_list):
    x = np.random.randint(0,len(words_list))
    return(words_list[x])
    

def setup_game_lists(game_word):
    game_info = dict()
    game_info['correct_letters'] = set(game_word)
    game_info['incorrect_guesses'] = set()
    game_info['correct_guesses'] = set()
    game_info['incorrect_guesses_no'] = 0 #set counter for wrong answers
    game_info['game_word'] = game_word
    game_info['won'] = False
    
    return(game_info)

setup_game_lists('test')

def wrong_guess(game_info,guess):
    game_info['incorrect_guesses'].add(guess) # increment incorrect guesses letters
    game_info['incorrect_guesses_no'] += 1 # increment incorrect guesses number
    
    return(game_info)

def correct_guess(game_info,guess):
    print('Correct guess!')
    game_info['correct_guesses'].add(guess)
    game_info['won'] = (game_info['correct_guesses'] == game_info['correct_letters'])
    return()

def print_status(game_info):
    print('-' * 40)
    print('Guesses remaining: ', 9 - game_info['incorrect_guesses_no'], '')
    test = ''
    for j in game_info['incorrect_guesses']:
        test += j + ', '
    print('Incorrect guesses: ', test)
    word = ' '
    for i in game_info['game_word']:
        if i in game_info['correct_guesses']:
            word = word + i + ' '
        else:
            word = word + '_ '
    print(word)
    return



import numpy as np
game_word = pickword(words_list) ##get a word
game_info = setup_game_lists(game_word) # make game variables
print_status(game_info)

while (game_info['incorrect_guesses_no'] < 9 and game_info['won'] == False):
    guess = input('Enter a guess here: ')
    if guess in game_info['correct_letters']:
        correct_guess(game_info,guess)
        print_status(game_info)
    else:
        wrong_guess(game_info,guess)
        print_status(game_info)

print('-' * 40)
print('-' * 40)

if game_info['incorrect_guesses_no'] < 9:
    print('Well done, you have won!')
else:
    print(':-(')
        
print('-' * 40)
print('-' * 40)



''' Python 3.9
22.10.2020

Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays
(using input), compare them, print out a message of congratulations
to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock'''

print('''Please pick one:
            * rock
            * scissors
            * paper''')

while True:
    game_dict = {'rock': 1, 'scissors': 2, 'paper': 3}
    player_a = str(input("Player a: "))
    player_b = str(input("Player b: "))
    a = game_dict.get(player_a)
    b = game_dict.get(player_b)
    dif = a - b

    if dif in [-1, 2]:
        print('player a wins.')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    elif dif in [-2, 1]:
        print('player b wins.')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    else:
        print('Draw.Please continue.')

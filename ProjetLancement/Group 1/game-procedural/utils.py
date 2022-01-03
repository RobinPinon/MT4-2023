def turn_print(player_score_list,turn,player):
    print('\nturn #' + str(turn) + '--> ' + str(player['name']) + ' rank # ' + str(player_score_list.index(player['score']) + 1) + ', ' + 'score ' + str(player['score']) + ' \n')

def roll_print(roll, total_winning_dice, player_winning_list, player_roll_score, player_turn_score, dice_to_roll):
    print("roll # {} : {} scoring dices {} scoring {}, potential turns score {}, remaining dice to roll : {}"
    .format(roll, total_winning_dice,player_winning_list,player_roll_score, player_turn_score, dice_to_roll))

def player_score_print(player):
    print("{} --> {}".format(player['name'], player['score']))
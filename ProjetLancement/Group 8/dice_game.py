import random

NB_DICE_TOROLL = 5
NB_DICE_SIDE = 6  # Nb of side of the Dices
SCORING_DICE_VALUE_LIST = [1, 5]  # List of the side values of the dice who trigger a standard score
SCORING_MULTIPLIER_LIST = [100, 50]  # List of multiplier for standard score

THRESHOLD_BONUS = 3  # Threshold of the triggering for bonus in term of occurrence of the same slide value
STD_BONUS_MULTIPLIER = 100  # Standard multiplier for bonus
ACE_BONUS_MULTIPLIER = 1000  # Special multiplier for aces bonus

WIN_NUMBER = 2000


# return a list of dices value occurrence for a roll of nb_dice_to_roll dices
def roll_dice_set(nb_dice_to_roll):
    dice_value_occurrence_list = [0] * NB_DICE_SIDE
    for n in range(nb_dice_to_roll):
        dice_value = random.randint(1, NB_DICE_SIDE)
        dice_value_occurrence_list[dice_value - 1] += 1

    return dice_value_occurrence_list

def analyse_bonus_score(dice_value_occurrence_list):
    score = 0
    for side_value_index, dice_value_occurrence in enumerate(dice_value_occurrence_list):
        nb_of_bonus = dice_value_occurrence // THRESHOLD_BONUS
        if nb_of_bonus > 0:
            if side_value_index == 0:
                bonus_multiplier = ACE_BONUS_MULTIPLIER
            else:
                bonus_multiplier = STD_BONUS_MULTIPLIER
            score += nb_of_bonus * bonus_multiplier * (side_value_index + 1)
            dice_value_occurrence_list[side_value_index] %= THRESHOLD_BONUS

    return score, dice_value_occurrence_list


def analyse_standard_score(dice_value_occurrence_list):
    score = 0
    for scoring_value, scoring_multiplier in zip(SCORING_DICE_VALUE_LIST, SCORING_MULTIPLIER_LIST):
        score += dice_value_occurrence_list[scoring_value - 1] * scoring_multiplier
        dice_value_occurrence_list[scoring_value - 1] = 0

    return score, dice_value_occurrence_list


def analyse_score(dice_value_occurrence_list):
    bonus_score, dice_value_occurrence_list = analyse_bonus_score(dice_value_occurrence_list)
    standard_score, dice_value_occurrence_list = analyse_standard_score(dice_value_occurrence_list)

    return bonus_score + standard_score


def diceleft(dice_value_occurrence_list):
    for n in range (len(dice_value_occurrence_list)):
        for i in range (len(SCORING_DICE_VALUE_LIST)):
           if (dice_value_occurrence_list[n]==SCORING_DICE_VALUE_LIST[i]-1) :
               dice_value_occurrence_list[n] = 0
           if (dice_value_occurrence_list[n]==THRESHOLD_BONUS) :
               dice_value_occurrence_list[n] = 0
    dice_left = sum(dice_value_occurrence_list)
    return dice_left


totallyrandomlist= [3,3,2,3,3,3]
print(diceleft(totallyrandomlist))


def rank_check(list_score, list_rank):
    for i in range(len(list_score)):
        max_rank = len(list_score)
        for n in range(len(list_score)):
            if(list_score[i]>list_score[n]):
                max_rank -= 1
        list_rank[i]= max_rank
    return list_rank


def game_end(list_score):
    for i in range(len(list_score)):
        if(WIN_NUMBER<=list_score[i]):
            return False
    return True

def game_turn(player, score, turn, rank):
    nb_roll = 1
    new_score = score
    player_bool = 0
    dice_left = NB_DICE_TOROLL
    print("Turn #" + str(turn) + "--> " + str(player) + "rank #" + str(rank) + ", score " + str(new_score))
    while ((player_bool == 0)):
        print("Roll#" + str(nb_roll))
        nb_roll += 1
        list_occurence = roll_dice_set(dice_left)
        new_score += analyse_score(list_occurence)
        dice_left = diceleft(list_occurence)
        print("You achieved this score:" + str(new_score) + " You have " + str(dice_left) + " dice to Roll (If you have 0 left, you can roll all the dice)")
        if(nb_roll <= 3):
            player_bool = int(input("Continue to roll?[0/1]"))
        else:
            player_bool = 1
        if((dice_left == 0) and (player_bool == 0)):
            dice_left = NB_DICE_TOROLL
            new_score = score
    return (new_score)


def main_game():
    number_of_player = int(input("Number of players : "))
    list_player = []
    list_score = []
    list_rank = []
    turn = 1
    for i in range(number_of_player):
        player_name = input("Player " + str(i+1) + " : ")
        list_player.append(player_name)
        list_score.append(0)
        list_rank.append(i+1)
    while game_end(list_score):
        print(len(list_player))
        for n in range (len(list_player)):
            print(list_player[n] + " it is your turn")
            list_score[n] = game_turn(list_player[n],list_score[n],turn,list_rank[n])
        list_rank = rank_check(list_score, list_rank)
        turn += 1


main_game()

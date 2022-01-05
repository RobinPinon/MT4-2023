import random
from constant import *

# return a list of dices value occurrence for a roll of nb_dice_to_roll dices
def roll_dice_set(nb_dice_to_roll, player):
    dice_value_occurrence_list = [0] * NB_DICE_SIDE
    for n in range(nb_dice_to_roll):
        dice_value = random.randint(1, NB_DICE_SIDE)
        dice_value_occurrence_list[dice_value - 1] += 1
        player._stats._increment_dice_values(dice_value)
    return dice_value_occurrence_list


def analyse_bonus_score(dice_value_occurrence_list, player):
    score = 0
    for side_value_index, dice_value_occurrence in enumerate(dice_value_occurrence_list):
        nb_of_bonus = dice_value_occurrence // THRESHOLD_BONUS
        if nb_of_bonus > 0:
            if side_value_index == 0:
                bonus_multiplier = ACE_BONUS_MULTIPLIER
            else:
                bonus_multiplier = STD_BONUS_MULTIPLIER
            bonus_value = nb_of_bonus * bonus_multiplier * (side_value_index + 1)
            score += bonus_value
            dice_value_occurrence_list[side_value_index] %= THRESHOLD_BONUS
            player._stats._set_highest_bonus(bonus_value)
            player._stats._increment_bonus()

    return score, dice_value_occurrence_list


def analyse_standard_score(dice_value_occurrence_list, player):
    score = 0
    for scoring_value, scoring_multiplier in zip(SCORING_DICE_VALUE_LIST, SCORING_MULTIPLIER_LIST):
        score += dice_value_occurrence_list[scoring_value - 1] * scoring_multiplier
        dice_value_occurrence_list[scoring_value - 1] = 0

    return score, dice_value_occurrence_list


def analyse_score(dice_value_occurrence_list, player):
    bonus_score, dice_value_occurrence_list = analyse_bonus_score(dice_value_occurrence_list, player)
    standard_score, dice_value_occurrence_list = analyse_standard_score(dice_value_occurrence_list, player)

    return { 'score': bonus_score + standard_score, 'occurrences': dice_value_occurrence_list }

def separate_text():
    print('------------------------------------')
    print()

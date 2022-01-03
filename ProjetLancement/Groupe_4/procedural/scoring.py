import random

NB_DICE_SIDE = 6  # Nb of side of the Dices
SCORING_DICE_VALUE_LIST = [1, 5]  # List of the side values of the dice who trigger a standard score
SCORING_MULTIPLIER_LIST = [100, 50]  # List of multiplier for standard score

THRESHOLD_BONUS = 3  # Threshold of the triggering for bonus in term of occurrence of the same slide value
STD_BONUS_MULTIPLIER = 100  # Standard multiplier for bonus
ACE_BONUS_MULTIPLIER = 1000  # Special multiplier for aces bonus


# return a list of dices value occurrence for a roll of nb_dice_to_roll dices
def roll_dice_set(nb_dice_to_roll):
    dice_value_occurrence_list = [0] * NB_DICE_SIDE
    for n in range(nb_dice_to_roll):
        dice_value = random.randint(1, NB_DICE_SIDE)
        dice_value_occurrence_list[dice_value - 1] += 1

    return dice_value_occurrence_list


def analyse_bonus_score(dice_value_occurrence_list):
    scoring_dices = []
    total_bonus = 0
    score = 0

    for side_value_index, dice_value_occurrence in enumerate(dice_value_occurrence_list):
        nb_of_bonus = dice_value_occurrence // THRESHOLD_BONUS
        if nb_of_bonus > 0:
            if side_value_index == 0:
                bonus_multiplier = ACE_BONUS_MULTIPLIER
            else:
                bonus_multiplier = STD_BONUS_MULTIPLIER

            score += nb_of_bonus * bonus_multiplier * (side_value_index + 1)
            total_bonus += nb_of_bonus

            # Stores dices left to play not used in bonus
            dices_left = dice_value_occurrence % THRESHOLD_BONUS
            dice_value_occurrence_list[side_value_index] = dices_left

            # Store scoring dices
            nb_scoring_dices = dice_value_occurrence - dices_left
            scoring_dices.append([side_value_index + 1, nb_scoring_dices])

    return score, dice_value_occurrence_list, scoring_dices, total_bonus


def analyse_standard_score(dice_value_occurrence_list):
    score = 0
    scoring_dices = []

    for scoring_value, scoring_multiplier in zip(SCORING_DICE_VALUE_LIST, SCORING_MULTIPLIER_LIST):
        score += dice_value_occurrence_list[scoring_value - 1] * scoring_multiplier

        if dice_value_occurrence_list[scoring_value - 1] != 0:
            scoring_dices.append([scoring_value, dice_value_occurrence_list[scoring_value - 1]])
            dice_value_occurrence_list[scoring_value - 1] = 0

    return score, dice_value_occurrence_list, scoring_dices


def analyse_score(dice_value_occurrence_list, player):
    bonus_score, dice_value_occurrence_list, bonus_scoring_dices, bonus_count = analyse_bonus_score(dice_value_occurrence_list)
    standard_score, dice_value_occurrence_list, standard_scoring_dices = analyse_standard_score(dice_value_occurrence_list)

    scoring_dices = bonus_scoring_dices
    scoring_dices += standard_scoring_dices

    return bonus_score + standard_score, dice_value_occurrence_list, scoring_dices, bonus_count


def game_stats():
    return {
        'max_turn_score': {
            'score': 0,
            'player': ''
        },
        'max_turn_loss': {
            'score': 0,
            'player': ''
        },
        'total_no_points_turn': 0,
        'longest_turn': {
            'count': 0,
            'player': ''
        },
        'mean_scoring_turn': 0,
        'mean_non_scoring_turn': 0
    }


def compute_game_stats(players, stats, total_turns_game):
    total_score_game = 0
    total_rolls_game = 0
    total_lost_points = 0

    for id in players:
        total_score_game += players[id]['score']
        total_rolls_game += players[id]['rolls']
        total_lost_points += players[id]['lost_points']

    stats['mean_scoring_turn'] = round((total_score_game / len(players) / total_turns_game), 2)
    stats['mean_non_scoring_turn'] = round((total_lost_points / stats['total_no_points_turn']), 2) if stats['total_no_points_turn'] else 0

    return stats


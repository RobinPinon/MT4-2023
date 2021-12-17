from back.constant import (
    THRESHOLD_BONUS,
    ACE_BONUS_MULTIPLIER,
    STD_BONUS_MULTIPLIER,
    SCORING_DICE_VALUE_LIST,
    SCORING_MULTIPLIER_LIST,
    DEFAULT_TARGET_SCORE)

# xxxxxx
# -------- PARAMETERS --------
# dice_value_occurrence_list : TYPE =  | xxxxxx


def analyse_bonus_score(dice_value_occurrence_list):
    bonus = {
        "full_roll": 0,
        "standard": 0
    }
    score = 0
    for side_value_index, dice_value_occurrence in enumerate(
        dice_value_occurrence_list
    ):
        nb_of_bonus = dice_value_occurrence // THRESHOLD_BONUS
        if nb_of_bonus > 0:

            if side_value_index == 0:
                bonus_multiplier = ACE_BONUS_MULTIPLIER
                bonus["full_roll"] += 1
            else:
                bonus_multiplier = STD_BONUS_MULTIPLIER
                bonus["standard"] += 1
            score += nb_of_bonus * bonus_multiplier * (side_value_index + 1)
            dice_value_occurrence_list[side_value_index] %= THRESHOLD_BONUS

    return score, dice_value_occurrence_list, bonus


# xxxxxx
# -------- PARAMETERS --------
# dice_value_occurrence_list : TYPE =  | xxxxxx

def analyse_standard_score(dice_value_occurrence_list):
    score = 0
    for scoring_value, scoring_multiplier in zip(
        SCORING_DICE_VALUE_LIST, SCORING_MULTIPLIER_LIST
    ):
        score += (
            dice_value_occurrence_list[scoring_value - 1] * scoring_multiplier
        )

        dice_value_occurrence_list[scoring_value - 1] = 0

    return score, dice_value_occurrence_list


# xxxxxx
# -------- PARAMETERS --------
# dice_value_occurrence_list : TYPE =  | xxxxxx

def analyse_score(dice_value_occurrence_list):
    bonus_score, dice_value_occurrence_list,bonus = analyse_bonus_score(
        dice_value_occurrence_list
    )

    standard_score, dice_value_occurrence_list = analyse_standard_score(
        dice_value_occurrence_list
    )
    return bonus_score + standard_score, dice_value_occurrence_list, bonus


# Check if any player reached DEFAULT_TARGET_SCORE
# -------- PARAMETERS --------
# players : TYPE = array of dict| array of players
def analyse_score_winner(players):
    for player in players:
        return True if player["score"] > DEFAULT_TARGET_SCORE else False




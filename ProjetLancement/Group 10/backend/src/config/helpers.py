import random
import re

from .constants import (
    NB_DICE_SIDE,
    TRIGGER_OCCURRENCE_FOR_BONUS,
    BONUS_VALUE_FOR_ACE_BONUS,
    BONUS_VALUE_FOR_NORMAL_BONUS,
    LIST_SCORING_DICE_VALUE,
    LIST_SCORING_MULTIPLIER,
    DEFAULT_DICES_NB
)


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
        nb_of_bonus = dice_value_occurrence // TRIGGER_OCCURRENCE_FOR_BONUS
        if nb_of_bonus > 0:
            if side_value_index == 0:
                bonus_multiplier = BONUS_VALUE_FOR_ACE_BONUS
            else:
                bonus_multiplier = BONUS_VALUE_FOR_NORMAL_BONUS
            score += nb_of_bonus * bonus_multiplier * (side_value_index + 1)
            dice_value_occurrence_list[side_value_index] %= TRIGGER_OCCURRENCE_FOR_BONUS

    return score, dice_value_occurrence_list


def analyse_standard_score(dice_value_occurrence_list):
    score = 0
    for scoring_value, scoring_multiplier in zip(LIST_SCORING_DICE_VALUE, LIST_SCORING_MULTIPLIER):
        score += dice_value_occurrence_list[scoring_value - 1] * scoring_multiplier
        dice_value_occurrence_list[scoring_value - 1] = 0

    return score, dice_value_occurrence_list


def analyse_score(dice_value_occurrence_list):
    bonus_score, dice_value_occurrence_list = analyse_bonus_score(dice_value_occurrence_list)
    standard_score, dice_value_occurrence_list = analyse_standard_score(dice_value_occurrence_list)

    return bonus_score, (bonus_score + standard_score), dice_value_occurrence_list


def initialize_players_datas(number_of_players: int):
    players = []

    for player in range(number_of_players):
        name = str(input(f"Nom du joueur {player + 1}: "))
        players.append({
            "name": name,
            "score": 0,
            "total_score": 0,
            "rolls": 0,
            "remaining_dices": DEFAULT_DICES_NB,
            "potential_score": 0,
            "scores": [],  # used for mean
            "longest_rolls": 0,
            "bonus": 0,
            "max_turn_scoring": 0,
            "longest_roll": 0,
        })
    return players


def continue_game():
    answer = str(input("continuer ? y/n: "))
    return re.match("y|yes", answer, re.I)


def player_can_continue_playing(remaining_dices: int, score: int) -> bool:
    if score and remaining_dices:
        if continue_game():
            return True
    elif score and not remaining_dices:
        return True
    else:
        return False


def increment_player_data(player, current_score_with_bonus, dice_roll_set, current_bonus, current_max_score):
    player["rolls"] += 1
    player["longest_roll"] += 1
    player["remaining_dices"] = sum(dice_roll_set)
    player["potential_score"] += current_score_with_bonus
    player["total_score"] += current_score_with_bonus

    if current_bonus:
        player["bonus"] += 1

    if current_score_with_bonus == 0:
        player["score"] = 0
        player["longest_roll"] = 0
        # player["total_score"] = 0
    else:
        player["score"] = player["potential_score"]
        if player["total_score"] > current_max_score:
            current_max_score += player["score"]

        if player["score"] > player["max_turn_scoring"]:
            player["max_turn_scoring"] = player["score"]

    return player, current_score_with_bonus, dice_roll_set, current_bonus, current_max_score


def display_turn_recap(players):
    print('Total : ' + ', '.join([f"{player['name']} --> {player['total_score']}" for player in players]))


def sort_players_by_key(players, key: str):
    return sorted(players, key=lambda p: p[key])[0]

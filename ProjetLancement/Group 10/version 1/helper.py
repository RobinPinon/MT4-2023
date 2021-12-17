import random
import re

from constants import *

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


def initialize_players_and_datas(number_of_players: int):
    players_name = []

    for player in range(number_of_players):
        player_name = str(input(f"Nom du joueur {player + 1}: \n"))
        players_name.append(player_name)

    players_roll = [0] * number_of_players
    players_score = [0] * number_of_players
    players_score_tmp = [0] * number_of_players
    players_remaining_dices = [5] * number_of_players
    players_potential_score = [0] * number_of_players
    players_results = [""] * number_of_players
    bonus = [0] * number_of_players
    total_potential_loss = [0] * number_of_players

    return (
        players_name,
        players_roll,
        players_remaining_dices,
        players_score,
        players_score_tmp,
        players_potential_score,
        players_results,
        bonus,
        total_potential_loss
    )


def continue_game():
    answer = str(input("Voulez-vous continuer la partie ? [y/yes/o/oui]: "))
    return re.match("y|yes|o|oui", answer, re.I)


def player_can_continue_playing(remaining_dices: int, score: int) -> bool:
    return score != 0 or remaining_dices != 0 and continue_game()


def defineWinner(number_of_players, players_results, players_score):
    for i in range(number_of_players):
        if players_score[i] == max(players_score):
            players_results[i] += "win"
        else:
            players_results[i] += "lose"

def player_can_continue_playing(remaining_dices: int, score: int) -> bool:
    return score != 0 or remaining_dices != 0 and continue_game()

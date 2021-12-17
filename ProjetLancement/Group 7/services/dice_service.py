import random
from procedural.services.player_service import *
from procedural.services.statistics_service import *
from procedural.services.message_service import *
from typing import Union, Any


def roll_dice_set(nb_dice_to_roll):
    # return in a list the number of times a dice face is found
    dice_value_occurrence_list = [0] * NB_DICE_SIDE
    for n in range(nb_dice_to_roll):
        dice_value = random.randint(1, NB_DICE_SIDE)
        dice_value_occurrence_list[dice_value - 1] += 1
    return dice_value_occurrence_list


def analyse_score(values: list[int]) -> tuple[list[int], int, int, int]:
    # calc the score, number of bonus and remove
    [values, score_bonus, bonus_count] = analyse_bonus_score(values)
    [values, score_standard] = analyse_standard_score(values)
    dice_remaining = get_dice_remaining(values)
    return values, score_bonus + score_standard, dice_remaining, bonus_count


def analyse_standard_score(values: list[int]) -> tuple[list[int], int]:
    # return only the score who is not from bonus
    score = 0
    index = 0
    log = []
    while index < len(LIST_SCORING_DICE_VALUE):
        score += LIST_SCORING_MULTIPLIER[index] * values[LIST_SCORING_DICE_VALUE[index] - 1]
        values[LIST_SCORING_DICE_VALUE[index] - 1] = 0
        index += 1
    return values, score


def analyse_bonus_score(values: list[int]) -> tuple[list[int], int, int]:
    # return only the score who is from bonus and the number of bonus
    index = 0
    score = 0
    bonus_count = 0
    while index < len(LIST_SCORING_DICE_VALUE):
        if values[LIST_SCORING_DICE_VALUE[index] - 1] >= TRIGGER_OCCURRENCE_FOR_BONUS:
            nb_of_bonus = values[LIST_SCORING_DICE_VALUE[index] - 1] // TRIGGER_OCCURRENCE_FOR_BONUS
            if LIST_SCORING_DICE_VALUE[index] == 1:
                bonus_multiplier = BONUS_VALUE_FOR_ACE_BONUS
            else:
                bonus_multiplier = BONUS_VALUE_FOR_NORMAL_BONUS
            score += nb_of_bonus * bonus_multiplier * LIST_SCORING_DICE_VALUE[index]
            values[LIST_SCORING_DICE_VALUE[index] - 1] -= (TRIGGER_OCCURRENCE_FOR_BONUS * nb_of_bonus)
            bonus_count += nb_of_bonus
        index += 1
    return values, score, bonus_count


def get_dice_remaining(values: list[int]) -> int:
    dice_remaining = 0
    for value in values:
        dice_remaining += value
    return dice_remaining


def get_logs(values: list[int]) -> tuple[list[tuple[Union[int, list[int]], Any]], int]:
    # return which face match for the current roll and the number of scoring dice
    logs = []
    index = 0
    scoring_dice = 0
    while index < len(LIST_SCORING_DICE_VALUE):
        if values[LIST_SCORING_DICE_VALUE[index] - 1]:
            logs.append((values[LIST_SCORING_DICE_VALUE[index] - 1], LIST_SCORING_DICE_VALUE[index]))
            scoring_dice += values[LIST_SCORING_DICE_VALUE[index] - 1]
        index += 1
    return logs, scoring_dice


def order_player_by_score() -> list[list[Union[str, int]]]:
    return sorted(PLAYERS, key=lambda row: row[1], reverse=True)


def get_current_rank(index_player: int) -> int:
    # return the collection of player order by score desc
    return order_player_by_score().index(PLAYERS[index_player]) + 1


def next_player(index_player: int, turn: int, roll: int, dice_remaining: int, preview_score_to_add: int,
                potential_score: int, has_lose: bool, max_score: list,
                longest_turn: list[list, int]) -> tuple[int, int, int, int, int, int, bool, list, bool, list]:
    if not has_lose:
        max_score = handle_win(index_player, preview_score_to_add, max_score)

    longest_turn = set_longest_turn(index_player, longest_turn, roll)
    party_is_win = is_party_win(index_player)

    print_after_turn_message()

    if not party_is_win:
        index_player, turn, roll, dice_remaining, preview_score_to_add, potential_score, has_lose = reset_turn(index_player, turn)

    return index_player, turn, roll, dice_remaining, preview_score_to_add, potential_score, has_lose, max_score, party_is_win, longest_turn


def want_replay() -> bool:
    return input('Do you want to replay ? yes/no (yes)') != 'no'


def handle_lose(index_player: int, potential_score: int, max_lost: list) -> list:
    set_player_add_lose_point(index_player, potential_score)
    max_lost = set_turn_lost(index_player, max_lost, potential_score)
    return max_lost


def handle_win(index_player: int, preview_score_to_add: int, max_score: list) -> list:
    set_player_add_score(index_player, preview_score_to_add)
    max_score = max_turn_scoring(index_player, max_score, preview_score_to_add)
    return max_score


def is_party_win(index_player: int):
    return PLAYERS[index_player][1] >= DEFAULT_TARGET_SCORE


def reset_turn(index_player: int, turn: int) -> tuple[int, int, int, int, int, int, bool]:
    # reset set of variable for the next player
    if index_player + 1 == len(PLAYERS):
        turn += 1
        index_player = 0
    else:
        index_player += 1
    roll = 0
    dice_remaining = DEFAULT_DICES_NB
    preview_score_to_add = 0
    potential_score = 0
    has_lose = False

    print_new_turn_message(turn, get_player_name(index_player), get_current_rank(index_player),
                           get_player_score(index_player))
    return index_player, turn, roll, dice_remaining, preview_score_to_add, potential_score, has_lose


def is_full_roll(remaining_dice: int) -> bool:
    return remaining_dice == 0

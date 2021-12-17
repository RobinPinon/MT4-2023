from procedural.config.params import *


def max_turn_scoring(index_player: int, max_score: list, score: int) -> list:
    if score > max_score[1]:
        max_score = [PLAYERS[index_player], score]
    return max_score


def set_longest_turn(index_player: int, longest_turn: list, turns: int) -> list:
    if turns > longest_turn[1]:
        longest_turn = [PLAYERS[index_player], turns]
    return longest_turn


def set_turn_lost(index_player: int, max_lost: list, lost: int) -> list:
    if lost > max_lost[1]:
        max_lost = [PLAYERS[index_player], lost]
    return max_lost


def get_total_win_score() -> int:
    sum = 0
    for player in PLAYERS: sum += player[1]
    return sum


def get_total_lose_score() -> int:
    sum = 0
    for player in PLAYERS: sum += player[3]
    return sum


def get_mean_scoring_turn(nb_turn: int) -> float:
    return round(get_total_win_score() / nb_turn, 2)


def get_mean_lose_scoring_turn(nb_turn: int) -> float:
    return round(get_total_lose_score() / nb_turn, 2)

from procedural.config.params import *


def set_player_add_score(index_player: int, score: int) -> None:
    PLAYERS[index_player][1] += score


def set_player_add_roll(index_player: int, roll: int) -> None:
    PLAYERS[index_player][2] += roll


def set_player_add_lose_point(index_player: int, lose_point: int) -> None:
    PLAYERS[index_player][3] += lose_point


def set_player_add_bonus(index_player: int, bonus: int) -> None:
    PLAYERS[index_player][4] += bonus


def set_player_add_full_roll(index_player: int, full_roll: int) -> None:
    PLAYERS[index_player][5] += full_roll


def get_player_name(index_player: int) -> str:
    return PLAYERS[index_player][0]


def get_player_score(index_player: int) -> int:
    return PLAYERS[index_player][1]


def get_player_roll(index_player: int) -> int:
    return PLAYERS[index_player][2]


def get_player_lose_point(index_player: int) -> int:
    return PLAYERS[index_player][3]


def get_player_bonus(index_player: int) -> int:
    return PLAYERS[index_player][4]


def get_player_full_roll(index_player: int) -> int:
    return PLAYERS[index_player][5]

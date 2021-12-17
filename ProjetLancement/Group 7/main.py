from services.dice_service import *
from procedural.services.player_service import *
from procedural.services.message_service import *

index_player: int = 0
current_turn: int = 1
current_roll: int = 0
dice_remaining: int = DEFAULT_DICES_NB
preview_score_to_add: int = 0
# Party and turn status
turn_is_lose: bool = False
party_is_win: bool = False
# Party statistics
party_max_score: list = [None, 0]  # 1: Player, 2: score
party_longest_turn: list = [None, 0]  # 1: Player, 2: number of current_roll in one current_turn
party_max_lost: list = [None, 0]  # 1: Player, 2: score lost

print_new_turn_message(current_turn, get_player_name(index_player), get_current_rank(index_player), get_player_score(index_player))
while not party_is_win:
    values = roll_dice_set(dice_remaining)
    previous_value = values.copy()
    values, score, dice_remaining, bonus_count = analyse_score(values)
    logs, scoring_dice = get_logs(previous_value)

    current_roll += 1
    set_player_add_roll(index_player, 1)
    set_player_add_bonus(index_player, bonus_count)

    if score == 0:
        turn_is_lose = True

    preview_score_to_add += score
    potential_score = PLAYERS[index_player][1] + preview_score_to_add

    print_after_roll_message(current_roll, scoring_dice, logs, score, potential_score, dice_remaining)

    if turn_is_lose:
        print_lose_turn_message(potential_score)
        party_max_lost = handle_lose(index_player, potential_score, party_max_lost)
        index_player, current_turn, current_roll, dice_remaining, preview_score_to_add, potential_score, turn_is_lose, party_max_score, party_is_win, party_longest_turn = next_player(
            index_player, current_turn, current_roll, dice_remaining, preview_score_to_add, potential_score, turn_is_lose,
            party_max_score, party_longest_turn)
    else:
        if is_full_roll(dice_remaining):
            dice_remaining = DEFAULT_DICES_NB
            set_player_add_full_roll(index_player, 1)
        replay = want_replay()
        if not replay:
            index_player, current_turn, current_roll, dice_remaining, preview_score_to_add, potential_score, turn_is_lose, party_max_score, party_is_win, party_longest_turn = next_player(
                index_player, current_turn, current_roll, dice_remaining, preview_score_to_add, potential_score, turn_is_lose, party_max_score,
                party_longest_turn)

print_statistics_players_message(current_turn)
print_statistics_party_message(party_max_score, party_longest_turn, party_max_lost, current_turn)

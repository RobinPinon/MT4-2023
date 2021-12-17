from procedural.config.params import DEFAULT_TARGET_SCORE
from procedural.services.dice_service import order_player_by_score
from procedural.services.statistics_service import get_mean_scoring_turn, get_mean_lose_scoring_turn


def print_new_turn_message(current_turn: int, player_name: str, player_rank: int, player_score: int) -> None:
    print('\n\nturn #', str(current_turn), '--> ', player_name, ' rank #', player_rank, ', score', player_score)


def print_after_roll_message(roll: int, scoring_dice: int, logs: list, score: int, potential_score: int, dice_remaining: int) -> None:
    print('roll #', roll, ' :', scoring_dice, 'scoring dices', logs, 'scoring ', score, ', potential total turn score ',
          potential_score, ', remaining dice to roll :', dice_remaining)


def print_after_turn_message() -> None:
    message = '\n'
    for player in order_player_by_score():
        message = message + player[0] + '--> ' + str(player[1]) + ' '
    print(message)


def print_lose_turn_message(potential_score: int) -> None:
    print('you lose this turn and a potential to score', potential_score, 'pts')


def print_statistics_players_message(turn: int) -> None:
    print('\n\nGame in ', turn, 'turns')
    for player in order_player_by_score():
        print(player[0], 'win' if player[1] >= DEFAULT_TARGET_SCORE else 'lose', ' !  scoring',
              player[1], 'in', player[2], 'roll with', player[5], 'full roll,',
              player[4], 'bonus and', player[3], 'potential points lost')
    print('\n\n')


def print_statistics_party_message(max_score: list, longest_turn: list, max_lost: list, turn: int) -> None:
    print('Max turn scoring :', max_score[0][0], 'with', max_score[1])
    print('Longest turn :', longest_turn[0][0], 'with', longest_turn[1], 'roll')

    if max_lost[0] is not None:
        print('Max turn loss :', max_lost[0][0], 'with', max_lost[1])
    else:
        print('Nobody lost points')

    print('\n')
    print('Mean scoring turn :', get_mean_scoring_turn(turn), '(', turn, ') turns)')
    print('Mean non scoring turn :', get_mean_lose_scoring_turn(turn), '(', turn, ') turns)')

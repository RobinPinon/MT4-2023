from constants import (DEFAULT_TARGET_SCORE, DEFAULT_DICES_NB)

from helpers import (
    initialize_players_datas,
    analyse_score,
    roll_dice_set,
    continue_game,
    sort_players_by_key,
    display_turn_recap,
    increment_player_data
)


def main():
    number_of_players: int = int(input("Nombre de joueur : "))
    if number_of_players == 0:
        raise Exception('Number of players must be a positive number !')

    play(number_of_players)


def play(number_of_players: int):
    """
    :param number_of_players:
    :return:
    """
    current_max_score = 0
    players = initialize_players_datas(number_of_players)
    game_turn = 0

    while current_max_score <= DEFAULT_TARGET_SCORE:
        game_turn += 1

        for idx, player in enumerate(players):

            won_turn = True
            print(f'turn #{game_turn} --> {player["name"]} rank #{idx}, score {player["total_score"]}')
            # restart player's dices
            player["remaining_dices"] = DEFAULT_DICES_NB
            # player["potential_score"] = 0
            while won_turn and player["remaining_dices"] != 0 and current_max_score <= DEFAULT_TARGET_SCORE:
                dice_roll_result = roll_dice_set(player["remaining_dices"])
                (
                    current_bonus,
                    current_score_with_bonus,
                    dice_roll_set
                ) = analyse_score(dice_roll_result)
                (
                    player,
                    current_score_with_bonus,
                    dice_roll_set,
                    current_bonus,
                    current_max_score
                ) = increment_player_data(player, current_score_with_bonus, dice_roll_set, current_bonus, current_max_score)

                print(f'scoring {current_score_with_bonus}, potential total turn score {player["potential_score"]}, remaining dice to roll : {sum(dice_roll_set)}')

                if current_score_with_bonus and player["remaining_dices"]:
                    if continue_game():
                        won_turn = True
                elif current_score_with_bonus and not player["remaining_dices"]:
                    won_turn = True
                else:
                    won_turn = False

                if won_turn:
                    print(f'You win this turn, scoring {player["score"]} pts')
                else:
                    print(f'You lose this turn and a potential to score {player["potential_score"]}')
                    player["score"] = 0
                    player["potential_score"] = 0
                    break

            display_turn_recap(players)
    game_turn += 1

    max_turn_scoring = sort_players_by_key(players, 'max_turn_scoring')
    longest_turn = sort_players_by_key(players, 'longest_roll')

    print(f'Max turn scoring : {max_turn_scoring["name"]} with {max_turn_scoring["max_turn_scoring"]}')
    print(f'Longest roll turn scoring : {longest_turn["name"]} with {longest_turn["longest_roll"]} rolls')


if __name__ == "__main__":
    main()

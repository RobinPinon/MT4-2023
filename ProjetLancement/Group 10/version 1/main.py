def main():
    number_of_players: int = int(input("Nombre de joueur : "))
    if number_of_players == 0:
        raise Exception('Number of players must be a positive number !')

    run(number_of_players)


def run(number_of_players: int):
    """
    :param number_of_players:
    :return:
    """
    # Swtiches when player scores DEFAULT_TARGET_SCORE
    current_max_score = 0
    players_potential_score: list[int]
    (
        players_name,
        players_roll,
        players_remaining_dices,
        players_score,
        players_score_tmp,
        players_potential_score,
        players_results,
        players_bonus,
        total_potential_loss
    ) = initialize_players_and_datas(number_of_players)

    game_turn = 0
    scoring_sum = 0
    n_scoring_sum = 0
    scoring_turn = 0
    n_scoring_turn = 0

    while current_max_score <= DEFAULT_TARGET_SCORE:
        game_turn += 1

        for p_idx in range(number_of_players):
            print(f'turn #{game_turn} --> {players_name[p_idx]} rank #{p_idx}, score {players_score[p_idx]}')
            continue_playing = True
            players_remaining_dices[p_idx] = 5

            while continue_playing and players_remaining_dices[p_idx] != 0:
                (current_bonus, current_score_with_bonus, dice_roll_set) = analyse_score(
                    roll_dice_set(players_remaining_dices[p_idx])
                )
                players_roll[p_idx] += 1

                players_remaining_dices[p_idx] = sum(dice_roll_set)
                players_potential_score[p_idx] += current_score_with_bonus
                players_score_tmp[p_idx] += current_score_with_bonus

                if current_bonus:
                    players_bonus[p_idx] += 1

                if current_score_with_bonus == 0 or players_remaining_dices[p_idx] == 0:
                    players_score[p_idx] = 0
                    players_score_tmp[p_idx] = 0
                    n_scoring_turn += 1
                    n_scoring_sum += players_potential_score[p_idx]
                else:
                    players_score[p_idx] += current_score_with_bonus
                    scoring_turn += 1
                    scoring_sum += players_potential_score[p_idx]
                    if players_score[p_idx] > current_max_score:
                        current_max_score = players_score[p_idx]

                print(
                    f'scoring {current_score_with_bonus}, potential total turn score {players_score_tmp[p_idx]}, remaining dice to roll : {sum(dice_roll_set)}')
                if not (current_score_with_bonus != 0 and players_remaining_dices[p_idx] != 0 and continue_game()):
                    players_score_tmp[p_idx] = 0
                    print('je ne veux plus jouer ou j\'ai perdu \n\n')
                    break

    if scoring_turn > 0:
        print(f'Mean scoring turn : {scoring_sum / scoring_turn} ({scoring_turn} turns)')

    if n_scoring_turn > 0:
        print(f'Mean non scoring turn : {n_scoring_sum / n_scoring_turn} ({n_scoring_turn} turns) \n')

    defineWinner(number_of_players, players_results, players_score)

    # Print final stats
    for i in range(number_of_players):
        print(f'{players_name[i]} {players_results[i]} !  scoring {players_score[i]} in {players_roll[i]} roll, '
              f'{players_bonus[i]} bonus and {players_potential_score[i] - players_score[i]} potential points lost')

    print('\n')

    # print('players_name', players_name)
    # print('players_roll', players_roll)
    # print('players_remaining_dices', players_remaining_dices)
    # print('players_score', players_score)
    # print('players_potential_score', players_potential_score)
    # print('players_bonus', players_bonus)
    # print('players_results', players_results)

    game_turn += 1


if __name__ == "__main__":
    main()
from helper import *


def main():
    number_of_players: int = int(input("Nombre de joueur : "))
    if number_of_players == 0:
        raise Exception('Number of players must be a positive number !')

    run(number_of_players)


def run(number_of_players: int):
    """
    :param number_of_players:
    :return:
    """
    # Swtiches when player scores DEFAULT_TARGET_SCORE
    current_max_score = 0
    players_potential_score: list[int]
    (
        players_name,
        players_roll,
        players_remaining_dices,
        players_score,
        players_score_tmp,
        players_potential_score,
        players_results,
        players_bonus,
        total_potential_loss
    ) = initialize_players_and_datas(number_of_players)

    game_turn = 0
    scoring_sum = 0
    n_scoring_sum = 0
    scoring_turn = 0
    n_scoring_turn = 0

    while current_max_score <= DEFAULT_TARGET_SCORE:
        game_turn += 1

        for p_idx in range(number_of_players):
            print(f'turn #{game_turn} --> {players_name[p_idx]} rank #{p_idx}, score {players_score[p_idx]}')
            continue_playing = True
            players_remaining_dices[p_idx] = 5

            while continue_playing and players_remaining_dices[p_idx] != 0:
                (current_bonus, current_score_with_bonus, dice_roll_set) = analyse_score(
                    roll_dice_set(players_remaining_dices[p_idx])
                )
                players_roll[p_idx] += 1

                players_remaining_dices[p_idx] = sum(dice_roll_set)
                players_potential_score[p_idx] += current_score_with_bonus
                players_score_tmp[p_idx] += current_score_with_bonus

                if current_bonus:
                    players_bonus[p_idx] += 1

                if current_score_with_bonus == 0 or players_remaining_dices[p_idx] == 0:
                    players_score[p_idx] = 0
                    players_score_tmp[p_idx] = 0
                    n_scoring_turn += 1
                    n_scoring_sum += players_potential_score[p_idx]
                else:
                    players_score[p_idx] += current_score_with_bonus
                    scoring_turn += 1
                    scoring_sum += players_potential_score[p_idx]
                    if players_score[p_idx] > current_max_score:
                        current_max_score = players_score[p_idx]

                print(
                    f'scoring {current_score_with_bonus}, potential total turn score {players_score_tmp[p_idx]}, remaining dice to roll : {sum(dice_roll_set)}')
                if not (current_score_with_bonus != 0 and players_remaining_dices[p_idx] != 0 and continue_game()):
                    players_score_tmp[p_idx] = 0
                    print('je ne veux plus jouer ou j\'ai perdu \n\n')
                    break

    if scoring_turn > 0:
        print(f'Mean scoring turn : {scoring_sum / scoring_turn} ({scoring_turn} turns)')

    if n_scoring_turn > 0:
        print(f'Mean non scoring turn : {n_scoring_sum / n_scoring_turn} ({n_scoring_turn} turns) \n')

    defineWinner(number_of_players, players_results, players_score)

    # Print final stats
    for i in range(number_of_players):
        print(f'{players_name[i]} {players_results[i]} !  scoring {players_score[i]} in {players_roll[i]} roll, '
              f'{players_bonus[i]} bonus and {players_potential_score[i] - players_score[i]} potential points lost')

    print('\n')

    game_turn += 1


if __name__ == "__main__":
    main()

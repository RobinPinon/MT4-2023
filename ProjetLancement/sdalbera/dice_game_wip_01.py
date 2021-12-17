import random
from operator import itemgetter

""" Procedural Farkle dice game implementation.

Game rules : https://en.wikipedia.org/wiki/Farkle

S. Dalbera, Dec 2021
"""

# ----------------------< Game rules constants  >-----------------------------------------------------------------------
# Rules can be parametrized by this globals constants
#
# Standard Farkle rules :
#  5 dices with 6 faces
#  1 & 5 are scoring
#  1 is scoring 100 pts
#  5 is scoring 50 pts
#
#  Bonus for 3 dices with the same value
#    3 ace is scoring 1000 pts
#   3 time the same dice value is scoring 100 pts x the dice value

NB_DICE_SIDE = 6  # Nb of side of the Dices
SCORING_DICE_VALUE = [1, 5]  # List of the side values of the dice who trigger a standard score
SCORING_MULTIPLIER = [100, 50]  # List of multiplier for standard score

THRESHOLD_BONUS = 3  # Threshold of the triggering for bonus in term of occurrence of the same slide value
STD_BONUS_MULTIPLIER = 100  # Standard multiplier for bonus
ACE_BONUS_MULTIPLIER = 1000  # Special multiplier for aces bonus

DEFAULT_DICES_NB = 5  # Number of dices by default in the set


def roll_dice_set(nb_dice_to_roll):
    """ Generate the occurrence list of dice value for nb_dice_to_roll throw

        :parameters     nb_dice_to_roll         the number of dice to throw

        :return:        occurrence list of dice value
    """

    dice_value_occurrence = [0] * NB_DICE_SIDE
    for n in range(nb_dice_to_roll):
        dice_value = random.randint(1, NB_DICE_SIDE)
        dice_value_occurrence[dice_value - 1] += 1

    return dice_value_occurrence


def analyse_bonus_score(dice_value_occurrence):
    """ Compute the score for bonus rules and update occurrence list

        :parameters     dice_value_occurrence       occurrence list of dice value

        :return:        a dictionary with
                        - 'score'                   the score from bonus rules
                        - 'scoring_dice'            occurrence list of scoring dice value
                        - 'non_scoring_dice'        occurrence list of non scoring dice value
    """
    scoring_dice_value_occurrence = [0] * NB_DICE_SIDE

    bonus_score = 0
    for side_value_index, side_value_occurrence in enumerate(dice_value_occurrence):
        nb_of_bonus = side_value_occurrence // THRESHOLD_BONUS
        if nb_of_bonus > 0:
            if side_value_index == 0:
                bonus_multiplier = ACE_BONUS_MULTIPLIER
            else:
                bonus_multiplier = STD_BONUS_MULTIPLIER
            bonus_score += nb_of_bonus * bonus_multiplier * (side_value_index + 1)

            # update the occurrence list after bonus rules for scoring dices and non scoring dices
            dice_value_occurrence[side_value_index] %= THRESHOLD_BONUS
            scoring_dice_value_occurrence[side_value_index] = nb_of_bonus * THRESHOLD_BONUS

    return {'score': bonus_score,
            'scoring_dice': scoring_dice_value_occurrence,
            'non_scoring_dice': dice_value_occurrence}


def analyse_standard_score(dice_value_occurrence):
    """ Compute the score for standard rules and update occurrence list

        :warning :      occurrence list of dice value should be cleaned from potential bonus
                        call analyse_bonus_score() first

        :parameters     dice_value_occurrence       occurrence list of dice value

        :return:        a dictionary with
                        - 'score'                   the score from standard rules
                        - 'scoring_dice'            occurrence list of scoring dice value
                        - 'non_scoring_dice'        occurrence list of non scoring dice value
    """
    scoring_dice_value_occurrence = [0] * NB_DICE_SIDE

    standard_score = 0
    for scoring_value, scoring_multiplier in zip(SCORING_DICE_VALUE, SCORING_MULTIPLIER):
        standard_score += dice_value_occurrence[scoring_value - 1] * scoring_multiplier

        # update the occurrence list after standard rules for scoring dices and non scoring dices
        scoring_dice_value_occurrence[scoring_value - 1] = dice_value_occurrence[scoring_value - 1]
        dice_value_occurrence[scoring_value - 1] = 0

    return {'score': standard_score,
            'scoring_dice': scoring_dice_value_occurrence,
            'non_scoring_dice': dice_value_occurrence}


def analyse_score(dice_value_occurrence):
    """ Compute the score for standard and bonus rules, update occurrence list

        :parameters     dice_value_occurrence       occurrence list of dice value

        :return:        a dictionary with
                        - 'score'                   the score from standard rules
                        - 'scoring_dice'            occurrence list of scoring dice value
                        - 'non_scoring_dice'        occurrence list of non scoring dice value
    """

    analyse_score_bonus = analyse_bonus_score(dice_value_occurrence)
    analyse_score_std = analyse_standard_score(analyse_score_bonus['non_scoring_dice'])

    # the occurrence list of scoring dice value is the sum from scoring dice by bonus and standard rules
    scoring_dice_value_occurrence = [sum(x) for x in
                                     zip(analyse_score_bonus['scoring_dice'], analyse_score_std['scoring_dice'])]

    return {'score': analyse_score_bonus['score'] + analyse_score_std['score'],
            'scoring_dice': scoring_dice_value_occurrence,
            'non_scoring_dice': analyse_score_std['non_scoring_dice']}


def game_turn(current_player, is_interactive=True):
    """ Handle a full player turn

        :parameters     current_player      dictionary of player information
                                            - 'name'
                                            - 'score'
                                            - 'lost_score'
                                            - 'nb_of_roll'
                                            - 'nb_of_turn'
                                            - 'nb_of_scoring_turn'
                                            - 'nb_of_non_scoring_turn'
                                            - 'nb_of_full_roll'

                        is_interactive      boolean for game mode
                                            - True -> interactive game mode
                                            - False -> random choice for game simulation

        :return:        updated dictionary of player information after a game turn
    """

    # turn start with the full set of dices
    remaining_dice_to_roll = DEFAULT_DICES_NB
    roll_again = True

    current_player['nb_of_turn'] += 1

    turn_score = 0
    while roll_again:
        # generate the dice roll and compute the scoring
        dice_value_occurrence = roll_dice_set(remaining_dice_to_roll)
        roll_score = analyse_score(dice_value_occurrence)
        remaining_dice_to_roll = sum(roll_score['non_scoring_dice'])
        current_player['nb_of_roll'] += 1

        if roll_score['score'] == 0:
            # lost roll

            print('\n-->', current_player['name'], 'got zero point ', turn_score, 'lost points\n')

            current_player['nb_of_non_scoring_turn'] += 1
            current_player['lost_score'] += turn_score

            roll_again = False
        else:
            # scoring roll

            turn_score += roll_score['score']
            print('=> Scoring Dice', occurrence_list_to_str(roll_score['scoring_dice']),
                  'for ', roll_score['score'], 'points',
                  'total potential score :', turn_score)

            # In case of scoring roll and no remaining dice to roll the player can roll again the full set of dices
            if remaining_dice_to_roll == 0:
                remaining_dice_to_roll = DEFAULT_DICES_NB
                print('-->Full Roll')
                current_player['nb_of_full_roll'] += 1

            print('Non Scoring Dice ', occurrence_list_to_str(roll_score['non_scoring_dice']),
                  "You can roll", remaining_dice_to_roll, "dices")

            # choice to roll again or stop and take roll score
            if is_interactive:
                # interactive decision for real game
                stop_turn = input("Do you want to roll this dice ? [y/n] ") == "n"
            else:
                # random decision for game simulation (50/50)
                stop_turn = (random.randint(1, 100) % 2) == 0

            if stop_turn:
                # stop turn and take roll score
                current_player['score'] += turn_score
                current_player['nb_of_scoring_turn'] += 1

                print('\n-->', current_player['name'], 'Scoring turn with', turn_score, 'points\n')

                roll_again = False

    return current_player


def full_game(players_name_list, target_score, is_interactive=True):
    """ Handle a full game

            :parameters     players_name_list   list of players name
                            target_score        score to reach to win the game

                            is_interactive      boolean for game mode
                                                - True -> interactive game mode
                                                - False -> random choice for game simulation

            :return:        updated dictionary of player information after a game turn
    """
    players_list = create_players_list(players_name_list)

    is_a_winner = False
    turn_index = 1

    print_turn_start_information(turn_index, players_list)

    player_index = 0
    while not is_a_winner:

        if player_index >= len(players_name_list):
            # All players finished previous full players turn -> next full players turn
            player_index = 0
            turn_index += 1
            print_turn_start_information(turn_index, players_list)

        print(players_list[player_index]['name'], 'play with a score of ', players_list[player_index]['score'])

        players_list[player_index] = game_turn(players_list[player_index], is_interactive)

        if players_list[player_index]['score'] >= target_score:
            print(players_list[player_index]['name'], 'win !!!')
            print_final_statistics(players_list)
            is_a_winner = True
        else:
            player_index += 1


def create_player(player_name):
    """ Create and initialise dictionary data structure to store player information

            :parameters  players_name   name of the player

            :return      dictionary of player information
                        - 'name'
                        - 'score'
                        - 'lost_score'
                        - 'nb_of_roll'
                        - 'nb_of_turn'
                        - 'nb_of_scoring_turn'
                        - 'nb_of_non_scoring_turn'
                        - 'nb_of_full_roll'
    """
    return {'name': player_name,
            'score': 0,
            'lost_score': 0,
            'nb_of_roll': 0,
            'nb_of_turn': 0,
            'nb_of_scoring_turn': 0,
            'nb_of_non_scoring_turn': 0,
            'nb_of_full_roll': 0}


def create_players_list(players_name_list):
    """ Create and initialise list of dictionary data structure to store players information

            :parameters  players_name_list   list of player name

            :return     list of dictionary of player information
                        - 'name'
                        - 'score'
                        - 'lost_score'
                        - 'nb_of_roll'
                        - 'nb_of_turn'
                        - 'nb_of_scoring_turn'
                        - 'nb_of_non_scoring_turn'
                        - 'nb_of_full_roll'
    """

    players_list = []
    for player_name in players_name_list:
        players_list.append(create_player(player_name))

    random.shuffle(players_list)

    return players_list


def print_turn_start_information(turn_index, players_list):
    """ print basic players information in score rank order

            :parameters turn_index   index of the current turn
                        players_list list of player information
    """
    turn_information = '-------- turn # ' + str(turn_index) + ', player rank : \n'
    for player_rank, player in enumerate(sorted(players_list, key=itemgetter('score'), reverse=True)):
        turn_information += '#' + str(player_rank + 1) + ' '
        turn_information += player['name']
        turn_information += '(' + str(player['score']) + 'pts), '

    turn_information += '\n'

    print(turn_information)


def print_final_statistics(players_list):
    """ print full players information in score rank order

            :parameters players_list list of player information
    """

    for player_rank, player in enumerate(sorted(players_list, key=itemgetter('score'), reverse=True)):
        player_information = '#' + str(player_rank + 1) + ' ' + player['name']
        player_information += '(' + str(player['score']) + ' pts), '
        player_information += 'in ' + str(player['nb_of_turn']) + ' turns, '
        player_information += 'with ' + str(player['nb_of_roll']) + ' rolls, '
        player_information += str(player['nb_of_scoring_turn']) + ' scoring turns, '
        player_information += str(player['nb_of_non_scoring_turn']) + ' non scoring turns, '
        player_information += str(player['lost_score']) + ' lost potential pts, '
        player_information += str(player['nb_of_full_roll']) + ' full roll\n '

        print(player_information)


def occurrence_list_to_str(dice_value_occurrence):
    """ convert dice occurrence in string

            :parameters dice_value_occurrence

            :returns    string in format [Dice Side]xNb of Occurrence
    """

    if sum(dice_value_occurrence) == 0:
        # no occurrence for all dice value
        return '[]'

    occurrence_str = ''
    for side_value_index, side_value_occurrence in enumerate(dice_value_occurrence):
        if side_value_occurrence > 0:
            occurrence_str += '[' + str(side_value_index + 1) + ']' + 'x' + str(side_value_occurrence) + ', '

    return occurrence_str


my_players_name_list = ['Pierre', 'Paul', 'Jacques', 'Isabelle', 'Carole']

full_game(my_players_name_list, 3_000, False)

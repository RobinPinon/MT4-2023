import random
from constants import *

# return a list of dices value occurrence for a roll of nb_dice_to_roll dices
def roll_dice_set(nb_dice_to_roll):
    dice_value_occurrence_list = [0] * NB_DICE_SIDE
    for n in range(nb_dice_to_roll):
        dice_value = random.randint(1, NB_DICE_SIDE)
        dice_value_occurrence_list[dice_value - 1] += 1

    return dice_value_occurrence_list

# returns the numbers of dices to roll
def analyse_dices_to_roll(nb_dices_rolled, dice_value_occurence_list):
    return nb_dices_rolled - (nb_dices_rolled - sum(dice_value_occurence_list))


def analyse_bonus_score(dice_value_occurrence_list):
    score = 0
    times_bonus = 0
    for side_value_index, dice_value_occurrence in enumerate(dice_value_occurrence_list):
        nb_of_bonus = dice_value_occurrence // THRESHOLD_BONUS
        if nb_of_bonus > 0:
            if side_value_index == 0:
                bonus_multiplier = ACE_BONUS_MULTIPLIER
            else:
                bonus_multiplier = STD_BONUS_MULTIPLIER
            score += nb_of_bonus * bonus_multiplier * (side_value_index + 1)
            dice_value_occurrence_list[side_value_index] %= THRESHOLD_BONUS
            times_bonus += 1

    return score, dice_value_occurrence_list, times_bonus


def analyse_standard_score(dice_value_occurrence_list):
    score = 0
    for scoring_value, scoring_multiplier in zip(SCORING_DICE_VALUE_LIST, SCORING_MULTIPLIER_LIST):
        score += dice_value_occurrence_list[scoring_value - 1] * scoring_multiplier
        dice_value_occurrence_list[scoring_value - 1] = 0

    return score, dice_value_occurrence_list


def analyse_score(dice_value_occurrence_list):
    bonus_score, dice_value_occurrence_list, times_bonus = analyse_bonus_score(dice_value_occurrence_list)
    standard_score, dice_value_occurrence_list = analyse_standard_score(dice_value_occurrence_list)

    return bonus_score + standard_score, times_bonus

def init_scoreboard():
    scoreboard = {}
    for player in PLAYERS:
        scoreboard[player] = {
            "score": 0,
            "bonus": 0,
            "lost_score": 0,
            "rolls": 0,
            "full_roll": 0,
            "max_potential_lost": 0,
            "rank": 0,
        }
    return scoreboard

def init_stats():
    return {
        "scored_max_turn": {
            "player": "",
            "value": 0
        },
        "max_loss_turn": {
            "player": "",
            "value": 0
        },
        "longest_turn": {
            "player": "",
            "value": 0
        },
        "scoring_turn": {
            "turns": 1,
            "score": 0
        },
        "non_scoring_turn": {
            "turns": 1,
            "score": 0
        }
    }


def get_sorted_scoreboard(scoreboard):
    sorted_dict_keys = sorted(scoreboard, key=lambda x: (scoreboard[x]['score']), reverse=True)
    for player in scoreboard:
        scoreboard[player]['rank'] = sorted_dict_keys.index(player) + 1

    return {x:scoreboard[x] for x in sorted_dict_keys}

def print_total_score(scoreboard):
    sorted_scoreboard = get_sorted_scoreboard(scoreboard)
    total_score = "Total score: "
    for player in sorted_scoreboard:
        current_player_score = sorted_scoreboard[player]['score']
        total_score += f"{player}--> {current_player_score}, "
    print(total_score + "\n")

def get_formatted_winning_occurences(occurences):
    formatted_winning_occurences = []
    for indexOcc, occValue in enumerate(occurences):
        if occValue >= THRESHOLD_BONUS:
            formatted_winning_occurences.append([occValue, indexOcc + 1])

        elif indexOcc + 1 in SCORING_DICE_VALUE_LIST and occValue > 0:
            formatted_winning_occurences.append([occValue, indexOcc + 1])
        

    return formatted_winning_occurences  


def print_endgame_stats(stats):
    print("\n")
    print(f"Max turn scoring : {stats['scored_max_turn']['player']} with {stats['scored_max_turn']['value']}")
    print(f"Longest turn : {stats['longest_turn']['player']} with {stats['longest_turn']['value']}")
    print(f"Max turn loss : {stats['max_loss_turn']['player']} with {stats['max_loss_turn']['value']}")
    print("\n")
    print(f"Mean scoring turn : {round(stats['scoring_turn']['score'] / stats['scoring_turn']['turns'], 2)} ({stats['scoring_turn']['turns']} turns)")
    print(f"Mean non scoring turn : {round(stats['non_scoring_turn']['score'] / stats['non_scoring_turn']['turns'], 2)} ({stats['non_scoring_turn']['turns']} turns)")          

def game():
    is_finished = False
    current_turn = 0
    scoreboard = init_scoreboard()
    stats = init_stats()

    while not is_finished:
        current_turn += 1
        for player in PLAYERS:

            print_total_score(scoreboard)

            print(f"turn#{current_turn}-->{player} rank #{scoreboard[player]['rank']}, score {scoreboard[player]['score']}")
            
            current_roll = 0
            potential_turn_score = 0
            is_looser = False
            reroll = "y"
            remaining_dices = DEFAULT_DICES_NB

            while remaining_dices > 0 and reroll == "y":

                if potential_turn_score > scoreboard[player]['max_potential_lost']:
                    scoreboard[player]['max_potential_lost'] = potential_turn_score

                current_roll += 1
                scoreboard[player]['rolls'] += 1
                dices_occurences = roll_dice_set(remaining_dices)
                formatted_winning_occurences = get_formatted_winning_occurences(dices_occurences)
                previous_remaining_dices = remaining_dices
                potential_roll_score, times_bonus = analyse_score(dices_occurences)
                remaining_dices = analyse_dices_to_roll(remaining_dices, dices_occurences)
                potential_turn_score += potential_roll_score
                
                print(f"roll #{current_roll} : {previous_remaining_dices - remaining_dices} scoring dices {str(formatted_winning_occurences)} scoring {potential_roll_score}, potential total turn score {potential_turn_score}, remaining dice to roll : {remaining_dices}")
                

                # Stats
                if remaining_dices == 0 and potential_roll_score > 0:
                    scoreboard[player]['full_roll'] += 1
                    remaining_dices = DEFAULT_DICES_NB

                if current_roll > stats["longest_turn"]["value"]:
                    stats["longest_turn"]["player"] = player
                    stats["longest_turn"]["value"] = current_roll

                scoreboard[player]['bonus'] += times_bonus

                if potential_roll_score == 0:
                    is_looser = True
                    break
                elif remaining_dices > 0:
                    reroll = input(f"Do you want to reroll {remaining_dices} dices ? [y/n]")


            if is_looser:
                print(f"you lose this turn and a potential to score {potential_turn_score} pts\n")
                scoreboard[player]["lost_score"] += potential_turn_score
                stats["non_scoring_turn"]["turns"] += 1
                stats["non_scoring_turn"]["score"] += potential_turn_score

                if potential_turn_score > stats["max_loss_turn"]["value"]:
                    stats["max_loss_turn"]["player"] = player
                    stats["max_loss_turn"]["value"] = potential_turn_score

            else:
                print(f"you win this turn, scoring {potential_turn_score} pts\n")
                scoreboard[player]["score"] += potential_turn_score
                stats["scoring_turn"]["turns"] += 1
                stats["scoring_turn"]["score"] += potential_turn_score

                if potential_turn_score > stats["scored_max_turn"]["value"]:
                    stats["scored_max_turn"]["player"] = player
                    stats["scored_max_turn"]["value"] = potential_turn_score

            
            if scoreboard[player]["score"] >= DEFAULT_TARGET_SCORE:
                print(f"Game in {current_turn} turns")
                sorted_scoreboard = get_sorted_scoreboard(scoreboard)
                for player in sorted_scoreboard:
                    if sorted_scoreboard[player]['score'] >= DEFAULT_TARGET_SCORE:
                        print(f"{player} wins ! scoring {sorted_scoreboard[player]['score']} in {sorted_scoreboard[player]['rolls']} rolls with {sorted_scoreboard[player]['full_roll']} full roll, {sorted_scoreboard[player]['bonus']} bonus and {sorted_scoreboard[player]['max_potential_lost']} potential points lost")
                    
                    else:
                        print(f"{player} lose ! scoring {sorted_scoreboard[player]['score']} in {sorted_scoreboard[player]['rolls']} rolls with {sorted_scoreboard[player]['full_roll']} full roll, {sorted_scoreboard[player]['bonus']} bonus and {sorted_scoreboard[player]['max_potential_lost']} potential points lost")
                    
                
                print_endgame_stats(stats)
                is_finished = True
                break

  
game()
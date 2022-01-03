import random
import gameConfig
from methods import statsMethods


def roll_dice_set(nb_dice_to_roll):
    """Launch the dice and set a list with an occurence of each value return by the dice

    Parameters

    ----------
    nb_dice_to_roll : int
        the number of dice with have to roll, set at DEFAULT_SIDE_NB

    Returns

    -------
    list
        a list with all the occurence for each side dice

    """
    dice_value_occurrence_list = [0] * gameConfig.NB_DICE_SIDE
    for index in range(nb_dice_to_roll):
        dice_value = random.randint(1, gameConfig.NB_DICE_SIDE)
        dice_value_occurrence_list[dice_value-1] += 1
    return dice_value_occurrence_list

def full_roll(player,dice_to_roll):
    """If the player hit a full-roll, he can roll all the dice again
    
    Parameters
    ----------
    
    player : Dictionnary
        All the data of the player who hit the full-roll(name, score, number of roll, number of full-roll, number of bonus and potential lost)
    
    dice_to_roll : Integer
        The number of dice remaining to roll
    
    Returns
    -------

    Integer
        the new number of dice remaining to roll after the player hit a full-roll
    
    """
    dice_to_roll = gameConfig.DEFAULT_DICES_NB
    player['full-roll'] += 1
    return dice_to_roll

def loosing_roll(loosing_turn, player_turn_score, player,turn_stat_dict,dice_to_roll):
    """if the player have no winning dice he can't roll again

    Parameters
    ----------

    loosing_turn : Integer
        the total number of turn where players loose point
    
    player_turn_score : Integer
        the score the player hit during this turn
    
    player : Dictionnary
        All the data of the player who hit the full-roll(name, score, number of roll, number of full-roll, number of bonus and potential lost)
    
    turn_stat_dict : Dictionnary
        A dictionnary of the max scoring turn, the longest turn and the max turn loss
    
    dice_to_roll : Integer
        The number of dice remaining to roll

    Returns
    -------

    Integer
        The number of dice remaining to roll
    
    Integer
        Add a loosing turn to the total of loosing turn
    

    """
    loosing_turn += 1
    statsMethods.max_turn_loss_analyse(turn_stat_dict, player_turn_score, player)
    player['potential lost'] += player_turn_score
    print('you lose this turn and a potential to score ' + str(player_turn_score))
    dice_to_roll = 0
    return dice_to_roll, loosing_turn

def ask_new_roll(roll, turn_stat_dict, player_score_list, player_turn_score,player,dice_to_roll):
    """The player still have dice he can roll, so we ask him if he want to roll again
    
    Parameters
    ----------
    
    roll : Integer
        the number of roll the player already have
    
    turn_stat_dict : Dictionnary
        A dictionnary of the max scoring turn, the longest turn and the max turn loss
    
    player_score_list : List
        The score foreach player 
    
    player_turn_score : Integer
        the score the player scored during this turn
    
    player : Dictionnary
        All the data of the player who hit the full-roll(name, score, number of roll, number of full-roll, number of bonus and potential lost)
    
    dice_to_roll : Integer
        The number of dice remaining to roll
    
    """
    user_answer = input('do you want to roll again ? y/n ')
    if user_answer == 'n':
        statsMethods.longest_turn_analyse(turn_stat_dict, roll, player)
        player_score_list[player_score_list.index(player['score'])] += player_turn_score
        player['score'] += player_turn_score
        print('\n' + player['name'] + ' win this turn, scoring ' + str(player_turn_score) + '\n')
        dice_to_roll = 0
    return dice_to_roll

def roll(total_winning_dice, player, loosing_turn, player_turn_score, turn_stat_dict,dice_to_roll):
    """Check the result of the last roll and call the appropriate function 
    Parameters
    ----------
    total_winning_dice : Integer
        the number of dice who score on the last roll
    player : Dictionnary
        All the data of the player who hit the full-roll(name, score, number of roll, number of full-roll, number of bonus and potential lost)
    loosing_turn : Integer
        the total number of turn where players loose point
    player_turn_score : Integer
        the score the player scored during this turn
    turn_stat_dict : Dictionnary
        A dictionnary of the max scoring turn, the longest turn and the max turn loss
    dice_to_roll : Integer
        The number of dice remaining to roll
    
    Returns
    -------

    Integer
        The number of dice remaining to roll
    
    Integer
        Add a loosing turn to the total of loosing turn

    """
    if total_winning_dice == gameConfig.DEFAULT_DICES_NB:
        dice_to_roll = full_roll(player,dice_to_roll)
    if total_winning_dice > 0 and dice_to_roll == 0:
        dice_to_roll = full_roll(player,dice_to_roll)
    if total_winning_dice == 0:
        dice_to_roll, loosing_turn = loosing_roll(loosing_turn, player_turn_score, player,turn_stat_dict,dice_to_roll)
    return dice_to_roll, loosing_turn
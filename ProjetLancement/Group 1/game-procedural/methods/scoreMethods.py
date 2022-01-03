import gameConfig
def analyse_bonus_score(dice_value_occurrence_list):
    """Analyse the bonus score, if the player scored bonus points on his launch

    Parameters

    ----------
    dice_value_occurence_list: list
        list of all the occurence for each side of the dice which's appears on the player launch

    Returns

    -------
    integer
        all the bonus point the player win with his roll
    list
        A list of all the tuple(number of winning dice, the winning side value) that make the player win bonus point.
    list
       list of all the occurence for each side of the dice which's appears on the player launch minus those which's appears 3 times

    """
    score_bonus = 0
    bonus_winning_tuple = ()
    bonus_winning_tuple_list = []
    for side_value_index, dice_value_occurrence in enumerate(dice_value_occurrence_list):
        nb_of_bonus = dice_value_occurrence // gameConfig.TRIGGER_OCCURRENCE_FOR_BONUS
        if nb_of_bonus > 0:
            if side_value_index == 0:
                bonus_multiplier = gameConfig.BONUS_VALUE_FOR_ACE_BONUS
            else:
                bonus_multiplier = gameConfig.BONUS_VALUE_FOR_NORMAL_BONUS
            score_bonus += nb_of_bonus * \
                bonus_multiplier * (side_value_index + 1)
            bonus_winning_tuple = (
                gameConfig.TRIGGER_OCCURRENCE_FOR_BONUS, side_value_index+1)
            bonus_winning_tuple_list.append(bonus_winning_tuple)
            dice_value_occurrence_list[side_value_index] %= gameConfig.TRIGGER_OCCURRENCE_FOR_BONUS
    return score_bonus, bonus_winning_tuple_list, dice_value_occurrence_list,

def analyse_standard_score(dice_value_occurrence_list):
    """Analyse the standard score if the player scored standard points on his launch

    Parameters

    ----------
    dice_value_occurence_list: list
        list of all the occurence for each side of the dice which's appears on the player launch

    Returns

    -------
    integer
        all the standard point the player win with his roll
    tuple
        A tuple of the number of winning dice and the winning side value  
    list
       list of all the occurence for each side of the dices which's appears on the player launch minus those which's give him standard points

    """
    score_standard = 0
    standard_winning_tuple = ()
    standard_winning_tuple_list = []
    for scoring_value, scoring_multiplier in zip(gameConfig.LIST_SCORING_DICE_VALUE, gameConfig.LIST_SCORING_MULTIPLIER):
        score_standard += dice_value_occurrence_list[scoring_value -
                                                     1] * scoring_multiplier
        if dice_value_occurrence_list[scoring_value - 1] > 0:
            standard_winning_tuple = (
                dice_value_occurrence_list[scoring_value-1], scoring_value)
            standard_winning_tuple_list.append(standard_winning_tuple)
        dice_value_occurrence_list[scoring_value-1] = 0
    return score_standard, standard_winning_tuple_list, dice_value_occurrence_list,
def analyse_score(dice_value_occurence_list, nb_dice_to_roll, bonus_win_by_player):
    """Analyse if the player scored and his total score

    Parameters

    ----------
    dice_value_occurence_list: list
        list of all the occurence for each side of the dice which's appears on the player launch

    Returns

    -------
    integer
        the total point the player win with his roll
    tuple
        A tuple of the number of winning dice and the winning side value  
    list
       list of all the occurence that did not give him point

    """
    bonus_score, bonus_winning_tuple_list, dice_value_occurence_list, = analyse_bonus_score(
        dice_value_occurence_list)
    standard_score, standard_winning_tuple_list, dice_value_occurence_list, = analyse_standard_score(
        dice_value_occurence_list)  
    nb_winning_dice, nb_dice_to_roll, winning_tuple_list,bonus_win_by_player = handle_tuple_exception(bonus_winning_tuple_list,standard_winning_tuple_list, nb_dice_to_roll,dice_value_occurence_list, bonus_win_by_player)
    return  bonus_score + standard_score,nb_winning_dice, nb_dice_to_roll, winning_tuple_list,bonus_win_by_player

def handle_tuple_exception(bonus_winning_tuple_list,standard_winning_tuple_list, nb_dice_to_roll, dice_value_occurence_list, bonus_win_by_player ):
    """Handle the returns if the list receive by analyse_bonus_score() and analyse_standard_score() exist

    Parameters

    ----------
    bonus_winning_tuple_list : list
        A list of all the tuple(number of winning dice, the winning side value) that make the player win bonus point. 
    
    standard_winning_tuple_list : list
        A list of all the tuple(number of winning dice, the winning side value) that make the player win standard point.
    
    nb_dice_to_roll : integer
        The number of remaining dice to roll

    dice_value_occurence_list : list
        List of all the occurence for each side of the dice which's appears on the player launch minus those which's make him win
    
    bonus_win_by_player : integer
        Number of bonus the player win during the game
    
    Returns

    -------

    Integer
        number of dice winning
    Integer
        The number of remaining dice to roll
    List
        List of tuple(number of winning dice, the winning side value) 
    Integer
        Number of bonus the player win during the game 


    """
    nb_winning_dice = nb_dice_to_roll - sum(dice_value_occurence_list)
    if nb_winning_dice > 0:
        nb_dice_to_roll = sum(dice_value_occurence_list)
    elif nb_winning_dice == 5:
        nb_dice_to_roll =5
    else:
        nb_dice_to_roll = 0
    if not bonus_winning_tuple_list:
        return nb_winning_dice, nb_dice_to_roll, standard_winning_tuple_list,bonus_win_by_player
    elif not standard_winning_tuple_list:
        bonus_win_by_player += len(bonus_winning_tuple_list)
        return nb_winning_dice, nb_dice_to_roll, bonus_winning_tuple_list,bonus_win_by_player
    elif not standard_winning_tuple_list and not bonus_winning_tuple_list:
        return nb_winning_dice, nb_dice_to_roll, bonus_winning_tuple_list,bonus_win_by_player
    else:
        bonus_win_by_player += len(bonus_winning_tuple_list)
        for bonus_tuple_value, standard_tuple_value in zip(bonus_winning_tuple_list, standard_winning_tuple_list):
            winning_tuple_list = []
            winning_tuple_list.append(standard_tuple_value)
            winning_tuple_list.append(bonus_tuple_value)
        return nb_winning_dice, nb_dice_to_roll, winning_tuple_list,bonus_win_by_player
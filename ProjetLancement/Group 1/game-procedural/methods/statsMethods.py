def player_stat_analyse(players_list, winner_name, turn, turn_stat_dict, total_turn, loosing_turn):
    """Analyse the stats for all the player 
    
    Parameters
    ----------
    players_list : List 
        a List of dictionnary foreach player with their name, score, number of roll, number of full-roll, number of bonus and potential lost
    winner_name : string
        The name of the player who win the game
    turn : Integer
        the last turn played
    turn_stat_dict : Dictionnary
        A dictionnary of the max scoring turn, the longest turn and the max turn loss
    total_turn : Integer
        the total number of turn played use for the calcul of the mean scoring turn and the mean non scoring turn
    loosing_turn : Integer
        the total number of turn where players loose point
    
    Returns
    -------

    None
    
    """
    total_score = 0
    total_potential_lost = 0
    scoring_turn = total_turn - loosing_turn
    print('\nGame in %s turns' %(turn))
    players_list_sorted_by_score = sorted(players_list, key=lambda x: x['score'], reverse=True)
    for player in players_list_sorted_by_score:
        total_score += player['score']
        total_potential_lost += player['potential lost']
        if player['name'] == winner_name:
            print('{} win ! scoring  {} in {} roll with {} full roll, {} bonus and {} potential points lost'
                .format(player['name'],player['score'],player['roll'], player['full-roll'], player['bonus'],player['potential lost'] )
            )
        else: 
            print('{} loose ! scoring  {} in {} roll with {} full roll, {} bonus and {} potential points lost'
                .format(player['name'],player['score'],player['roll'], player['full-roll'], player['bonus'],player['potential lost'] )
            )
    print('\nMax turn scoring : {} with {} \nLongest turn : {} with {} roll \nMax turn loss : {} with {}'
        .format(turn_stat_dict['max_turn_scoring'][1],turn_stat_dict['max_turn_scoring'][0],turn_stat_dict['longest_turn'][1], turn_stat_dict['longest_turn'][0], turn_stat_dict['max_turn_loss'][1], turn_stat_dict['max_turn_loss'][0]  )
    )
    mean_scoring_turn = round(total_score/scoring_turn,2)
    mean_non_scoring_turn = round(total_potential_lost/loosing_turn,2)
    print('\nMean scoring turn : {} ({} turns)\nMean non scoring turn : {} ({} turns)'
        .format(mean_scoring_turn,scoring_turn, mean_non_scoring_turn, loosing_turn)
    )

def max_scoring_turn_analyse(turn_stat_dict, player_turn_score,player):
    """Take the maximum score in one turn
    Parameters
    ----------
    turn_stat_dict : Dictionnary
        A dictionnary of the max scoring turn, the longest turn and the max turn loss
    player_turn_score : Integer
        the score the player scored during this turn
    player : Dictionnary
        All the data of the player who hit the full-roll(name, score, number of roll, number of full-roll, number of bonus and potential lost)
    
    Returns
    -------
    None
    

    """
    if player_turn_score >= turn_stat_dict['max_turn_scoring'][0]:
        turn_stat_dict['max_turn_scoring'][0] = player_turn_score
        turn_stat_dict['max_turn_scoring'][1] = player['name']

def max_turn_loss_analyse(turn_stat_dict, player_turn_score,player): 
    """take the maximum score lost in one turn
     Parameters
    ----------
    turn_stat_dict : Dictionnary
        A dictionnary of the max scoring turn, the longest turn and the max turn loss
    player_turn_score : Integer
        the score the player scored during this turn
    player : Dictionnary
        All the data of the player who hit the full-roll(name, score, number of roll, number of full-roll, number of bonus and potential lost)
    
    Returns
    -------
    None
    """
    if player_turn_score > turn_stat_dict['max_turn_loss'][0]:
        turn_stat_dict['max_turn_loss'][0] = player_turn_score
        turn_stat_dict['max_turn_loss'][1] = player['name']

def longest_turn_analyse(turn_stat_dict, roll, player):
    """Set the longest turn play by a player
    Parameters
    ----------
    turn_stat_dict : Dictionnary
        A dictionnary of the max scoring turn, the longest turn and the max turn loss
    roll : Integer
        the number of roll by the player in this turn
    player : Dictionnary
        All the data of the player who hit the full-roll(name, score, number of roll, number of full-roll, number of bonus and potential lost)
    
    Returns
    -------
    None
    """
    if roll > turn_stat_dict['longest_turn'][0]:
        turn_stat_dict['longest_turn'][0] = roll
        turn_stat_dict['longest_turn'][1] = player['name']


def set_player():
    """Ask the number of player and their name create a list of dictionnary foreach player

    Returns

    -------
    List 
        a List of dictionnary foreach player with their name, score, number of roll, number of full-roll, number of bonus and potential lost
    List
        a List of the points scored by each player used to set the rank
    """
    nb_player = int(input('How many player ?'))
    players_list = []
    player_score_list = []
    for index in range(nb_player):
        player_dict = {}
        player_name = input('Name of player ' + str(index+1) + ' ')
        player_dict['name'] = player_name
        player_dict['score'] = 0
        player_dict['roll'] = 0
        player_dict['full-roll'] = 0
        player_dict['bonus'] = 0
        player_dict['potential lost'] = 0
        players_list.append(player_dict)
        player_score_list.append(player_dict['score'])
    return players_list, player_score_list
    
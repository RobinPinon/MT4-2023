def manage_players():
    player_count = int(input('How many players ?'))
    player_list = {}
    nb_player = 1

    for n in range(player_count):
        name = input('Player ' + str(nb_player) + ' what is your name ?')
        player_list[nb_player - 1] = {
            'name': name,
            'score': 0,
            'rolls': 0,
            'bonus': 0,
            'lost_points': 0,
            'no_point_turn': 0,
            'has_won': False,
            'full_rolls': 0
        }
        nb_player = nb_player + 1

    return player_list


def does_player_continue(can_play):
    if not can_play:
        return False

    wanna_play = input('Do you want to continue ? (y/n)')
    while wanna_play != 'y' and wanna_play != 'n':
        wanna_play = input('Do you want to continue ? (y/n)')

    return True if wanna_play == "y" else False


def players_rank(players):
    # orders the table players thanks to players score
    players = {k: v for k, v in sorted(players.items(), key=lambda item: item[1]['score'], reverse=True)}
    return players


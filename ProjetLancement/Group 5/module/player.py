from back.helpers.utils import check_user_boolean_response

# Set up and return all players

def add_players():
    new_player = True
    players = []
    while new_player:
        player_id = len(players) + 1
        players.append(add_player(player_id))
        new_player = check_user_boolean_response(input(f"New player ? [y/n]"))
    return players


# Prompt and return player username
# -------- PARAMETERS --------
# player_id : TYPE = int | Id of the new player

def add_player(player_id):
    player_username = input(f"Player {player_id} ! What's your name ?")
    player = {
            "username": player_username,
            "score": 0,
            "rank": 0,
            "turn": 0,
            "roll_nb": 0,
            "bonus": {"full_roll": 0,"standard":0},
            "potential_points_lost": 0,
    }
    return player

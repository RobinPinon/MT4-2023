from back.helpers.utils import check_user_boolean_response
from ..constant import NB_DICE
from .roll import random_roll_generator


# Manage turn for single player
# -------- PARAMETERS --------
# player_name : TYPE = str | name of the player

def turn_manager(player):

    turn = {
        "win": False,
        "score": 0,
        "dices": NB_DICE,
        "roll_nb": 0,
        "potential_points_lost": 0,
        "bonus": {"full_roll": 0, "standard": 0}
    }

    # Text to introduce the turn
    print(f"turn #{player['turn']}--> {player['username']} rank #{player['rank']}, score {player['score']}")
    input("press any key to roll the dices ! ")

    while turn["dices"] > 0:
        # Generate random roll and get associated output
        roll_output = random_roll_generator(turn["dices"])

        # Update turn
        turn.update({
            "dices": roll_output["dices_left"],
            "score": turn["score"] + roll_output['score'],
            "roll_nb": turn["roll_nb"] + 1
        })

        print(
            f"roll # {turn['roll_nb']} : scoring dices {roll_output['dices_matched']} scoring {roll_output['score']} potential total turn score {turn['score']} remaining dice to roll : {turn['dices']}"
        )

        turn["roll_nb"] += 1
        if roll_output['score'] > 0:

            roll_again = check_user_boolean_response(input('roll again ? [y/n]'))

            if not roll_again:
                turn["win"] = True

                print(f"you win this turn, scoring {turn['score']} pts")
                return turn
        else:
            turn["dices"] = 0
    print(
        f"you lose this turn and a potential to score {turn['score']} pts"
    )

    turn_update = {'score': 0, 'win': False, "potential_points_lost": turn['score']}
    turn.update(turn_update)

    return turn




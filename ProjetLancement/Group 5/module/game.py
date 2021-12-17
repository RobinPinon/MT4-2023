from module.player import add_players
from helpers.utils import check_user_boolean_response
from module.score import analyse_score_winner
from module.turn import turn_manager
from module.stats import apply_statistic_turn, display_stat


def dice_game_manager(play_again):

    """
    Manage game of dice
    -------- PARAMETERS --------
    play_again : TYPE = Boolean | Restart new game directly when TRUE
    same_user : TYPE = Boolean | Restart the game with same user
    add_user : TYPE = Array | Array of the new users to add for the new game
    """

    # Global game stats

    # Initializing the game

    if not play_again:
        new_game = check_user_boolean_response(
            input(
                'Hello & Welcome to the Hetic dice game tournment ! \nDo you want to start a new game ? [y/n]'
            )
        )
    else:
        new_game = True

    if new_game:

        # Init players (see player module for more info about players structure)
        players = add_players()

        # Start Main game loop
        print("Let's begin the game !")
        game_running = True

        while game_running:

            for player in players:

                # Manage player turn then return results
                turn_result = turn_manager(player)
                print("result =====>", turn_result)

                # TODO Check & update player rank

                # TODO Update full player information

                player.update(
                    {
                        "score": player["score"] + turn_result["score"],
                        "roll_nb": player["roll_nb"] + turn_result["roll_nb"],
                        "potential_points_lost": player[
                            "potential_points_lost"
                        ]
                        + turn_result["potential_points_lost"],
                        "turn": player["turn"] + 1,
                        "bonus": {
                            "full_roll": player["bonus"]["full_roll"]
                            + turn_result["bonus"]["full_roll"],
                            "standard": player["bonus"]["standard"]
                            + turn_result["bonus"]["standard"],
                        },
                    }
                )

                # Print total scores for each players
                total_score = "total score : "
                for player in players:
                    total_score += (
                        player["username"] + '-->' + str(player["score"]) + ' '
                    )
                    apply_statistic_turn(
                        username=player['username'],
                        score=turn_result['score'],
                        turn=turn_result["roll_nb"],
                        loss=turn_result["potential_points_lost"],
                    )
                print(total_score)

                # TODO Update game stats

                # Check for winner after every turn

                print(analyse_score_winner(players))
                if analyse_score_winner(players):
                    game_running = False

                    # Return game's winner and players stats to print
                    # print(game_winner_printer)

                    print("Someone win ! Game in 6 turn")
                    display_stat()

                    # Game restart

                    new_game = check_user_boolean_response(
                        input('Do you want to play again ? [y/n]')
                    )
                    if new_game:
                        return dice_game_manager(True)
                    else:
                        print('Good by see you next time')

    else:
        print('Good by see you next time')

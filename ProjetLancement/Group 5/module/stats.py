import statistics as stat

GAME_STAT = {
    "max_turn_scoring": {"username": "", "score": 0},
    "longest_turn": {"username": "", "turn": 0},
    "max_turn_loss": {"username": "", "score": 0},
    "mean_scoring_turn": [],
    "mean_non_scoring_turn": [],
    "game_running": False,
}


def apply_statistic_turn(username, score, loss, turn):
    """
    Check if the player's value is higher than the old one.
    if yes, update the statistics dictionnary
    """
    GAME_STAT["mean_scoring_turn"].append(score)
    GAME_STAT["mean_non_scoring_turn"].append(loss)

    if GAME_STAT["max_turn_loss"]["score"] < loss:
        GAME_STAT.update(
            {"max_turn_loss": {"username": username, "score": loss}}
        )

    if GAME_STAT["max_turn_scoring"]["score"] < score:
        GAME_STAT.update(
            {"max_turn_scoring": {"username": username, "score": score}}
        )

    if GAME_STAT["longest_turn"]["turn"] < turn:
        GAME_STAT.update(
            {"longest_turn": {"username": username, "turn": turn}}
        )


def calcul_means(list_mean):
    """
    Check if the player's value is higher than the old one.
    if yes, update the statistics dictionnary
    """
    if len(list_mean) > 0:
        mean = stat.mean(list_mean)
        return mean


def display_stat():
    mean_score = calcul_means(GAME_STAT["mean_scoring_turn"])
    mean_non_score = calcul_means(GAME_STAT["mean_non_scoring_turn"])
    print(
        f"Max turn scoring : {GAME_STAT['max_turn_scoring']['username']} with {GAME_STAT['max_turn_scoring']['score']}"
    )
    print(
        f"Max turn loss : {GAME_STAT['max_turn_loss']['username']} with {GAME_STAT['max_turn_loss']['score']}"
    )
    print(
        f"Longest turn : {GAME_STAT['longest_turn']['username']} with {GAME_STAT['longest_turn']['turn']} roll"
    )
    print(f"Mean scoring turn : {mean_score}")
    print(f"Mean non scoring turn : {mean_non_score}")

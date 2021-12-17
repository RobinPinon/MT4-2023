import random
import parametres as params


def create_player():
    PLAYER = []
    how_many_player = int(input("combien de joueur êtes vous ? "))
    for index in range(how_many_player):
        player_username = str(input("votre nom "))
        PLAYER.append(
            {
                "username": player_username,
                "score": 0,
                "RoundScore": 0,
                "turnScore": 0,
                "id": index,
                "isWining": False,
                "endTurn": False,
                "diceToThrow": params.THROW_DICE_COUNTER,
            }
        )
    return PLAYER


def roll_dice_set(player):
    print(f"{player['username']}")
    dice_to_throw = player["diceToThrow"]
    dice_value_occurrence_list = [0] * params.NB_DICE_SIDE
    for n in range(dice_to_throw):
        dice_value = random.randint(1, params.NB_DICE_SIDE)
        dice_value_occurrence_list[dice_value - 1] += 1

    player["diceToThrow"] = 0
    return dice_value_occurrence_list


def analyse_bonus_score(dice_value_occurrence_list, player):
    print(dice_value_occurrence_list)
    bonus_score = 0
    for index, dice_value in enumerate(dice_value_occurrence_list):
        nb_of_bonus = dice_value // params.TRIGGER_OCCURRENCE_FOR_BONUS
        if nb_of_bonus > 0:
            if index == 0:
                bonus_mulitplier = params.BONUS_VALUE_FOR_ACE_BONUS
            else:
                bonus_mulitplier = params.BONUS_VALUE_FOR_NORMAL_BONUS

            bonus_score += nb_of_bonus * bonus_mulitplier * (index + 1)
            dice_value_occurrence_list[index] %= params.TRIGGER_OCCURRENCE_FOR_BONUS

    player["turnScore"] += bonus_score
    return dice_value_occurrence_list


def analyse_standard_score(dice_value_occurrence_list, player):
    standard_score = 0
    for scoring_value, scoring_multiplier in zip(
        params.LIST_SCORING_DICE_VALUE, params.LIST_SCORING_MULTIPLIER
    ):
        standard_score += (
            dice_value_occurrence_list[scoring_value - 1] * scoring_multiplier
        )
        dice_value_occurrence_list[scoring_value - 1] = 0

    player["turnScore"] += standard_score
    return dice_value_occurrence_list


def analyse_score(dice_value_occurrence_list, player):
    player["RoundScore"] += player["turnScore"]
    print("votre score sur ce lancé est de : " + str(player["turnScore"]))
    print(f"votre score sur ce round est de  {player['RoundScore']}")

    if player["turnScore"] + player["score"] > player["score"]:
        for n in dice_value_occurrence_list:
            player["diceToThrow"] += n
        if player["diceToThrow"] == 0:
            player["diceToThrow"] = 6
        player["score"] += player["turnScore"]
        player["turnScore"] = 0
        if player["score"] >= params.DEFAULT_TARGET_SCORE:
            return None
    else:
        player["turnScore"] = 0
        player["endTurn"] = True
        return None

    print("Il vous reste " + str(player["diceToThrow"]) + " a lancer")
    wannaPlayAgain = input("voulez vous relancez ? Oui | Non ")
    if wannaPlayAgain == "Oui" or wannaPlayAgain == "oui":
        player["endTurn"] = False
    else:
        player["endTurn"] = True
        return None


def round(players):
    for player in players:
        print(
            " C'est au tour de "
            + str(player["username"] + " avec un score de " + str(player["score"]))
        )
        print("")
        player["RoundScore"] = 0
        player["endTurn"] = False
        player["diceToThrow"] = params.THROW_DICE_COUNTER


        while not player["endTurn"]:
            dice_value_occurrence_list = roll_dice_set(player)
            dice_value_occurrence_list = analyse_bonus_score(
                dice_value_occurrence_list, player
            )
            dice_value_occurrence_list = analyse_standard_score(
                dice_value_occurrence_list, player
            )
            analyse_score(dice_value_occurrence_list, player)
            if player["score"] >= params.DEFAULT_TARGET_SCORE:
                params.SOMEONE_WIN = True
                print(
                    "the winner is "
                    + str(
                        player["username"] + " avec un score de " + str(player["score"])
                    )
                )
                break


def sort_players(players):
    sorted_players = dict(sorted(players.items(), key=lambda item: item['score']))
    return sorted_players


def game():
    players = create_player()
    i = 0
    while params.SOMEONE_WIN is False:
        i += 1
        print("------------------------------------------")
        print(f"tour numéro: {i}")
        print("------------------------------------------")
        round(players)

        # print(sort_players(players))


if __name__ == "__main__":
    game()

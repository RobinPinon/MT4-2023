from .Player import Player


class GameStat:

    def __init__(self) -> None:
        pass

    @staticmethod
    def print_turn_stats(players: [Player], turn_index: int) -> None:
        """
        print basic players information in score rank order

        @param players: list of players
        @param turn_index: index of the current turn
        @return: None
        """
        turn_information = '|-------------------------------------|\n'
        turn_information += f'| TURN #{str(turn_index)}, player rank : \n'
        for rank, player in enumerate(GameStat.sort_players_by_score(players)):
            turn_information += f'| #{str(rank + 1)} {player.name} ({str(player.score)} pts) \n'
        turn_information += '|-------------------------------------|'
        turn_information += '\n'

        print(turn_information)

    @staticmethod
    def print_final_stats(players: [Player]) -> None:
        """
        print full players information in score rank order
        @param players: players_list list of player information
        @return:
        """
        for rank, player in enumerate(GameStat.sort_players_by_score(players)):
            ranking_stats = \
                f"| #{rank + 1} {player.name} => {player.score} points in {player.nb_of_turn} turns with {player.nb_of_roll} rolls, " \
                f"{player.nb_of_scoring_turn} scoring turn, {player.nb_of_non_scoring_turn} non scoring turns and " \
                f"{player.lost_score} lost potential points \n"

            print(ranking_stats)

    @staticmethod
    def sort_players_by_score(players: [Player]) -> [Player]:
        return sorted(players, key=lambda x: x.score, reverse=True)

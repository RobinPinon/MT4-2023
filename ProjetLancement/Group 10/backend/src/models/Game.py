from config.constants import DEFAULT_TARGET_SCORE

from .GameStat import GameStat
from .Player import Player


class Game:

    def __init__(self, list_of_players: [str], is_interactive: bool = False):
        self._players = [Player(player) for player in list_of_players]
        self._is_a_winner = False
        self._is_interactive = is_interactive

    @property
    def players(self) -> [Player]:
        return self._players

    @property
    def is_a_winner(self) -> bool:
        return self._is_a_winner

    @is_a_winner.setter
    def is_a_winner(self, value: bool):
        self._is_a_winner = value

    @property
    def is_interactive(self) -> bool:
        return self._is_interactive

    @is_interactive.setter
    def is_interactive(self, value: bool):
        self._is_interactive = value

    def play(self):
        turn_index = 1
        player_index = 0
        while not self.is_a_winner:
            current_player = self.players[player_index]

            if player_index >= len(self.players) - 1:
                # All players finished previous full players turn -> next full players turn
                player_index = 0
                turn_index += 1
                GameStat.print_turn_stats(self.players, turn_index)

            print(f'➡ {current_player.name} play with a score of {current_player.score}')

            current_player = current_player.play_turn(self.is_interactive)

            if current_player.is_winner():
                self.is_a_winner = True
                GameStat.print_final_stats(self.players)
            else:
                player_index += 1

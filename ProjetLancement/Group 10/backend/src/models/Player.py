import random

from config.constants import (
    DEFAULT_DICES_NB,
    DEFAULT_TARGET_SCORE
)

from .GameTurn import GameTurn


class Player:

    @property
    def name(self) -> str:
        return self._name

    @property
    def score(self) -> int:
        return self._score

    @property
    def lost_score(self) -> int:
        return self._lost_score

    @property
    def nb_of_roll(self) -> int:
        return self._nb_of_roll

    @property
    def nb_of_turn(self) -> int:
        return self._nb_of_turn

    @property
    def nb_of_scoring_turn(self) -> int:
        return self._nb_of_scoring_turn

    @property
    def nb_of_non_scoring_turn(self) -> int:
        return self._nb_of_non_scoring_turn

    @property
    def nb_of_full_roll(self) -> int:
        return self._nb_of_full_roll

    def __init__(self, name):
        self._name = name
        self._score = 0
        self._lost_score = 0
        self._nb_of_roll = 0
        self._nb_of_turn = 0
        self._nb_of_scoring_turn = 0
        self._nb_of_non_scoring_turn = 0
        self._nb_of_full_roll = 0

    def play_turn(self, is_interactive):
        # turn start with the full set of dices
        remaining_dice_to_roll = DEFAULT_DICES_NB
        roll_again = True

        self.nb_of_turn += 1

        turn_score = 0
        while roll_again:
            (
                dice_value_occurrence, roll_score, remaining_dice_to_roll
            ) = self.generate_dice_roll_and_compute_scoring(remaining_dice_to_roll)
            self.nb_of_roll += 1
            if roll_score['score'] == 0:
                # lost roll
                print(f"\n--> {self.name} got zero point {turn_score} lost points\n")
                self.nb_of_non_scoring_turn += 1
                self.lost_score += turn_score
                roll_again = False
            else:
                turn_score += roll_score['score']
                print('-------------------------------------------')
                print(f"## Scoring {roll_score['score']} points")
                print(f"## Total potential score => {turn_score}")

                if remaining_dice_to_roll == 0:
                    remaining_dice_to_roll = DEFAULT_DICES_NB
                    print('--> Full Roll')
                    self.nb_of_full_roll += 1

                print(f"## You can roll {remaining_dice_to_roll} dices")
                print('-------------------------------------------')

                if is_interactive:
                    # interactive decision for real game
                    stop_turn = input("Do you want to roll this dice ? [y/n] ") == "n"
                else:
                    # random decision for game simulation (50/50)
                    stop_turn = (random.randint(1, 100) % 2) == 0

                if stop_turn:
                    # stop turn and take roll score
                    self.score += turn_score
                    self.nb_of_scoring_turn += 1

                    print('\n-->', self.name, 'Scoring turn with',
                          turn_score, 'points\n')

                    roll_again = False
        return self

    def generate_dice_roll_and_compute_scoring(self, remaining_dice_to_roll):
        game_turn = GameTurn(remaining_dice_to_roll)
        dice_value_occurrence = game_turn.roll_dice_set()
        roll_score = game_turn.analyse_score()
        remaining_dice_to_roll = sum(roll_score['non_scoring_dice'])
        return dice_value_occurrence, roll_score, remaining_dice_to_roll

    def occurrence_list_to_str(self, dice_value_occurrence):
        """ convert dice occurrence in string

                :parameters dice_value_occurrence

                :returns    string in format [Dice Side]xNb of Occurrence
        """

        if sum(dice_value_occurrence) == 0:
            # no occurrence for all dice value
            return '[]'

        occurrence_str = ''
        for side_value_index, side_value_occurrence in enumerate(dice_value_occurrence):
            if side_value_occurrence > 0:
                occurrence_str += f'[{side_value_index + 1}] x {side_value_occurrence}, '

        return occurrence_str

    def is_winner(self):
        return self.score >= DEFAULT_TARGET_SCORE

    @name.setter
    def name(self, value):
        self._name = value

    @score.setter
    def score(self, value):
        self._score = value

    @lost_score.setter
    def lost_score(self, value):
        self._lost_score = value

    @nb_of_roll.setter
    def nb_of_roll(self, value):
        self._nb_of_roll = value

    @nb_of_turn.setter
    def nb_of_turn(self, value):
        self._nb_of_turn = value

    @nb_of_scoring_turn.setter
    def nb_of_scoring_turn(self, value):
        self._nb_of_scoring_turn = value

    @nb_of_non_scoring_turn.setter
    def nb_of_non_scoring_turn(self, value):
        self._nb_of_non_scoring_turn = value

    @nb_of_full_roll.setter
    def nb_of_full_roll(self, value):
        self._nb_of_full_roll = value

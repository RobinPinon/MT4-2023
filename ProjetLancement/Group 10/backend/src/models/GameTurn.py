import random

from config.constants import (
    NB_DICE_SIDE,
    LIST_SCORING_DICE_VALUE,
    LIST_SCORING_MULTIPLIER,
    BONUS_VALUE_FOR_NORMAL_BONUS,
    BONUS_VALUE_FOR_ACE_BONUS,
    TRIGGER_OCCURRENCE_FOR_BONUS
)


class GameTurn:

    @property
    def dice_value_occurrence(self):
        return self._dice_value_occurrence

    @property
    def nb_dice_to_roll(self):
        return self._nb_dice_to_roll

    def __init__(self, nb_dice_to_roll, dice_value_occurrence=None) -> None:
        if dice_value_occurrence is None:
            dice_value_occurrence = []
        self._nb_dice_to_roll = nb_dice_to_roll
        self._dice_value_occurrence = dice_value_occurrence

    @dice_value_occurrence.setter
    def dice_value_occurrence(self, value):
        self._dice_value_occurrence = value

    @nb_dice_to_roll.setter
    def nb_dice_to_roll(self, value):
        self._nb_dice_to_roll = value

    def roll_dice_set(self):
        """ Generate the occurrence list of dice value for nb_dice_to_roll throw
            :parameters     nb_dice_to_roll         the number of dice to throw
            :return:        occurrence list of dice value
        """
        self.dice_value_occurrence = [0] * NB_DICE_SIDE
        for n in range(self.nb_dice_to_roll):
            dice_value = random.randint(1, NB_DICE_SIDE)
            self.dice_value_occurrence[dice_value - 1] += 1

        return self.dice_value_occurrence

    def analyse_bonus_score(self):
        """ Compute the score for bonus rules and update occurrence list

            :parameters     dice_value_occurrence       occurrence list of dice value

            :return:        a dictionary with
                            - 'score'                   the score from bonus rules
                            - 'scoring_dice'            occurrence list of scoring dice value
                            - 'non_scoring_dice'        occurrence list of non scoring dice value
        """
        scoring_dice_value_occurrence = [0] * NB_DICE_SIDE
        bonus_score = 0
        for side_value_index, side_value_occurrence in enumerate(self.dice_value_occurrence):
            nb_of_bonus = side_value_occurrence // TRIGGER_OCCURRENCE_FOR_BONUS
            if nb_of_bonus > 0:

                if side_value_index == 0:
                    bonus_multiplier = BONUS_VALUE_FOR_ACE_BONUS
                else:
                    bonus_multiplier = BONUS_VALUE_FOR_NORMAL_BONUS

                bonus_score += nb_of_bonus * bonus_multiplier * (side_value_index + 1)

                # update the occurrence list after bonus rules for scoring dices and non scoring dices
                self.dice_value_occurrence[side_value_index] %= TRIGGER_OCCURRENCE_FOR_BONUS
                scoring_dice_value_occurrence[side_value_index] = nb_of_bonus * TRIGGER_OCCURRENCE_FOR_BONUS

        return {
            'score': bonus_score,
            'scoring_dice': scoring_dice_value_occurrence,
            'non_scoring_dice': self.dice_value_occurrence
        }

    def analyse_standard_score(self, dice_value_occurrence):
        """ Compute the score for standard rules and update occurrence list

            :warning :      occurrence list of dice value should be cleaned from potential bonus
                            call analyse_bonus_score() first

            :parameters     dice_value_occurrence       occurrence list of dice value

            :return:        a dictionary with
                            - 'score'                   the score from standard rules
                            - 'scoring_dice'            occurrence list of scoring dice value
                            - 'non_scoring_dice'        occurrence list of non scoring dice value
        """
        scoring_dice_value_occurrence = [0] * NB_DICE_SIDE

        standard_score = 0
        for scoring_value, scoring_multiplier in zip(LIST_SCORING_DICE_VALUE, LIST_SCORING_MULTIPLIER):
            standard_score += dice_value_occurrence[scoring_value - 1] * scoring_multiplier

            # update the occurrence list after standard rules for scoring dices and non scoring dices
            scoring_dice_value_occurrence[scoring_value - 1] = dice_value_occurrence[scoring_value - 1]
            dice_value_occurrence[scoring_value - 1] = 0

        return {
            'score': standard_score,
            'scoring_dice': scoring_dice_value_occurrence,
            'non_scoring_dice': dice_value_occurrence
        }

    def analyse_score(self):
        """ Compute the score for standard and bonus rules, update occurrence list

            :parameters     dice_value_occurrence       occurrence list of dice value

            :return:        a dictionary with
                            - 'score'                   the score from standard rules
                            - 'scoring_dice'            occurrence list of scoring dice value
                            - 'non_scoring_dice'        occurrence list of non scoring dice value
        """

        analyse_score_bonus = self.analyse_bonus_score()
        analyse_score_std = self.analyse_standard_score(analyse_score_bonus['non_scoring_dice'])

        # the occurrence list of scoring dice value is the sum from scoring dice by bonus and standard rules
        scoring_dice_value_occurrence = [sum(x) for x in zip(analyse_score_bonus['scoring_dice'], analyse_score_std['scoring_dice'])]

        return {
            'score': analyse_score_bonus['score'] + analyse_score_std['score'],
            'scoring_dice': scoring_dice_value_occurrence,
            'non_scoring_dice': analyse_score_std['non_scoring_dice']
        }

    def occurrence_list_to_str(self):
        """ convert dice occurrence in string
            :parameters dice_value_occurrence
            :returns string in format [Dice Side]xNb of Occurrence
        """
        if sum(self.dice_value_occurrence) == 0:
            # no occurrence for all dice value
            return '[]'

        occurrence_str = ''
        for side_value_index, side_value_occurrence in enumerate(self.dice_value_occurrence):
            if side_value_occurrence > 0:
                occurrence_str += '[' + str(side_value_index + 1) + ']' + 'x' + str(side_value_occurrence) + ', '

        return occurrence_str

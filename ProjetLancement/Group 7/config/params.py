# Target total score to win by default
from typing import Union

DEFAULT_TARGET_SCORE: int = 2000

# Number of dices by default in the set
DEFAULT_DICES_NB: int = 6
# Number of side of the dices used in the game
NB_DICE_SIDE: int = 6

# List of dice value scoring
LIST_SCORING_DICE_VALUE: list[int] = [1, 5]
# List of associated score for scoring dice values
LIST_SCORING_MULTIPLIER: list[int] = [100, 50]

# Trigger for multiple bonus
TRIGGER_OCCURRENCE_FOR_BONUS: int = 3
# Special bonus multiplier for multiple ace bonus
BONUS_VALUE_FOR_ACE_BONUS: int = 1000
# Standard multiplier for multiple dices value bonus
BONUS_VALUE_FOR_NORMAL_BONUS: int = 100

# Collections of player
# 0: name
# 1: score
# 2: number of roll
# 3: number of lose points
# 4: number of bonus
# 5: number of full roll
PLAYERS: list[list[Union[str, int, int, int, int, int]]] = [['Romain', 0, 0, 0, 0, 0], ['Lucie', 0, 0, 0, 0, 0]]


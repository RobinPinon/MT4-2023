# ----------------------< Game rules constants  >-----------------------------------------------------------------------
# Rules can be parametrized by this globals constants
#
# Standard Farkle rules :
#  5 dices with 6 faces
#  1 & 5 are scoring
#  1 is scoring 100 pts
#  5 is scoring 50 pts
#
#  Bonus for 3 dices with the same value
#   3 ace is scoring 1000 pts
#   3 time the same dice value is scoring 100 pts signal the dice value

# Target total score to win by default
DEFAULT_TARGET_SCORE = 2000

# Number of dices by default in the set
DEFAULT_DICES_NB = 5
# Number of side of the dices used in the game
NB_DICE_SIDE = 6

# List of dice value scoring
LIST_SCORING_DICE_VALUE = [1, 5]
# List of associated score for scoring dice values
LIST_SCORING_MULTIPLIER = [100, 50]

# Trigger for multiple bonus
TRIGGER_OCCURRENCE_FOR_BONUS = 3
# Special bonus multiplier for multiple ace bonus
BONUS_VALUE_FOR_ACE_BONUS = 1000
# Standard multiplier for multiple dices value bonus
BONUS_VALUE_FOR_NORMAL_BONUS = 100


# ----------------------------------------------------------------------------------------------------------------------
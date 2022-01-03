class GameSetting:
    """
    Constants game
    """

    # Number of dice to throw
    NB_DICE_ROLLS: int = 5

    # Number of turns completed
    turns: int = 0

    # Debug
    DEBUG: bool = True

    # Score to reach
    DEFAULT_TARGET_SCORE: int = 2000

    # Number of occurrences to trigger the bonus
    TRIGGER_OCCURRENCE_FOR_BONUS: int = 3

    # Point multiplier for a classic bonus
    BONUS_VALUE_FOR_NORMAL_BONUS: int = 100

    # Point multiplier for an ACE
    BONUS_VALUE_FOR_ACE_BONUS: int = 1000

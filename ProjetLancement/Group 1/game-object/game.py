from src.models.dice_model import DiceModel
from src.game_method import GameMethod
from src.models.player_model import PlayerModel
from src.settings.score_bonus_setting import ScoreBonusSetting


def main():
    game: GameMethod = GameMethod()
    dice_model: DiceModel = DiceModel()

    player_1: PlayerModel = PlayerModel('Jean')
    player_2: PlayerModel = PlayerModel('Romain')
    player_3: PlayerModel = PlayerModel('Victor')
    player_4: PlayerModel = PlayerModel('Fiona')

    game.add_players(player_1, player_2, player_3, player_4)

    score_bonus_1: ScoreBonusSetting = ScoreBonusSetting(1, 100)
    score_bonus_2: ScoreBonusSetting = ScoreBonusSetting(5, 50)

    game.add_scores(score_bonus_1, score_bonus_2)

    while not game.get_player_winner():
        player_turn, turn_selected = game.get_player_turn()

        if turn_selected.roll == 1:
            print(f"Turn #{game.turns} --> {player_turn.name} | score: {player_turn.score}")

        rolls: [int] = dice_model.get_rolls_dice(turn_selected.nb_dice_rolls)

        score, dice_sorted, dice_result_sorted = game.calculate_score(dice_model.NB_DICE_FACES, rolls)

        turn_selected.set_roll_done(rolls, score, dice_sorted, dice_result_sorted)
        turn_selected.get_roll_result()
        turn_selected.get_turn_next_roll_logic()

        game.get_players_dashboard(turn_selected)

    game.get_results_dashboard()
    game.get_game_resume()


main()

from methods import gameMethods

turn_stat_dict = {'max_turn_scoring':[0,''], 'longest_turn' : [0,''], 'max_turn_loss' : [0,'']}
total_turn = 0
loosing_turn = 0
turn = 1


gameMethods.play(turn_stat_dict, total_turn, turn, loosing_turn)

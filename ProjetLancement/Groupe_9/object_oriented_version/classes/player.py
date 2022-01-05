# from ..utils.constant import NB_OF_PLAYERS
from methods import roll_dice_set, analyse_score, separate_text
from classes.stats import Stats

class Player(object):

  def __init__(self, name):
    self._name = name
    self._score = 0
    self._stats = Stats()

  def _get_name(self):
    return self._name
  
  def _set_name(self, new_name):
    self._name = new_name
  
  def _get_score(self):
    return self._score
  
  def _set_score(self, new_score):
    self._score = new_score

  def _play_turn(self):
    user_result = analyse_score(roll_dice_set(5, self), self)
    sum_occurrences = sum(user_result['occurrences'])
    score = user_result['score']
    print('score: %s || dé(s) à relancer: %s' % (score, sum_occurrences))
    separate_text()
    if sum_occurrences == 0:
      self._stats._increment_perfects()
      self._stats._increment_bonus()
      sum_occurrences = 5
      print('LUCKY GUY YOU CAN ROOOOOOOLLL AGAIN')
      print('score: %s || dé(s) à relancer: %s' % (score, sum_occurrences))
      separate_text()
    can_roll_dices = self._reroll()
    while can_roll_dices and sum_occurrences > 0:
      reroll_result = analyse_score(roll_dice_set(sum_occurrences, self), self)
      sum_reroll_occurrences = sum(reroll_result['occurrences'])
      if sum_occurrences == sum_reroll_occurrences:
        score = 0
        self._stats._increment_fails()
        print("T'as perdu mon reuf, on passe au joueur suivant")
        separate_text()
        break
      sum_occurrences = sum_reroll_occurrences
      score += reroll_result['score']
      print('score: %s || dé(s) à relancer: %s' % (score, sum_reroll_occurrences))
      separate_text()
      can_roll_dices = self._reroll()
    self._set_score(self._get_score() + score)

    
  def _reroll(self):
    print('Tu veux relancer ? y/n')
    user_input = input()
    separate_text()
    roll_again = False
    if user_input == 'y':
      roll_again = True
    elif user_input == 'n':
      roll_again = False
    else:
      self._reroll()
    return roll_again

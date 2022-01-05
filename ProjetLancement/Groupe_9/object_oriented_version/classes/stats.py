class Stats(object):

  def __init__(self):
    self._fails = 0
    self._perfects = 0
    self._bonus = 0
    self._highest_bonus = 0
    self._dice_values = {
      1: 0,
      2: 0,
      3: 0,
      4: 0,
      5: 0,
      6: 0,
    }

  def _get_fails(self):
    return self._fails

  def _increment_fails(self):
    self._fails += 1

  def _get_perfects(self):
    return self._perfects

  def _increment_perfects(self):
    self._perfects += 1

  def _get_bonus(self):
    return self._bonus

  def _increment_bonus(self):
    self._bonus += 1

  def _get_highest_bonus(self):
    return self._highest_bonus

  def _set_highest_bonus(self, bonus):
    if (bonus > self._highest_bonus):
      self._highest_bonus = bonus

  def _get_dice_values(self):
    return self._dice_values

  def _increment_dice_values(self, value):
    self._dice_values[value] += 1

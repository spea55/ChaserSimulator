import GameSystem

class CHaserSimulator:
  def __init__(self):
    self.system = GameSystem()

  def __order(self, str: str):
    responce = self.system.gameStep(str)

    if responce[0] == 1:
      return [int(x) for x in responce[1:10]]

  def get_ready(self):
    return self.__order("gr")

  def walk_up(self):
    return self.__order("wp")

  def walk_down(self):
    return self.__order("wd")

  def walk_left(self):
    return self.__order("wl")

  def walk_right(self):
    return self.__order("wr")

  def look_up(self):
    return self.__order("lu")

  def look_down(self):
    return self.__order("ld")

  def look_left(self):
    return self.__order("ll")

  def look_right(self):
    return self.__order("lr")

  def search_up(self):
    return self.__order("su")

  def search_down(self):
    return self.__order("sd")

  def search_left(self):
    return self.__order("sl")

  def search_right(self):
    return self.__order("sr")

  def put_up(self):
    return self.__order("pu")

  def put_down(self):
    return self.__order("pd")

  def put_left(self):
    return self.__order("pl")

  def put_right(self):
    return self.__order("pr")
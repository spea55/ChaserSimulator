#from chaser_simulator.Map import Map
#from chaser_simulator.Action import Action
#import GameBoard
from enum import Enum

class GameSystem:
  class MapObject(Enum):
    NOTHING = 0,
    TARGET  = 1,
    BLOCK   = 2,
    ITEM    = 3

  class Method:
    class Action(Enum):
      WALK      = 0,
      LOOK      = 1,
      SEARCH    = 2,
      PUT       = 3,
      GETREADY  = 4,
      UNKNOWN   = 5

    class Rote(Enum):
      UP    = 0,
      DOWN  = 1,
      LEFT  = 2,
      RIGHT = 3,
      UNKNOWN = 4

    def __init__(self):
      self.action = self.Action.UNKNOWN
      self.rote = self.Rote.UNKNOWN

    def from_string(self, str):
      #コマンドをメソッドの配列に変換
      if   str[0] == 'w': self.action = GameSystem.Method.Action.WALK
      elif str[0] == 'l': self.action = GameSystem.Method.Action.LOOK
      elif str[0] == 's': self.action = GameSystem.Method.Action.SEARCH
      elif str[0] == 'p': self.action = GameSystem.Method.Action.PUT
      else:               self.action = GameSystem.Method.Action.UNKNOWN

      if   str[1] == 'u': self.rote = GameSystem.Method.Rote.UP
      elif str[1] == 'd': self.rote = GameSystem.Method.Rote.DOWN
      elif str[1] == 'r': self.rote = GameSystem.Method.Rote.RIGHT
      elif str[1] == 'l': self.rote = GameSystem.Method.Rote.LEFT
      else:               self.rote = GameSystem.Method.Rote.UNKNOWN

    def get_rote_vector(self):
      #進行方向から位置情報を更新
      if    self.rote == GameSystem.Method.Rote.UP:    return [1, 0]
      elif  self.rote == GameSystem.Method.Rote.DOWN:  return [-1, 0]
      elif  self.rote == GameSystem.Method.Rote.RIGHT: return [0, 1]
      elif  self.rote == GameSystem.Method.Rote.LEFT : return [0, -1]
      else: return [0, 0]

  class AroundData:
    def __init__(self):
      self.data = [GameSystem.MapObject.NOTHING] * 9

    def to_string(self, field):
      #周辺情報を文字列に変換
      pass
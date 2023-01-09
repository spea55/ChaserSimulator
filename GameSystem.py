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

    action: Action
    rote: Rote

    def from_string(self, str: str):
      import GameSystem
      #コマンドをメソッドの配列に変換
      answer: GameSystem.Method
      if   str[0] == 'w': answer.action = self.Method.Action.WALK
      elif str[0] == 'l': answer.action = self.Method.Action.LOOK
      elif str[0] == 's': answer.action = self.Method.Action.SEARCH
      elif str[0] == 'p': answer.action = self.Method.Action.PUT
      else:               answer.action = self.Method.Action.UNKNOWN

      if   str[1] == 'u': answer.rote = self.Method.Rote.UP
      elif str[1] == 'd': answer.rote = self.Method.Rote.DOWN
      elif str[1] == 'r': answer.rote = self.Method.Rote.RIGHT
      elif str[1] == 'l': answer.rote = self.Method.Rote.LEFT
      else:               answer.rote = self.Method.Rote.UNKNOWN

      return answer

    def get_rote_vector(self):
      #進行方向から位置情報を更新
      if    self.Method.rote == self.Method.Rote.UP:    return [1, 0]
      elif  self.Method.rote == self.Method.Rote.DOWN:  return [-1, 0]
      elif  self.Method.rote == self.Method.Rote.RIGHT: return [0, 1]
      elif  self.Method.rote == self.Method.Rote.LEFT : return [0, -1]
      else: return [0, 0]

  class AroundData:
    import GameSystem

    data: list[GameSystem.Method]

    def to_string(self, field:list[int[int]]):
      #周辺情報を文字列に変換
      pass
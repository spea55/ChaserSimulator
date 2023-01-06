#from chaser_simulator.Map import Map
#from chaser_simulator.Action import Action
import Map
from enum import Enum
import Action

class GameSystem:
  def __init__(self):
    self.map = Map()
    self.action = Action()
    
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
  
  def gameStep(self, str: str):
    cmd = self.fromString(str)

  def getRoteVector(self):
    if    self.Method.rote == self.Method.Rote.UP:    return
    elif  self.Method.rote == self.Method.Rote.DOWN:  return
    elif  self.Method.rote == self.Method.Rote.RIGHT: return
    elif  self.Method.rote == self.Method.Rote.LEFT : return
    else: return
 
  def fromString(self, str: str):
    answer: self.Method
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
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from chaser_simulator.GameSystem import GameSystem
#import GameSystem

class GameBoard:
  height = 17
  width = 15

  def __init__(self):
    self.field = [[GameSystem.MapObject.NOTHING for i in range(GameBoard.width)] for j in range(GameBoard.height)]
    self.team_pos = np.array([1, 1])
    self.score: int = 0

    self.import_map()
    self.view_field()

  def import_map(self):
    #MapListからmapをランダムで読み込む
    self.field[0][0] = GameSystem.MapObject.BLOCK
    self.field[2][2] = GameSystem.MapObject.ITEM
    self.field[3][2] = GameSystem.MapObject.BLOCK

  def view_field(self):
    fig = plt.figure()
    ax = plt.axes()

    for i in range(GameBoard.height):
      for j in range(GameBoard.width):
        if self.field[i][j] == GameSystem.MapObject.NOTHING:
          ax.add_patch(patches.Rectangle(xy=(j, i), width=1.0, height=1.0, ec='k', fill=False))

        elif self.field[i][j] == GameSystem.MapObject.TARGET:
          ax.add_patch(patches.Rectangle(xy=(j, i), width=1.0, height=1.0, ec='r', fill=False))

        elif self.field[i][j] == GameSystem.MapObject.BLOCK:
          ax.add_patch(patches.Rectangle(xy=(j, i), width=1.0, height=1.0, fc='k', ec='k'))

        elif self.field[i][j] == GameSystem.MapObject.ITEM:
          ax.add_patch(patches.Circle(xy=(j+0.5 , i+0.5), radius=0.3, fc='b', ec='k'))

        if i == self.team_pos[0] and j == self.team_pos[1]: 
          ax.add_patch(patches.Rectangle(xy=(j, i), width=1.0, height=1.0, fc='b', ec='k'))

    plt.axis('scaled')
    ax.set_aspect('equal')

  def field_access_method(self, method): #それぞれの処理終了後に情報返す
    print("field_access_method called")
    if   method.action == GameSystem.Method.Action.PUT:
      pass
    elif method.action == GameSystem.Method.Action.LOOK:
      pass
    elif method.action == GameSystem.Method.Action.WALK:
      self.team_pos += method.get_rote_vector()
      #pick_item時の処理
      self.view_field()
      return self.field_access_around(self.team_pos)

    elif method.action == GameSystem.Method.Action.SEARCH:
      pass
    else: return

  def field_access(self, pos: list): 
    #場外
    if pos[0] < 0                or pos[1] < 0:               return GameSystem.MapObject.BLOCK
    if pos[0] > GameBoard.height or pos[1] > GameBoard.width: return GameSystem.MapObject.BLOCK

    #ターゲットの位置
    #通常マップオブジェクト
    return self.field[pos[0]][pos[1]]

  def field_access_around(self, center):
    around = GameSystem.AroundData()

    for i in range(9):
      around.data[i] = self.field_access([center[0] - int(i / 3) + 1, center[1] + int(i % 3) - 1])

    return around
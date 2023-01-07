import matplotlib.pyplot as plt
import matplotlib.patches as patches
from GameSystem import *
import MapList
import numpy as np

class GameBoard:
  def __init__(self):
    self.height = 17
    self.width = 15

    self.field = np.zeros([self.height, self.width])
    self.pos = np.zeros(2)
    self.score: int

  def import_map(self):
    #MapListからmapをランダムで読み込む
    self.fieid = []
    self.pos = []

  def view_field(self):
    fig = plt.figure()
    ax = plt.axes()

    for i in range(self.height):
      for j in range(self.width):
        if self.field[i][j] == GameSystem.MapObject.NOTHING:
          ax.add_patch(patches.Rectangle(xy=(j, i), width=1.0, height=1.0, ec='k', fill=False))

        elif self.field[i][j] == GameSystem.MapObject.TARGET:
          ax.add_patch(patches.Rectangle(xy=(j, i), width=1.0, height=1.0, ec='r', fill=False))

        elif self.field[i][j] == GameSystem.MapObject.BLOCK:
          ax.add_patch(patches.Rectangle(xy=(j, i), width=1.0, height=1.0, fc='k', ec='k'))

        elif self.field[i][j] == GameSystem.MapObject.ITEM:
          ax.add_patch(patches.Circle(xy=(j+0.5 , i+0.5), radius=0.3, fc='b', ec='k'))

        elif self.fieid[i][j] == [self.pos[0], self.pos[1]]:
          ax.add_patch(patches.Rectangle(xy=(j, i), width=1.0, height=1.0, fc='b', ec='k'))

    plt.axis('scaled')
    ax.set_aspect('equal')

  def field_access_method(self, method: GameSystem.Method): #それぞれの処理終了後に情報返す
    if   method.action == GameSystem.Method.Action.PUT:
      pass
    elif method.action == GameSystem.Method.Action.LOOK:
      pass
    elif method.action == GameSystem.Method.Action.WALK:
      self.pos += GameSystem.Method.get_rote_vector()
      #pick_item時の処理
    elif method.action == GameSystem.Method.Action.SEARCH:
      pass
    else: return GameSystem.around

  def field_access_around(self):
    pass
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from GameSystem import *
import MapList
import numpy as np

class Map:
  def __init__(self):
    self.height = 17
    self.width = 15

    sys = GameSystem()
    self.objects = sys.MapObjects()

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
        if self.field[i][j] == 0:
          ax.add_patch(patches.Rectangle(xy=(j, i), width=1.0, height=1.0, ec='k', fill=False))

        elif self.field[i][j] == self.objects.BLOCK:
          ax.add_patch(patches.Rectangle(xy=(j, i), width=1.0, height=1.0, fc='k', ec='k'))

        elif self.field[i][j] == self.objects.ITEM:
          ax.add_patch(patches.Circle(xy=(j+0.5 , i+0.5), radius=0.3, fc='b', ec='k'))

    plt.axis('scaled')
    ax.set_aspect('equal')

  def find_position(self, player_num: int):
    for i in range(self.height):
      for j in range(self.width):
        if self.field[i][j] == player_num:
          return [j, i]

    return []
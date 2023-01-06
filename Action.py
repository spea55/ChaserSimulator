
class Action:
  def __init__(self, field):
    self.field = field

  def get_ready(self, num):
    

    return self.field

  def walk_up(self):
    field = self.field
    for i in range(field.height):
      for j in range(field.width):
        if field.map_list[i][j] == self.num and i+1 != field.height:
          field.map_list[i][j] = 0
          field.map_list[i+1][j] = self.num
          return field
      
    return field

  def walk_left(self):
    field = self.field
    for i in range(field.height):
      for j in range(field.width):
        if field.map_list[i][j] == self.num and j-1 >= 0:
          field.map_list[i][j] = 0
          field.map_list[i][j-1] = self.num
          return field
      
    return field

  def walk_right(self):
    field = self.field
    for i in range(field.height):
      for j in range(field.width):
        if field.map_list[i][j] == self.num and j+1 != field.width:
          field.map_list[i][j] = 0
          field.map_list[i][j+1] = self.num
          return field
      
    return field

  def walk_left(self):
    field = self.field
    for i in range(field.height):
      for j in range(field.width):
        if field.map_list[i][j] == self.num and j-1 >= 0:
          field.map_list[i][j] = 0
          field.map_list[i][j-1] = self.num
          return field
      
    return field
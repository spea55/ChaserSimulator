import GameSystem

class CHaserSimulator:
  def __init__(self):
    self.system = GameSystem()

  def __game_step(self, str: str):
    getready_flag = True

    #getReady受け取り
    if getready_flag:
      #getReadyに対し、周辺情報を返す
      
      getready_flag = False

    #コマンド受け取り
    else: 
      #コマンドを文字列からメソッドに変換
      cmd = self.system.Method.from_string(str)

      #コマンド処理
      self.system.around = self.system.board.FieldAccessMethod()

      #情報を返す
      return self.system.around

  def get_ready(self):
    return self.__game_step("gr")

  def walk_up(self):
    return self.__game_step("wp")

  def walk_down(self):
    return self.__game_step("wd")

  def walk_left(self):
    return self.__game_step("wl")

  def walk_right(self):
    return self.__game_step("wr")

  def look_up(self):
    return self.__game_step("lu")

  def look_down(self):
    return self.__game_step("ld")

  def look_left(self):
    return self.__game_step("ll")

  def look_right(self):
    return self.__game_step("lr")

  def search_up(self):
    return self.__game_step("su")

  def search_down(self):
    return self.__game_step("sd")

  def search_left(self):
    return self.__game_step("sl")

  def search_right(self):
    return self.__game_step("sr")

  def put_up(self):
    return self.__game_step("pu")

  def put_down(self):
    return self.__game_step("pd")

  def put_left(self):
    return self.__game_step("pl")

  def put_right(self):
    return self.__game_step("pr")
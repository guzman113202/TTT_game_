board = [
  ["-", "-", "-"],
  ["-", "-", "-"],
  ["-", "-", "-"]
]

user = True # when true it refers to x, otherwise o
turns = 0



def Pboard(board):
  for row in board:
    for slot in row:
      print(f"{slot} ", end="")
    print()

def quit(player_inp):
  if player_inp.lower() == "q": 
    print("\n Thank you for playing! :)\n")
    return True
  else: return False

def check_inp(player_inp):
  if not check_num(player_inp): return False
  player_inp = int(player_inp)
  if not limits(player_inp): return False

  return True

def check_num(player_inp):
  if not player_inp.isnumeric(): 
    print("\nThis number cannot be used\n")
    return False
  else: return True

def limits(player_inp):
  if player_inp > 9 or player_inp < 1: 
    print("\nNumber is out of viable selections, please use 1-9\n")
    return False
  else: return True

def occupied(coords, board):
  row = coords[0]
  col = coords[1]
  if board[row][col] != "-":
    print("\nRetry selection, desired space is occupied\n")
    return True
  else: return False

def coordinates(player_inp):
  row = int(player_inp / 3)
  col = player_inp
  if col > 2: col = int(col % 3)
  return (row,col)

def draw_board(coords, board, active_user):
  row = coords[0]
  col = coords[1]
  board[row][col] = active_user

def player(user):
  if user: return "x"
  else: return "o"

def iswin(user, board):
  if check_row(user, board): return True
  if check_col(user, board): return True
  if check_diag(user, board): return True
  return False

def check_row(user, board):
  for row in board:
    complete_row = True
    for slot in row:
      if slot != user:
        complete_row = False
        break
    if complete_row: return True
  return False 

def check_col(user, board):
  for col in range(3):
    complete_col = True
    for row in range(3):
      if board[row][col] != user:
        complete_col = False
        break
    if complete_col: return True
  return False

def check_diag(user, board):
  if board[0][0] == user and board[1][1] == user and board[2][2] == user: return True
  elif board[0][2] == user and board[1][1] == user and board[2][0] == user: return True
  else: return False

while turns < 9:
  active_user = player(user)
  Pboard(board)
  player_inp = input("Please enter a position 1-9 (from top left to bottom right)\nor enter \"q\" to quit:")
  if quit(player_inp): break
  if not check_inp(player_inp):
    print("\nRetry")
    continue
  player_inp = int(player_inp) - 1
  coords = coordinates(player_inp)
  if occupied(coords, board):
    print("\nRetry")
    continue
  draw_board(coords, board, active_user)
  if iswin(active_user, board): 
    print(f"{active_user.upper()} won!, congratulations!!!")
    break
  
  turns += 1
  if turns == 9: print("Tie! womp womp woOoOoOoOomp\nTry again!")
  user = not user

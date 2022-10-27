
board=[]
def init_board():
   global board
   board = list(range(1,10))

def draw_board(board):
   result="-" * 13+'\n'
   for i in range(3):
           result+="| "+str(board[0+i*3])+" | "+str(board[1+i*3])+" | "+str(board[2+i*3])+" | "+'\n'
           result+="-" * 13+'\n'
   return result


def tk_in(pl_token,pl_answer):
   if (str(board[pl_answer-1]) not in "XO"):
      board[pl_answer-1] = pl_token
      return True
   else: return None

def check_win():
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False


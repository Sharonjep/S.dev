#tic tac toe game
#design of tic tac toe game
play_board = [
  [' ' ,' ' ,' '],
  [' ' ,' ' ,' '],
  [' ' ,' ' ,' ']
]

#the choices
X_CHOICE = 'X'
O_CHOICE = 'O'

#prints the board
def print_board():
  for i in range(3):
    for j in range(3):
      print("[" + play_board[i][j] +"]", end="")#print elements without new line
    print()#print empty line after each row
  print('--------------')

def play_at_position( row , col, player ):
  if play_board[row][col] == ' ':
    play_board[row][col] = player.upper()#returns in uppercase
    print_board()
  else:
    print("Position is not empty")

def get_at_position(row, col):
  return play_board[row][col]

def get_winner():
  #check win first row
  if get_at_position(0,0) != ' ' and get_at_position(0,0) == get_at_position(0,1) == get_at_position(0,2):
    if get_at_position(0,0) == X_CHOICE:
      return X_CHOICE
    elif get_at_position(0,0) == O_CHOICE:
      return O_CHOICE
  #check win second row
  if get_at_position(1,0) != ' ' and get_at_position(1,0) == get_at_position(1,1) == get_at_position(1,2):
    if get_at_position(1,0) == X_CHOICE:
        return X_CHOICE
    elif get_at_position(1,0) == O_CHOICE:
        return O_CHOICE
  
  #check win third row
  if get_at_position(2,0) != ' ' and get_at_position(2,0) == get_at_position(2,1) == get_at_position(2,2):
    if get_at_position(2,0) == X_CHOICE:
        return X_CHOICE
    elif get_at_position(2,0) == O_CHOICE:
        return O_CHOICE

  #check win first column
  if get_at_position(0,0) != ' ' and get_at_position(0,0) == get_at_position(1,0) == get_at_position(2,0):
    if get_at_position(0,0) == X_CHOICE:
      return X_CHOICE
    elif get_at_position(0,0) == O_CHOICE:
      return O_CHOICE
  
  #check win second column
  if get_at_position(0,1) != ' ' and get_at_position(0,1) == get_at_position(1,1) == get_at_position(2,1):
    if get_at_position(0,1) == X_CHOICE:
      return X_CHOICE
    elif get_at_position(0,1) == O_CHOICE:
      return O_CHOICE
  
  #check win third column
  if get_at_position(0,2) != ' ' and get_at_position(0,2) == get_at_position(1,2) == get_at_position(2,2):
    if get_at_position(0,2) == X_CHOICE:
      return X_CHOICE
    elif get_at_position(0,2) == O_CHOICE:
      return O_CHOICE

  #check diagonal one
  if get_at_position(0,0) != ' ' and get_at_position(0,0) == get_at_position(1,1) == get_at_position(2,2):
    if get_at_position(0,0) == X_CHOICE:
      return X_CHOICE
    elif get_at_position(0,0) == O_CHOICE:
      return O_CHOICE

  #check diagonal two
  if get_at_position(0,2) != ' ' and get_at_position(0,2) == get_at_position(1,1) == get_at_position(2,0):
    if get_at_position(0,2) == X_CHOICE:
      return X_CHOICE
    elif get_at_position(0,2) == O_CHOICE:
      return O_CHOICE

  else:
    return None;

def is_board_full():
  for i in range(3):
    for j in range(3):
      if play_board[i][j] == ' ':
        return False
  return True


def clear_board():
  for i in range(3):
    for j in range(3):
      play_board[i][j]= ' '

#game

X_CHOICE = 'X'
O_CHOICE = 'O'

game_list = []

while True:
  clear_board()
  print()
  print("1. New Game")
  print("2. Previous Games")
  print("3. Exit")

  choice = int(input("\nEnter a choice: "))

  if choice == 2:
    print()
    print("--------------------------")
    for game in game_list:
      print(game)
    print("--------------------------")
    print()
   
    continue
  elif choice == 3:
    break;
  

  player1_name = input("Player 1's name: ")
  player2_name = input("Player 2's name: ")
  
  
  player1_choice = input(f"{player1_name}, Choose 'X' or 'O': ")
  player1_choice = player1_choice.upper()
  
  #set player 2 choice based on player one's choice
  if player1_choice == X_CHOICE:
    player2_choice = O_CHOICE
  else:
    player1_choice = O_CHOICE
    player2_choice = X_CHOICE
  
  
  print("----------------------")
  print("Welcome to Tic Tac Toe")
  print(f"\n{player1_name} plays as '{player1_choice}'and {player2_name} play as '{player2_choice}'. Lets play!\n")
  
  
  
  while True:  
    #Player 1 turn
    player1_play_position   = input(player1_name + ", enter a position to play at (i.e., 1,1) ")
    player1_pos_row = int(player1_play_position.split(",")[0])
    player1_pos_col = int(player1_play_position.split(",")[1])
    
    play_at_position (player1_pos_row , player1_pos_col , player1_choice)
  
    winner = get_winner()
    #print("Winner", winner)
    if winner == player1_choice:
      print(f"{player1_name} wins!")
      game_list.append(f"{player1_name} X {player2_name} - {player1_name} won!")
      break
      
    #Player 2 turn
    player2_play_position   = input(player2_name + ", enter a position to play at (i.e., 1,1) ")
    player2_pos_row = int(player2_play_position.split(",")[0])
    player2_pos_col = int(player2_play_position.split(",")[1])
    
    play_at_position (player2_pos_row , player2_pos_col , player2_choice)
    
    winner = get_winner()
    #print("Winner", winner)
    if winner == player2_choice:
      print(f"{player2_name} wins!")
      game_list.append(f"{player1_name} X  {player2_name} - {player2_name} won!")
      break
  
    if is_board_full():
      print("Draw!")
      game_list.append(f"{player1_name} VS.  {player2_name}. Draw!")

      break

# A board with notation for each board positions
positionsFormat = [
    ['tl','tc','tr'], 
    ['ml','mc','mr'], 
    ['bl','bc','br']
]

# Create a board for gameplay, initially empty (containing '-')
gameBoard = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

# Valid positions
valid_positions = ['tl', 'tc', 'tr', 'ml', 'mc', 'mr', 'bl', 'bc', 'br']

# Filled positions
filled_positions = []

# Position to mark mapping
position2Mark = {
    'tl': 'gameBoard[0][0]', 'tc': 'gameBoard[0][1]', 'tr': 'gameBoard[0][2]',
    'ml': 'gameBoard[1][0]', 'mc': 'gameBoard[1][1]', 'mr': 'gameBoard[1][2]',
    'bl': 'gameBoard[2][0]', 'bc': 'gameBoard[2][1]', 'br': 'gameBoard[2][2]'
}

# Initialize winner, intially no one is winner
winner = None

# Initialize variable to store won/lost status, initially winner is not decided
winner_decided = False

# Initialize variable to store direction along which correct pattern is obtained, initially none
direction = None

# Set default mark with which game starts as 'X'
mark = 'O'

# A function that takes the board (a dictionary) as argument and display it in formatted way
def displayBoard(board):
    count = 0
    for row_elements in board:
        row = ' | '.join(row_elements)
        print(row.center(78))
        
        if count == 2:
            break
        count += 1
        
        if board == positionsFormat:
            print('---+----+---'.center(78))
        else:
            print('--+---+--'.center(78))
    print('\n')
    
def getPosition():
    global mark
    global position
    
    # Swap mark and take position to set each mark.
    if mark == 'X':
        position = input("Enter the position to place 'O': ")
        mark = 'O'
    elif mark == 'O':
        position = input("Enter the position to place 'X': ")
        mark = 'X'
    return position

def correctPosition(position):
    if position in valid_positions:
        return True
    else:
        return False
    
def availablePosition(position):
    if position not in filled_positions:
        return True
    else:
        return False

def getCurrentMark(position):
    global gameBoard
    exec('%s = %s' % ('curr_mark', position2Mark[position]))
    return curr_mark

def reset():
    global winner
    global winner_decided
    global gameBoard
    global filled_positions
    
    gameBoard.clear()
    for i in range(3):
        gameBoard.append([' ', ' ', ' '])
        
    filled_positions.clear()
    
    winner = None
    winner_decided = False
    
def setMark(position):
    global gameBoard
    exec("%s = %s" % (position2Mark[position],'mark'))
    filled_positions.append(position)
    
def decideWinner():
    global winner_decided
    global winner
    global direction
    
    winning_patterns = ['XXX', 'OOO']
    
    # Check row-wise patterns
    for row in gameBoard:
        rpattern = ''.join(row)
        if rpattern in winning_patterns:
            winner = rpattern[0]
            direction = 'row-wise'
            
    # Check column-wise patterns
    col = 0
    cpattern = ''
    while col <= 2:
        for row in range(3):
            cpattern += gameBoard[row][col]
        if cpattern in winning_patterns:
            winner = cpattern[0]
            direction = 'column-wise'
        col += 1
        cpattern = ''
        
    # Check diagonal-wise patterns
    dpattern1 = gameBoard[0][0] + gameBoard[1][1] + gameBoard[2][2]
    dpattern2 = gameBoard[2][0] + gameBoard[1][1] + gameBoard[0][2]
    if dpattern1 in winning_patterns:
        winner = dpattern1[0]
        direction = 'diagonal-wise'
    elif dpattern2 in winning_patterns:
        winner = dpattern2[0]
        direction = 'diagonal-wise'
        
    # Modify winner decided flag
    if winner:
        winner_decided = True

def askPlayerName():
    global x_player
    global y_player
    x_player = input("Enter player name for 'X' mark: ")
    y_player = input("Enter player name for 'O' mark: ")
    
def winnerName():
    if winner == 'X':
        winner_name = x_player.title()
    elif winner == 'O':
        winner_name = y_player.title()
    return winner_name

def swapMark():
    global mark
    if mark == 'X':
        mark = 'O'
    elif mark == 'O':
        mark = 'X'
        
def main():
    """Main function for the game."""
    global mark
    global winner_decided
    
    # Display the board each time a player sets a mark on a position to show the user the updated board
    displayBoard(gameBoard)
    
    # Get position to set the mark
    position = getPosition()
    
    # Set mark if entered position is correct and available
    if correctPosition(position):
        if availablePosition(position):
            setMark(position)
        else:
            print("The position is already filled, select another.\n")
            swapMark()
        if len(filled_positions) == 9 and winner_decided == False:
            winner_decided = 'draw'
    else:
        print("Wrong position please enter any one from specified positions.\n")
        swapMark()

# Main loop (Game loop)
while True:
    # Show Game Title
    print('\n------------------------------------------------------------------------------------------------------------------------\n')
    print('                                                                                                           ')
    print('    %%%%%%%%%%   %%%%%%%%        %%         %%%%%%%%%%      %%            %%         %%%%%%%%%%      %%       %%%%%%%%%')
    print('    %%%%%%%%%%   %%%%%%%%      %%           %%%%%%%%%%     %% %%        %%           %%%%%%%%%%    %%  %%    %%%%%%%%% ')
    print('        %%          %%       %%                 %%        %%   %%     %%                 %%       %%    %%   %%        ')
    print('        %%          %%      %%                  %%       %%     %%   %%                  %%      %%      %%  % %%%%    ')
    print('        %%          %%      %%                  %%      %%%%%%%%%%%  %%                  %%      %%      %%  % %%%%    ')
    print('        %%          %%       %%                 %%      %%%%%%%%%%%   %%                 %%      %%      %%  %%        ')
    print('        %%       %%%%%%%%      %%               %%      %%       %%     %%               %%       %%    %%   %%%%%%%%% ')
    print('        %%       %%%%%%%%        %%             %%      %%       %%       %%             %%         %%%%      %%%%%%%%%')
    print('\n------------------------------------------------------------------------------------------------------------------------\n')

    print()
    
    replay_decision = input("Enter play/quit to start/stop playing: ")
    if replay_decision.lower() == 'quit':
        break
        
    reset()
    
    askPlayerName()
    
    # Display notation containing board
    print('\n--------------------------------------------------------------------------------------\n')
    print("Instruction:\n\tBelow is structural representation of positions on board.\n\tPlease, keep in mind the notation for each position to use while playing.\n--------------------------------------------------------------------------------------")
    displayBoard(positionsFormat)
    print('\n--------------------------------------------------------------------------------------\n')
    
    print("Game Started. Enjoy playing...\n")
    
    while True:
        main()
        decideWinner()
        if winner_decided == True:
            displayBoard(gameBoard)
            print(f"'{winner}' matched {direction}.\n{winnerName()} won!\n")
            break
        elif winner_decided == 'draw':
            displayBoard(gameBoard)
            print("No more positions are available.\nGame draw!")
            break
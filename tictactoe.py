from IPython.display import clear_output
import random

# PRINTS OUT BOARD AS A NUMPAD
def display_board( board ):
	print( "   |   |  " )
	print( f" { board[ 7 ] } | { board[ 8 ] } | { board[ 9 ] } " )
	print( "   |   |  " )
	print( "-----------" )
	print( "   |   |  " )
	print( f" { board[ 4 ] } | { board[ 5 ] } | { board[ 6 ] } " )
	print( "   |   |  " )
	print( "-----------" )
	print( "   |   |  " )
	print( f" { board[ 1 ] } | { board[ 2 ] } | { board[ 3 ] } " )
	print( "   |   |  " )

# TAKES IN A PLAYER INPUT AND ASSIGNS THEIR MARKER AS 'X' OR 'O'
def player_input():
    player1_marker = ''
    while player1_marker != 'X' or player1_marker != 'O':
        player1_marker = input('Player 1: Do you want to be X or O? ')
        if player1_marker == 'X' or player1_marker == 'O':
            break
        print( "Invalid input, please pick 'X' or 'O'." )
    return player1_marker

# ASSIGNS MARKER TO POSITION ON THE BOARD
def place_marker( board, marker, position ):
	board[ position ] = marker

# CHECKS TO SEE IF THE MARKER HAS WON
def win_check(board, mark):
    # HORIZONTAL WINNING COMBINATIONS
    if board[ 7 ] == mark and board[ 8 ] == mark and board[ 9 ] == mark:
        return True
    elif board[ 4 ] == mark and board[ 5 ] == mark and board[ 6 ] == mark:
        return True
    elif board[ 1 ] == mark and board[ 2 ] == mark and board[ 3 ] == mark:
        return True
    # VERTICAL WINNING COMBINATIONS
    elif board[ 1 ] == mark and board[ 4 ] == mark and board[ 7 ] == mark:
        return True
    elif board[ 2 ] == mark and board[ 5 ] == mark and board[ 8 ] == mark:
        return True
    elif board[ 3 ] == mark and board[ 6 ] == mark and board[ 9 ] == mark:
        return True
    # DIAGONAL WINNING COMBINATIONS
    elif board[ 7 ] == mark and board[ 5 ] == mark and board[ 3 ] == mark:
        return True
    elif board[ 9 ] == mark and board[ 5 ] == mark and board[ 1 ] == mark:
        return True
    else:
        return False

# RANDOMLY DECIDES WHICH PLAYER TO GO FIRST
def choose_first():
	first = random.randint( 1, 2 )
	print( f'Player { first } will go first.' )
	return first

# CHECKS IF A SPACE ON THE BOARD IS FREELY AVAILABLE
def space_check( board, position ):
	return board[ position ] == ' '

# CHECKS IF THE BOARD IS FULL
def full_board_check( board ):
	index = 0
	for item in board:
		if board[ index ] == ' ':
			return False
		index += 1
	return True

# ASKS FOR PLAYER'S NEXT POSITION AND CHECKS IF IT IS AVAILABLE
def player_choice( board ):
    valid_position = False
    position = 0
    while not valid_position:
        try:
            position = int( input( "Choose your next position: (1-9) " ) )
            if position < 1 or position > 9:
                print( "Invalid input, please pick a position 1-9.")
            else:
            	# CHECK IF THAT POSITION IS AVAILABLE
                if space_check( board, position ):
                    valid_position = True
                    return position
                else:
                    print( "That position is filled, please try again." )
        except:
            print( "Invalid input, please pick a position 1-9." )
    return position

# ASKS PLAYER IF THEY WANT TO PLAY AGAIN
def replay():
	restart = input( "Do you want to play again? Enter Yes or No: " )
	return restart == 'Yes'

# WHAT TAKES PLACE DURING EACH PLAYER'S TURN
def control_flow( board, mark ):
	while True:
		if full_board_check( board ):
			print( 'ITS A TIE' )
			return 1
		print( '\n' )
		position = player_choice( board )
		place_marker( board, mark, position )
		if win_check( board, mark ):
			print( '\n' * 100 )
			display_board( board )
			print( 'Congratulations! You have won the game!' )
			return 1
		print( '\n' * 100 )
		display_board( board )
		break

### MAIN CONTROL FLOW OF THE GAME ###
print( 'Welcome to Tic Tac Toe!' )
while True:
    # SETTING UP THE GAME UP HERE
    board = [ '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ]
    player2_mark = ''
    player1_mark = player_input()
    # ASSIGNING PLAYER MARKS
    if player1_mark == "X":
    	player2_mark = 'O'
    else:
    	player2_mark = 'X'
    # DECIDING WHO GOES FIRST
    first_player = choose_first()
    player1_turn = False
    player2_turn = False
    if first_player == 1:
    	player1_turn = True
    else:
    	player2_turn = True
    ready = input( "Are you ready to play? Enter Yes or No: " )
    # GAME HAS BEGUN
    while ready == 'Yes':
    	print( '\n' * 100 )
    	display_board( board )
    	# PLAYER ONE'S TURN
    	if player1_turn:
    		if control_flow( board, player1_mark ) == 1:
    			break
    		player1_turn = False
    		player2_turn = True
    	# PLAYER TWO'S TURN
    	if player2_turn:
    		if control_flow( board, player2_mark ) == 1:
    			break
    		player2_turn = False
    		player1_turn = True
    # CHECK TO RESTART THE GAME
    if not replay():
    	break

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

### MAIN CONTROL FLOW OF THE GAME ###
print('Welcome to Tic Tac Toe!')
while True:
    # SET THE GAME UP HERE
    board = [ '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ]
    player1_mark = ''
    player2_mark = ''
    player1_mark = player_input()
    # print( f'Player 1 Mark: {player1_mark}' )
    if player1_mark == "X":
    	player2_mark = 'O'
    else:
    	player2_mark = 'X'
    # print( f'Player 2 Mark: {player2_mark}' )
    first_player = choose_first()
    player1_turn = False
    player2_turn = False
    if first_player == 1:
    	player1_turn = True
    else:
    	player2_turn = True
    print( '\n' )
    ready = input( "Are you ready to play? Enter Yes or No: " )
    print( '\n' )
    while ready == 'Yes':
    	display_board( board )
    	# PLAYER ONE TURN
    	if player1_turn:
    		if full_board_check( board ):
    			print( 'ITS A TIE' )
    			break
    		print( '\n' )
    		player1_position = player_choice( board )
    		place_marker( board, player1_mark, player1_position )
    		if win_check( board, player1_mark ):
    			print( '\n' )
    			display_board( board )
    			print( '\n' )
    			print( 'PLAYER ONE WINS' )
    			break
    		print( '\n' )
    		display_board( board )
    		print( '\n' )
    		player1_turn = False
    		player2_turn = True
    	if player2_turn:
    		if full_board_check( board ):
    			print( 'ITS A TIE' )
    			break
    		print( '\n' )
    		player2_position = player_choice( board )
    		place_marker( board, player2_mark, player2_position )
    		if win_check( board, player2_mark ):
    			print( '\n' )
    			display_board( board )
    			print( '\n' )
    			print( 'PLAYER TWO WINS' )
    			break
    		print( '\n' )
    		player2_turn = False
    		player1_turn = True
    if not replay():
    	break

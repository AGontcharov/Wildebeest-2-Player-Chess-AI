#!/usr/bin/python

import Constants
import fileinput
import copy
import math
import sys

# Generate all the posssible states of the given board.
def succesor(board, player):
	boards = []

	# Get the pieces from the top left of the board.
	for row, line in enumerate(board):
		for col, piece in enumerate(line):

			# Skip over black pieces.
			if player == 'W':
				if piece in Constants.BLACK:
					continue

			# Skip over white pieces.
			elif player == 'B':
				if piece in Constants.WHITE:
					continue

			# Check if the piece is paralyzed by the Beekeeper.
			if paralyzed(row, col, piece, board):
				continue

			# Rook
			if piece.lower() == 'r':
				boards.append(rookMove(row, col, piece, board))

			# Knight
			elif piece.lower() == 'n':
				boards.append(knightMove(row, col, piece, board))

			# Beekeeper
			elif piece.lower() == 'z':
				boards.append(kingMove(row, col, piece, board))

			# Bishop
			elif piece.lower() == 'b':
				boards.append(bishopMove(row, col, piece, board))

			# old Woman
			elif piece.lower() == 'o':
				boards.append(kingMove(row, col, piece, board))

			# Grand Empress
			elif piece.lower() == 'e':
				boards.append(rookMove(row, col, piece, board))
				boards.append(bishopMove(row, col, piece, board))
				boards.append(knightMove(row, col, piece, board))

			# King
			elif piece.lower() == 'k':
				boards.append(kingMove(row, col, piece, board))

			# King with a Jet Pack
			elif piece.lower() == 'w':
				boards.append(bishopMove(row, col, piece, board))

			# Golf Cart
			elif piece.lower() == 'x':
				boards.append(golfCart(row, col, piece, board))

			# Catapult
			elif piece.lower() == 'c':
				boards.append(serpentMove(row, col, piece, board))
				boards.append(catapultMove(row, col, piece, board))

			# Gorilla
			elif piece.lower() == 'g':
				boards.append(serpentMove(row, col, piece, board))
				boards.append(gorillaMove(row, col, piece, board))

			# Pawn
			elif piece.lower() == 'p':
				boards.append(pawnMove(row, col, piece, board))

			# Serpent
			elif piece.lower() == 's':
				boards.append(serpentMove(row, col, piece, board))

			# Prince Joey
			elif piece.lower() == 'j':
				boards.append(kingMove(row, col, piece, board))

	return boards

# Check if a piece is paralyzed by an opposing Beekeeper.
def paralyzed(y, x, id, state):
	
	# White piece
	if id in Constants.WHITE:
		beekeeper = 'z'
	# Black piece
	else:
		beekeeper = 'Z'

	# Generate adjacent moves for an opposing Beekeeper
	for i in range(-1, 2):
		for j in range(-1, 2):

			# Skip over current location
			if i == 0 and j == 0:
				continue;

			if 0 <= y + i < 11 and 0 <= x + j < 11 and state[y + i][x + j] == beekeeper:
				return True

	return False

# Generate all the possible moves for a Pawn
def pawnMove(y, x, id, state):
	results = []

	# White
	if id in Constants.WHITE:

		# Move one down
		if y + 1 < 11:
			if state[y + 1][x] in Constants.NEUTRAL:
				newState = copy.deepcopy(state)
				newState[y][x] = '.'
				newState[y + 1][x] = id
				results.append(newState)

		# Move two down
		if y == 1 and state[y + 1][x] in Constants.NEUTRAL and state[y + 2][x] in Constants.NEUTRAL:
			newState = copy.deepcopy(state)
			newState[y][x] = '.'
			newState[y + 2][x] = id
			results.append(newState)

		# Capture
		for i in range(-1, 2):

			# Skip over current location
			if i == 0:
				continue

			if y + 1 >= 0 and 0 <= x + i < 11 and state[y + 1][x + i] in Constants.BLACK and state[y + 1][x + i] is not 'g':
				newState = copy.deepcopy(state)
				newState[y][x] = '.'
				newState[y + 1][x + i] = id
				results.append(newState)

	# Black
	else:

		# Move one up
		if y - 1 >= 0:
			if state[y - 1][x] in Constants.NEUTRAL:
				newState = copy.deepcopy(state)
				newState[y][x] = '.'
				newState[y - 1][x] = id
				results.append(newState)

		# Move two up
		if y == 9 and state[y - 1][x] in Constants.NEUTRAL and state[y - 2][x] in Constants.NEUTRAL:
			newState = copy.deepcopy(state)
			newState[y][x] = '.'
			newState[y - 2][x] = id
			results.append(newState)

		# Capture
		for i in range(-1, 2):

			# Skip over current location
			if i == 0:
				continue

			if y - 1 >= 0 and 0 <= x + i < 11 and state[y - 1][x + i] in Constants.WHITE and state[y - 1][x + i] is not 'G':
				newState = copy.deepcopy(state)
				newState[y][x] = '.'
				newState[y - 1][x + i] = id
				results.append(newState)

	return results

# Generate all the possible moves for a Knight
def knightMove(y, x, id, state):
	results = []

	# Cannot capture opposing Gorilla
	if id in Constants.WHITE:
		friendlyPieces = copy.deepcopy(Constants.WHITE)
		friendlyPieces.add('g')
	else:
		friendlyPieces = copy.deepcopy(Constants.BLACK)
		friendlyPieces.add('G')

	# Generate L shape moves for Knight
	for i in range(-2, 3):
		for j in range(-2, 3):
			
			# Skip over invalid moves
			if i == 0 or j == 0 or (i + j) % 2 == 0:
				continue

			# Check boundary
			if 0 <= y + i < 11 and 0 <= x + j < 11 and state[y + i][x + j] not in friendlyPieces:
				newState = copy.deepcopy(state)
				newState[y][x] = '.'
				newState[y + i][x + j] = id
				results.append(newState)

	return results

# Generate all the possible moves for a Bishop
def bishopMove(y, x, id, state):
	results = []
	upLeft, upRight, downLeft, downRight = True, True, True, True

	# Cannot capture opposing Gorilla
	if id in Constants.WHITE:
		friendlyPieces = copy.deepcopy(Constants.WHITE)
		friendlyPieces.add('g')
	else:
		friendlyPieces = copy.deepcopy(Constants.BLACK)
		friendlyPieces.add('G')

	# Generate current and diagonal moves for Bishop
	for i in range(1, 11):

		# Skip over current location
		if i == 0:
			continue;

		# Slide diagonaly up left
		if y - i >= 0 and x - i >= 0 and state[y - i][x - i] not in friendlyPieces and upLeft:
			newState = copy.deepcopy(state)
			newState[y][x] = '.'
			newState[y - i][x - i] = id
			results.append(newState)

			# Stop after capturing a piece.
			if state[y - i][x - i] not in Constants.NEUTRAL:
				upLeft = False
		else:
			upLeft = False

		# Slide diagonaly up right
		if y - i >= 0 and x + i < 11 and state[y - i][x + i] not in friendlyPieces and upRight:
			newState = copy.deepcopy(state)
			newState[y][x] = '.'
			newState[y - i][x + i] = id
			results.append(newState)

			# Stop after capturing a piece.
			if state[y - i][x + i] not in Constants.NEUTRAL:
				upRight = False
		else:
			upRight = False

		# Slide diagonaly down left
		if y + i < 11 and x - i >= 0 and state[y + i][x - i] not in friendlyPieces and downLeft:
			newState = copy.deepcopy(state)
			newState[y][x] = '.'
			newState[y + i][x - i] = id
			results.append(newState)

			# Stop after capturing a piece.
			if state[y + i][x - i] not in Constants.NEUTRAL:
				downLeft = False
		else:
			downLeft = False

		# Slide diagonaly down right
		if y + i < 11 and x + i < 11 and state[y + i][x + i] not in friendlyPieces and downRight:
			newState = copy.deepcopy(state)
			newState[y][x] = '.'
			newState[y + i][x + i] = id
			results.append(newState)

			# Stop after capturing a piece.
			if state[y + i][x + i] not in Constants.NEUTRAL:
				downRight = False
		else:
			downRight = False

	return results

# Generate all the possible moves for a Rook
def rookMove(y, x, id, state):
	results = []
	left, right, up, down = True, True, True, True

	# Cannot capture opposing Gorilla
	if id in Constants.WHITE:
		friendlyPieces = copy.deepcopy(Constants.WHITE)
		friendlyPieces.add('g')
	else:
		friendlyPieces = copy.deepcopy(Constants.BLACK)
		friendlyPieces.add('G')

	# Generate cross moves for Rook
	for i in range(1, 11):

		# Slide left
		if x - i >= 0 and state[y][x - i] not in friendlyPieces and left:
			newState = copy.deepcopy(state)
			newState[y][x] = '.'
			newState[y][x - i] = id
			results.append(newState)

			# Stop after capturing a piece.
			if state[y][x - i] not in Constants.NEUTRAL:
				left = False
		else:
			left = False

		# Slide right
		if x + i < 11 and state[y][x + i] not in friendlyPieces and right:
			newState = copy.deepcopy(state)
			newState[y][x] = '.'
			newState[y][x + i] = id
			results.append(newState)

			# Stop after capturing a piece.
			if state[y][x + i] not in Constants.NEUTRAL:
				right = False
		else:
			right = False

		# Slide up
		if y - i >= 0 and state[y - i][x] not in friendlyPieces and up:
			newState = copy.deepcopy(state)
			newState[y][x] = '.'
			newState[y - i][x] = id
			results.append(newState)

			# Stop after capturing a piece.
			if state[y - i][x ] not in Constants.NEUTRAL:
				up = False
		else:
			up = False

		# Slide down
		if y + i < 11 and state[y + i][x] not in friendlyPieces and down:
			newState = copy.deepcopy(state)
			newState[y][x] = '.'
			newState[y + i][x] = id
			results.append(newState)

			# Stop after capturing a piece.
			if state[y + i][x] not in Constants.NEUTRAL:
				down = False
		else:
			down = False

	return results

# Generate all the possible moves for "King" like pieces
def kingMove(y, x, id, state):
	results = []

	# Cannot capture opposing Gorilla
	if id in Constants.WHITE:
		friendlyPieces = copy.deepcopy(Constants.WHITE)
		friendlyPieces.add('g')
	else:
		friendlyPieces = copy.deepcopy(Constants.BLACK)
		friendlyPieces.add('G')

	# Generate current and adjacent moves of the king
	for i in range(-1, 2):
		for j in range(-1, 2):
		
			# Skip over current location
			if i == 0 and j == 0:
				continue

			if 0 <= y + i < 11 and 0 <= x + j < 11 and state[y + i][x + j] not in friendlyPieces:
				newState = copy.deepcopy(state)
				newState[y][x] = '.'
				newState[y + i][x + j] = id
				results.append(newState)

	return results

# Generate all the possible moves for a Golf Cart
def golfCart(y, x, id, state):
	results = []

	# Cannot capture opposing Gorilla
	if id in Constants.WHITE:
		friendlyPieces = copy.deepcopy(Constants.WHITE)
		friendlyPieces.add('g')
	else:
		friendlyPieces = copy.deepcopy(Constants.BLACK)
		friendlyPieces.add('G')
	
	# Generate horizontal moves of the Golf Cart
	for i in range(-1, 2, 2):

		if 0 <= x + i < 11 and state[y][x + i] not in friendlyPieces:
			newState = copy.deepcopy(state)
			newState[y][x] = '.'
			newState[y][x + i] = id
			results.append(newState)

	return results

# Generate all the possible moves for a "Serpent" like pieces
def serpentMove(y, x, id, state):
	results = []

	# Generate current and adjacent moves of the Serpent
	for i in range(-1, 2):
		for j in range(-1, 2):
		
			# Skip over current location
			if i == 0 and j == 0:
				continue

			if 0 <= y + i < 11 and 0 <= x + j < 11 and state[y + i][x + j] in Constants.NEUTRAL:
				newState = copy.deepcopy(state)
				newState[y][x] = '.'
				newState[y + i][x + j] = id
				results.append(newState)

	return results

# Generate all the possible moves for a Gorilla
def gorillaMove(y, x, id, state):
	results = []

	#Gorillas cannot push each other
	unpushablePieces = copy.deepcopy(Constants.NEUTRAL)
	unpushablePieces.add('G')
	unpushablePieces.add('g')

	# Generate current and adjacent moves
	for i in range(-1, 2):
		for j in range(-1, 2):
		
			# Skip over current location
			if i == 0 and j == 0:
				continue

			# Get a friendly piece
			if 0 <= y + i < 11 and 0 <= x + j < 11 and state[y + i][x + j] not in unpushablePieces:
				pushedPiece = state[y + i][x + j]

				# Boundary check
				if y + i * 2 > 10 or y + i * 2 < 0 or x + j * 2 > 10 or x + j * 2 < 0:
					continue

				# Create the resultant board
				if state[y + i * 2][x + j * 2] not in "gG":
					newState = copy.deepcopy(state)
					newState[y][x] = '.'
					newState[y + i][x + j] = id
					newState[y + i * 2][x + j * 2] = pushedPiece
					results.append(newState)

	return results

# Generate all the possible moves for a Catapault
def catapultMove(y, x, id, state):
	results = []

	if id in Constants.WHITE:
		friendlyPieces = copy.deepcopy(Constants.WHITE)

		# Cannot fling Time Machine or Golf Cart
		throwablePieces = copy.deepcopy(Constants.WHITE)
		throwablePieces.remove('H')
		throwablePieces.remove('X');
	else:
		friendlyPieces = copy.deepcopy(Constants.BLACK)

		# Cannot fling Time Machine or Golf Cart
		throwablePieces = copy.deepcopy(Constants.BLACK)
		throwablePieces.remove('h')
		throwablePieces.remove('x');

	# Generate current and adjacent moves
	for i in range(-1, 2):
		for j in range(-1, 2):
		
			# Skip over current location
			if i == 0 and j == 0:
				continue

			# Get a friendly piece
			if 0 <= y + i < 11 and 0 <= x + j < 11 and state[y + i][x + j] in throwablePieces:
				flingedPiece = state[y + i][x + j]

				for k in range(1, 11):

					# Boundary check
					if y + i * -k > 10 or y + i * -k < 0 or x + j * -k > 10 or x + j * -k < 0:
						continue

					# Create the resultant board
					if state[y + i * -k][x + j * -k] not in "KkGg" and state[y + i * -k][x + j * -k] not in friendlyPieces:
						newState = copy.deepcopy(state)
						newState[y + i][x + j] = '.'
						newState[y + i * -k][x + j * -k] = flingedPiece
						results.append(newState)

	return results

# Update the state of the board when a Golf Cart is charged
def chargedGolfCart(board, whiteCharged, blackCharged):
	golfCart = []
	destroy = -1

	# Go through the top row 
	for x, piece in enumerate(board[0]):

		# Get only Charged Golf Cart
		if piece in "X" and whiteCharged or piece in "x" and blackCharged:
			golfCart.append((0, x, piece))

	# Go through the bottom row 
	for x, piece in enumerate(board[10]):

		# Get only Charged Golf Cart
		if piece in "X" and whiteCharged or piece in "x" and blackCharged:
			golfCart.append((10, x, piece))

	# List not empty
	while golfCart:
		y, x, piece = golfCart.pop(0)

		# Charged Black Golf Cart
		if piece == 'x':

			# Top row
			if y == 0:

				# Both Golf Carts charged
				if board[10][x] == 'X' and whiteCharged:
					destroy = x

				# Move Black's Golf Cart to bottom row
				else:
					for i in range(0, 10):
						board[i][x] = '.'
						board[10][x] = 'x'

			# Bottom row
			else:

				# Both Golf Carts charged
				if board[0][x] == 'X' and whiteCharged:
					destroy = x

				# Move Black's Golf Cart to top row
				else:
					for i in range(10, 0, -1):
						board[i][x] = '.'
						board[0][x] = 'x'

		# Charged White Golf Cart
		else:

			# Top row
			if y == 0:

				# Both Golf Carts charged
				if board[10][x] == 'x' and blackCharged:
					destroy = x

				# Move White's Golf Cart to bottom row
				else:
					for i in range(0, 10):
						board[i][x] = '.'
						board[10][x] = 'X'

			# Bottom row
			else:

				# Both Golf Carts charged
				if board[0][x] == 'x' and blackCharged:
					destroy = x

				# Move White's Golf Cart to top row
				else:
					for i in range(10, 0, -1):
						board[i][x] = '.'
						board[0][x] = 'X'

	# Destroy the whole column
	if destroy != -1:
		for i in range(0, 11):
			board[i][x] = '.'

# Update the state of the board should a piece be poisoned by a Serpent or a Grand Empress
def poison(board):
	serpentEmpress = []
	toRemove = []

	# Iterate over every piece on the board
	for y, row in enumerate(board):
		for x, piece in enumerate(row):

			# Get the serpent or grand empress coordinates
			if piece in "eEsS":
				serpentEmpress.append((y, x, piece))

	# List is not empty
	while serpentEmpress:
		y, x, piece = serpentEmpress.pop(0)

		# Generate list of biological pieces
		if piece in Constants.WHITE:
			biologicalPieces = copy.deepcopy(Constants.BLACK)
			biologicalPieces.remove('x')
			biologicalPieces.remove('h')
		else:
			biologicalPieces = copy.deepcopy(Constants.WHITE)
			biologicalPieces.remove('X')
			biologicalPieces.remove('H')

		# Generate current and 8 adjacent locations of a serpent or a grand empress
		for i in range(-1, 2):
			for j in range(-1, 2):

				# Skip over current location
				if i == 0 and j == 0:
					continue

				# Boundary check
				if 0 <= y + i < 11 and 0 <= x + j < 11 and board[y + i][x + j] in biologicalPieces:

					# Get the coordinates of the piece to be poisoned
					poisonPieceY = y + i
					poisonPieceX = x + j

					# Check for enemy adjacent serpent
					if board[poisonPieceY][poisonPieceX] in "sS":
						toRemove.append((y, x))

					# Generate current and 8 adjacent locations of the piece to be poisoned
					for k in range(-1, 2):
						for l in range(-1, 2):

							# Skip over current piece to be poisoned location
							if k == 0 and l == 0:
								continue

							# Check if Old Woman is adjacent to the piece to be poisoned by the serpent
							if 0 <= poisonPieceY + k < 11 and 0 <= poisonPieceX + l < 11 and board[poisonPieceY + k][poisonPieceX + l] in "oO" and piece in "sS":

								# Make sure old woman is in the same set as the piece to be poisoned.
								if board[poisonPieceY + k][poisonPieceX + l] in biologicalPieces:
								
									# Promote Old Woman to Grand Empress
									if 'o' in biologicalPieces:
										board[poisonPieceY + k][poisonPieceX + l] = 'e'
									else:
										board[poisonPieceY + k][poisonPieceX + l] = 'E'

									toRemove.append((y, x))

					toRemove.append((poisonPieceY, poisonPieceX))
	
	# Remove all the pieces as a result of serpent's poison effect
	while toRemove:
		y, x = toRemove.pop(0)
		board[y][x] = '.'

# Update the state of the board with some of generic after effects
def afterEffects(board):

	# White pawn transforming to time machine
	for i, piece in enumerate(board[10]):
		if piece == 'P':
			board[10][i] = 'H'	

	# Black pawn transforming to time machine
	for i, piece in enumerate(board[0]):
		if piece == 'p':
			board[0][i] = 'h'

	# White king transforming to king with a jetpack
	if board[5][5] == 'K':
		board[5][5] = 'W'

	# Black king transforming to king with a jetpack
	elif board[5][5] == 'k':
		board[5][5] = 'w'

	# Poison before teleportation
	poison(board)

	# Charged Golf Cart
	whiteCharged = 0
	blackCharged = 0

	# Pawn in the middle of board
	for piece in board[5]:

		if piece == 'p':
			whiteCharged = 1

		if piece == 'P':
			blackCharged = 1

	# Time machine
	if 'H' in board[10]:
		whiteCharged = 1

	if 'h' in board[0]:
		blackCharged = 1
	
	# One or both potential golf carts are charged
	if whiteCharged or blackCharged:
		chargedGolfCart(board, whiteCharged, blackCharged)

	# Get all the pieces on the transporter pads
	transporterPad = []
	transporterPad.append(board[3][1]);
	transporterPad.append(board[3][9]);
	transporterPad.append(board[7][1]);
	transporterPad.append(board[7][9]);

	# Shift all the pieces to their corresponding transporter pad
	board[7][9] = transporterPad.pop(0);
	board[3][1] = transporterPad.pop(0);
	board[3][9] = transporterPad.pop(0);
	board[7][1] = transporterPad.pop(0);

	# Poison after teleportation
	poison(board)

	# Prince Joey
	for y, row in enumerate(board):
		princeJoey = []
		for x, piece in enumerate(row):

			# Find Prince Joey in the current row
			if piece in "jJ":
				princeJoey.append((y, x))

		# If Prince Joey(s) are in the row check if they will explode
		if princeJoey:
			totalPieces = 0
			for i in range(0, 11):

				# Count the number of total pieces
				if board[y][i] not in Constants.NEUTRAL:
					totalPieces += 1

			# All Prince Joeys in this row explode
			if totalPieces % 5 == 0:

				while (princeJoey):
					princeJoeyY, princeJoeyX = princeJoey.pop(0)

					# Generate current and adjacent locations of Prince Joey
					for j in range(-1, 2):
						for k in range(-1, 2):

							# Boundary check
							if 0 <= princeJoeyY + j < 11 and 0 <= princeJoeyX + k < 11:
								board[princeJoeyY + j][princeJoeyX + k] = '.'

	# Place the jetpack back on the board after a move or capture
	if board[5][5] == '.':
		board[5][5] = '#'

	# Place Top left transporter pad back on the board after a move or capture
	if board[3][1] == '.':
		board[3][1] = '*';

	# Place Top right transporter padback on the board after a move or capture  
	if board[3][9] == '.':
		board[3][9] = '*'

	# Place Bottom left transporter pback on the board after a move or capturead
	if board[7][1] == '.':
		board[7][1] = '*'

	# Place Bottom right transporter back on the board after a move or capturepad 
	if board[7][9] == '.':
		board[7][9] = '*'

	return board

# Evaluate a state of the board based on a number heuristic and assign it a score
def heuristics(state, player):
	totalScore = 0
	kingYX = ()
	serpentYX = ()
	catapultYX = ()
	beekeeperYX = ()
	gorillaCoordinates = []
	bestGorillaDistance = []
	enemyKingYX = ()

	if player == 'W':
		friendlyPieces = Constants.WHITE
		enemyPieces = Constants.BLACK
		enemyRow = 10
		enemyRow2 = 9
	else:
		friendlyPieces = Constants.BLACK
		enemyPieces = Constants.WHITE
		enemyRow = 0
		enemyRow2 = 1
 
 	# Go through the whole board
	for y, row in enumerate(state):
		for x, piece in enumerate(row):

			# Skip over empty spaces
			if piece in Constants.NEUTRAL:
				continue

			# SKIP OVER FRIENDLY PARALYZED PIECE - TO DO
			
			# King and King with a Jetpack score
			if piece in "kKwW" and piece in friendlyPieces:
				totalScore = totalScore + 100000
				# Get King coordinates
				kingYX = y, x
			# Grand Empress score
			elif piece in "eE" and piece in friendlyPieces:
				totalScore = totalScore + 50000
			# Serpent score
			elif piece in "sS" and piece in friendlyPieces:
				totalScore = totalScore + 25000
				# Get Serpent coordinates
				serpentYX = y, x
			# Catapult score
			elif piece in "cC" and piece in friendlyPieces:
				totalScore = totalScore + 12500
				# Get Catapult coordinates
				catapultYX = y, x
			# Old Woman score
			elif piece in "oO" and piece in friendlyPieces:
				totalScore = totalScore + 10000
			# Beekeeper score
			elif piece in "zZ" and piece in friendlyPieces:
				totalScore = totalScore + 7500
				# Get Beekeeper cooridnates
				beekeeperYX = y, x
			# Rook and Gorilla score
			elif piece in "rRgG" and piece in friendlyPieces:
				totalScore = totalScore + 5000
				# Get Gorilla coordinates
				if piece in "gG":
					gorillaCoordinates.append((y, x))
			# Knight and Bishop score
			elif piece in "nNbB" and piece in friendlyPieces:
				totalScore = totalScore + 4000
			# Prince Joey score
			elif piece in "jJ" and piece in friendlyPieces:
				totalScore = totalScore + 2000

			# Enemy King and King with a Jetpack score
			elif piece in "kKwW" and piece in enemyPieces:
				totalScore = totalScore - 100000
				# Get enemy King coordinates
				enemyKingYX = y, x
			# Enemy Grand Empress score
			elif piece in "eE" and piece in enemyPieces:
				totalScore = totalScore - 50000
			# Enemy Serpent score
			elif piece in "sS" and piece in enemyPieces:
				totalScore = totalScore - 25000
			# Enemy Catapult score
			elif piece in "cC" and piece in enemyPieces:
				totalScore - totalScore - 12500
			# Enemy Old Woman score
			elif piece in "oO" and piece in enemyPieces:
				totalScore = totalScore - 10000
			# Enemy Beekeeper score
			elif piece in "zZ" and piece in enemyPieces:
				totalScore = totalScore - 7500
			# Enemy Rook and Gorilla score
			elif piece in "rRgG" and piece in enemyPieces:
				totalScore = totalScore - 5000
			# Enemy Knight and Bishop score
			elif piece in "nNbB" and piece in enemyPieces:
				totalScore = totalScore - 4000
			elif piece in "jJ" and piece in enemyPieces:
				totalScore = totalScore - 2000

			# Rook in middle column - ROOK SCORE TOO HIGH?
			for i in range(0,11):
				if piece in friendlyPieces and piece in "rR" and piece == state[i][5]:
					totalScore = totalScore + 5500

			# Total friendly pieces score
			if piece in friendlyPieces:
				totalScore = totalScore + 1000
			# Total enemy pieces score
			elif piece in enemyPieces:
				totalScore = totalScore - 1000

	# Catapult related score
	if catapultYX:

		# Pieces offset from the Catapult
		if player == 'W':
			behindCatapult = catapultYX[0] - 1
		else:
			behindCatapult = catapultYX[0] + 1

		# Generate catapult x offset
		for i in range(-1, 2):

			# Boundary check
			if 0 <= behindCatapult < 11 and 0 <= catapultYX[1] + i < 11:

				# Score for pieces behind the catapult
				if state[behindCatapult][catapultYX[1] + i] in friendlyPieces:
					totalScore = totalScore + 2000

	# King related score
	if kingYX:

		# Prince Joey offset from King
		if player == 'W':
			inFrontKing = kingYX[0] + 2
		else:
			inFrontKing = kingYX[0] - 2

			# Boundary check
			if 0 <= inFrontKing < 11 and 0 <= kingYX[1] < 11:

				# Prince Joey ahead of the King by 2 score
				if state[inFrontKing][kingYX[1]] in "jJ" and state[inFrontKing][kingYX[1]] in friendlyPieces:
					totalScore = totalScore + 500

		
	# Euclidean distance of Serpent from enemy King score
	if enemyKingYX and serpentYX:
		serpentDistance = math.sqrt(math.pow((enemyKingYX[1] - serpentYX[1]), 2) + math.pow((enemyKingYX[0] - serpentYX[0]), 2))
		totalScore = totalScore - (serpentDistance * 75)

	# Get the best Euclidean distance of the two Gorilla from enemy King
	if enemyKingYX and gorillaCoordinates:

		while gorillaCoordinates:
			gorillaYX = gorillaCoordinates.pop(0)
			gorillaDistance = math.sqrt(math.pow((enemyKingYX[1] - gorillaYX[1]), 2) + math.pow((enemyKingYX[0] - gorillaYX[0]), 2))
			bestGorillaDistance.append(gorillaDistance)

	# Euclidean distance of Gorilla from enemy King score - INDENT RIGHT?
	if bestGorillaDistance:
		totalScore = totalScore - (min(bestGorillaDistance) * 50)

	# Eucliden distance of Beekeeper from enemy King score
	if enemyKingYX and beekeeperYX:
		beekeeperDistance = math.sqrt(math.pow((enemyKingYX[1] - beekeeperYX[1]), 2) + math.pow((enemyKingYX[0] - beekeeperYX[0]), 2))
		totalScore = totalScore - (beekeeperDistance * 25)

	# EUCLIDEAN DISTANCE FOR KNIGHT AND BISHOP TO DO

	return totalScore

# Alpha-beta maximizer
def maxMove(board, player, startingDepth, depth, alpha, beta):
	
	if depth == 0:
		return heuristics(board, player)

	# Generate successor boards
	successorBoards = succesor(board, player)

	# Go through each successor board
	while successorBoards:
		parentBoard = successorBoards.pop(0)

		while parentBoard:

			# Apply after effects on the board
			tempBoard = afterEffects(parentBoard.pop(0))

			# Get the minimum score move
			score = minMove(tempBoard, player, startingDepth, depth - 1, alpha, beta)

			if score >= beta:
				return beta

			# Update alpha
			if score > alpha:
				alpha = score
				bestBoard = tempBoard

	if depth == startingDepth:
		return bestBoard
	else:
		return alpha

# Alpha-beta minimizer
def minMove(board, player, startingDepth, depth, alpha, beta):

	if depth == 0:
		return heuristics(board, player)

	# Generate successor boards for opponent 
	if player == 'W':
		successorBoards = succesor(board, 'B')
	else:
		successorBoards = succesor(board, 'W')

	# Go through each successor board
	while successorBoards:
		parentBoard = successorBoards.pop(0)

		while parentBoard:

			# Apply after effects on the board
			tempBoard = afterEffects(parentBoard.pop(0))

			# Get the maximum score move
			score = maxMove(tempBoard, player, startingDepth, depth - 1, alpha, beta)

			if score <= alpha:
				return alpha

			# Update beta
			if score < beta:
				beta = score
				
	return beta

if __name__ == "__main__":
	chosenBoard = []

	# Create an 11x11 chess board
	startBoard = [[" " for x in range(11)] for x in range(11)]

	# Read the board file
	for row, line in enumerate( fileinput.input() ):

		# Get the current player's turn
		if row == 0:
			currentPlayer = line[:-1]

		# Update the current state of the chess board
		elif 0 < row < 12:
			for col, piece in enumerate(line[:-1]):
				startBoard[row-1][col] = piece

		# Store current time used
		elif row == 12:
			currenTime = int(line[:-1])

		# Store maximum allowed time
		elif row == 13:
			allowedTime = int(line[:-1])
		
		# Store current turn
		else:
			currentTurn = int(line)

	# White first turn
	if currentTurn == 0:
		startBoard[1][5] = '.'
		startBoard[2][5] = 'J'
		chosenBoard = startBoard
	
	# Black first turn
	elif currentTurn == 1:
		startBoard[9][5] = '.'
		startBoard[8][5] = 'j'
		chosenBoard = startBoard

	# White second turn
	elif currentTurn == 2:
		startBoard[1][9] = '.'
		startBoard[3][9] = 'P'
		chosenBoard = afterEffects(startBoard)		

	# Black second turn
	elif currentTurn == 3:
			startBoard[9][9] = '.'

			# Move pawn two spaces
			if startBoard[7][9] == '*':
				startBoard[7][9] = 'p'
				chosenBoard = afterEffects(startBoard)
			# Move pawn one space
			else:
				startBoard[8][9] = 'p'
				chosenBoard = afterEffects(startBoard)

	# White third turn		
	elif currentTurn == 4:
		startBoard[0][8] = '.'
		startBoard[1][9] = 'C'
		chosenBoard = afterEffects(startBoard)

	# Black third turn
	elif currentTurn == 5:
		startBoard[10][8] = '.'
		startBoard[9][9] = 'c'
		chosenBoard = afterEffects(startBoard)

	# Move depends on heuristics
	else:

		# Depth 2
		if currenTime < 55000:
			chosenBoard = maxMove(startBoard, currentPlayer, 2, 2, -sys.maxint - 1, sys.maxint)
		# Depth 1
		else:
			chosenBoard = maxMove(startBoard, currentPlayer, 1, 1, -sys.maxint - 1, sys.maxint)

	# Change player after every move
	if currentPlayer == 'W':
		currentPlayer = 'B'
	else:
		currentPlayer = 'W'

	# Update the turn for the next player
	currentTurn += 1

	# Write the chosen board to standard out
	#print currentPlayer
	#for row in chosenBoard:
	#	print ''.join(row)
	#print currenTime
	#print allowedTime
	#print currentTurn

	# Write the chosen board to board.out
	outputFile = open("board.out", "w");
	outputFile.write(currentPlayer + "\n")

	for row in chosenBoard:
	 	outputFile.write(''.join(row) + "\n")

	outputFile.write(str(currenTime) + "\n")
	outputFile.write(str(allowedTime) + "\n")
	outputFile.write(str(currentTurn))
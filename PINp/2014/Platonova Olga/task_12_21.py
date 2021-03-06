# Задача 12. Вариант 21.
#Разработайте игру "Крестики-нолики". (см. М.Доусон Программируем на Python гл. 6).

# Platonova O. A.
# 30.05.2016

def display_instruct():
    print("""
	    Приветствуем Вас в игре "Крестики-нолики". Ниже представлено игровое поле.
	    			Каждая цифра соответствует номеру поля для игры.
										0 | 1 | 2
										---------
										3 | 4 | 5
										---------
										6 | 7 | 8
		""")
X="X"
O="O"
EMPTY=" "
TIE="Ничья"
NUM_SQUARES=9

def ask_yes_no(question):
	response=None
	while response not in ("д","н"):
		response=input(question).lower()
	return response

def ask_number(question, low, high):
	response=None
	while response not in range(low, high):
		response=int(input(question))
	return response

def pieces():
	go_first=ask_yes_no("Вы будете ходить первым? (д/н): ")
	if go_first=="д":
		print("\nВы играете крестиками.")
		human=X
		computer=O
	else:
		print("\nВы играете ноликами.")
		computer=X
		human=O
	return computer, human

def new_board():
	board=[]
	for square in range(NUM_SQUARES):
		board.append(EMPTY)
	return board

def display_board(board):
	print("\n\t", board[0], "|", board[1], "|", board[2])
	print("\t", "---------")
	print("\t", board[3], "|", board[4], "|", board[5])
	print("\t", "---------")
	print("\t", board[6], "|", board[7], "|", board[8])

def legal_moves(board):
	moves = []
	for square in range(NUM_SQUARES):
		if board[square]==EMPTY:
			moves.append(square)
	return moves

def winner(board):
	WAYS_TO_WIN=((0, 1, 2),
				(3, 4, 5),
				(6, 7, 8),
				(0, 3, 6),
				(1, 4, 7),
				(2, 5, 8),
				(0, 4, 8),
				(2, 4, 6))
	for row in WAYS_TO_WIN:
		if board[row[0]]==board[row[1]]==board[row[2]]!=EMPTY:
			winner=board[row[0]]
			return winner
		if EMPTY not in board:
			return TIE
	return None

def human_move(board, human):
	legal=legal_moves(board)
	move=None
	while move not in legal:
		move=ask_number("Ваш ход. Выберите поле от 0 до 8", 0, NUM_SQUARES)
		if move not in legal:
			print("\nНедопустимый ход.\n")
	return move

def computer_move(board, computer, human):
	board=board[:]
	BEST_MOVES=(4, 0, 2, 6, 8, 1, 3, 5, 7)
	print("Я выберу поле номер", end=" ")
	for move in legal_moves(board):
		board[move]=computer
		if winner(board)==computer:
			print(move)
			return move
		board[move] = EMPTY
	for move in legal_moves(board):
		board[move]=human
		if winner(board)==human:
			print(move)
			return move
		board[move]=EMPTY
	for move in BEST_MOVES:
		if move in legal_moves(board):
			print(move)
			return move

def next_turn(turn):
	if turn==X:
		return O
	else:
		return X

def congrat_winner(the_winner, computer, human):
	if the_winner !=TIE:
		print("Три", the_winner, "в ряд!\n")
	else:
		print("Ничья!\n")
	if the_winner==computer:
		print("Победил компьютер")
	elif the_winner==human:
		print("Поздравляем с победой!")
	elif the_winner==TIE:
		print("Победила дружба.")

def main():
	display_instruct()
	computer, human=pieces()
	turn=X
	board=new_board()
	display_board(board)
	while  not winner(board):
		if turn==human:
			move=human_move(board, human)
			board[move]=human
		else:
			move=computer_move(board, computer, human)
			board[move]=computer
		display_board(board)
		turn=next_turn(turn)
	the_winner=winner(board)
	congrat_winner(the_winner, computer, human)

main()
input("\n\nНажмите Enter, чтобы выйти.")
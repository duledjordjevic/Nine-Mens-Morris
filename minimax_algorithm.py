from copy import deepcopy
# from Game import game

def number_of_mices(game):
    black_counter = 0
    white_counter = 0
    for i in game.current_state.all_mices:
        x,y = int(i[0][0]), int(i[0][1])
        player = game.current_state.board[x][y]
        if player != 0:
            player1, player2 = game.current_state.board[int(i[1][0])][int(i[1][1])], game.current_state.board[int(i[2][0])][int(i[2][1])]
            if player == player1 == player2 == "B":
                black_counter += 1
            elif player == player1 == player2 == "W":
                white_counter += 1
    return white_counter, black_counter
def number_of_blocked_pieces(game, player_turn):
    blocked_moves = 0
    all_moves = game.get_all_moves(player_turn)
    used_positions = game.get_all_used_positions(player_turn)
    all_moves_positions = []
    for i in all_moves:
        if i['xy1'] not in all_moves_positions:
            all_moves_positions.append(i['xy1'])

    for i in used_positions:
        if i not in all_moves_positions:
            blocked_moves += 1

    return blocked_moves
def counter_of_pices(game):
    black = len(game.get_all_used_positions("B"))
    white = len(game.get_all_used_positions("W"))
    return white, black
def number_of_deuce(game, player_turn):
    used_positions = game.get_all_used_positions(player_turn)
    count = 0
    for i in game.current_state.all_deuces:
        x1, y1 = int(i[0][0]), int(i[0][1])
        x2, y2 = int(i[1][0]), int(i[1][1])

        if game.current_state.board[x1][y1] == game.current_state.board[x2][y2] == player_turn:
            count += 1

    return count

def heuristic(game):
    white_mices, black_mices = number_of_mices(game)
    h = black_mices - white_mices
    black_blocked = number_of_blocked_pieces(game, "B")
    white_blocked = number_of_blocked_pieces(game, "W")
    h += black_blocked - white_blocked
    white_all, black_all  = counter_of_pices(game)
    h += black_all - white_all
    black_deuces = number_of_deuce(game, "B")
    white_deuces = number_of_deuce(game, "W")
    h += black_deuces - white_deuces
    return h
# def minimax(board, depth, who_play_tf):
#     end, player_win = game.is_end()
#     if end or depth == 0:
#         return board.heuristic(), board
    
#     if who_play_tf:
#         maxHeuristic = -10000
#         best_move = None

#         return maxHeuristic, best_move
#     else:

def minimax(game):
    game = deepcopy(game)
    game.current_state.board[0][0] = "W"
    print(game.current_state)
    print(heuristic(game))
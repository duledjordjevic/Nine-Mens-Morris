from copy import deepcopy
from tracemalloc import start
# from Game import game
import time
from wsgiref.simple_server import demo_app
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
def number_of_double_mices(game, player_turn):
    used_positions = game.get_all_used_positions(player_turn)
    count_all = 0
    for i in used_positions:
        count = 0
        for position in game.current_state.hashmap_mices[i]:
            x1, y1 = int(position[0][0]), int(position[0][1])
            x2, y2 = int(position[1][0]), int(position[1][1])
            if game.current_state.board[x1][y1] == game.current_state.board[x2][y2] == player_turn:
                count += 1
        if count == 2:
            count_all += 1

    return count_all

def blocked_mice(game):
    white_blocked = 0
    black_blocked = 0
    for i in game.current_state.all_mices:
        black = 0
        white = 0
        for move in i:
            x, y = int(move[0]), int(move[1])
            if game.current_state.board[x][y] == "B":
                black += 1
            elif game.current_state.board[x][y] == "W":
                white += 1
        if black == 2 and white == 1:
            black_blocked += 1
        elif black == 1 and white == 2:
            white_blocked += 1

    return white_blocked, black_blocked

def three_piece_configuration(game):
    black = 0
    white = 0

    white_positions = game.get_all_used_positions("W")
    black_positions = game.get_all_used_positions("B")

    for i in white_positions:
        count = 0
        for moves in game.current_state.hashmap_mices[i]:
            x1, y1 = int(moves[0][0]), int(moves[0][1])
            x2, y2 = int(moves[1][0]), int(moves[1][1])

           
            if game.current_state.board[x1][y1] == "W" and game.current_state.board[x2][y2] == 0:
                count += 1
            elif game.current_state.board[x1][y1] == 0 and game.current_state.board[x2][y2] == "W":
                count += 1
        
        if count == 2:
            white += 1
    for i in black_positions:
        count = 0
        for moves in game.current_state.hashmap_mices[i]:
            x1, y1 = int(moves[0][0]), int(moves[0][1])
            x2, y2 = int(moves[1][0]), int(moves[1][1])

           
            if game.current_state.board[x1][y1] == "B" and game.current_state.board[x2][y2] == 0:
                count += 1
            elif game.current_state.board[x1][y1] == 0 and game.current_state.board[x2][y2] == "B":
                count += 1
        
        if count == 2:
            black += 1
    return white, black


def heuristic(game, phase_of_game):
    h = 0
    white_config, black_config = three_piece_configuration(game)
    three_piece_config = black_config - white_config

    white_mice_blocked, black_mice_blocked  = blocked_mice(game)
    mice_blocked = white_mice_blocked - black_mice_blocked

    white_mices, black_mices = number_of_mices(game)
    mices = black_mices - white_mices

    black_blocked = number_of_blocked_pieces(game, "B")
    white_blocked = number_of_blocked_pieces(game, "W")
    blocked = white_blocked - black_blocked

    white_all, black_all  = counter_of_pices(game)
    all_pieces = black_all - white_all

    black_deuces = number_of_deuce(game, "B")
    white_deuces = number_of_deuce(game, "W")
    deuces = black_deuces - white_deuces

    black_double_mices = number_of_double_mices(game, "B")
    white_double_mices = number_of_double_mices(game, "W")
    double_mices = black_double_mices - white_double_mices

    tf, who_win = game.is_end()
    win = 0
    if tf:
        if who_win == "W":
            win = -1
        else:
            win = 1
    if phase_of_game == 0:
        h = (mice_blocked * 30) + (50 * mices) + (blocked * 1) + (all_pieces * 9) + (deuces * 10)  + (7 * three_piece_config)
    else:
        h = (mice_blocked * 14) + (43 * mices) + (blocked * 10) + (all_pieces * 11) + (double_mices * 8)  + (win * 1086)
    # h = (mice_blocked * 20) + (mices * 50) + (blocked * 5) + (all_pieces * 20) + (deuces * 5) + (three_piece_config * 10) + (double_mices * 100) + (win * 10000)
    return h

def minimax_mice(game, player_turn):
    all_positions = game.get_all_used_positions(player_turn)
    best_move = None
    if player_turn == "W":
        best_value = float('-inf')
    else:
        best_value = float('inf')
    for move in all_positions:
        x, y = int(move[0]), int(move[1])
        game = deepcopy(game)
        game.current_state.board[x][y] = 0
        heuris = heuristic(game, 0)
        if player_turn == "W":
            best_value = max(best_value, heuris)
        else:
            best_value = min(best_value, heuris)

        if best_value == heuris:
            best_move = move
    return best_move

def get_all_moves_1(game, player_turn):
    from Game import Game
    moves = []
    all_positions = game.get_all_free_positions()
    for move in all_positions:
        # temp_game = deepcopy(game)
        temp_game = Game()
        temp_game.current_state.board = deepcopy(game.current_state.board)
        x, y = int(move['xy'][0]), int(move['xy'][1])
        temp_game.current_state.board[x][y] = player_turn
        moves.append([temp_game, move])
    return moves

def minimax_1(game, depth, max_player, alpha, beta):
    if depth == 0:
        return heuristic(game, 0), game
    
    if max_player:
        maxHeuristic = float('-inf')
        best_move = None
        for list_of_moves in get_all_moves_1(game, "B"):
            move = list_of_moves[0]
            last_move = list_of_moves[1]
            if move.is_mice(last_move['xy'], "B"):
                move1 = minimax_mice(move, "W")
                x, y = int(move1[0]), int(move1[1])
                move.current_state.board[x][y] = 0
            heuris = minimax_1(move, depth-1, False, alpha, beta)
            maxHeuristic = max(maxHeuristic, heuris[0])
    
            alpha = max(alpha, maxHeuristic)
            if beta <= alpha:
                break

            if maxHeuristic == heuris[0]:
                best_move = move
    
        return maxHeuristic, best_move
    else:
        minHeuristic = float('inf')
        best_move = None
        for list_of_moves in get_all_moves_1(game, "W"):
            move = list_of_moves[0]
            last_move = list_of_moves[1]
            if move.is_mice(last_move['xy'], "W"):
                move1 = minimax_mice(move, "B")
                x, y = int(move1[0]), int(move1[1])
                move.current_state.board[x][y] = 0
            heuris = minimax_1(move, depth-1, True, alpha, beta)
            minHeuristic = min(minHeuristic, heuris[0])
        
            beta = min(beta, minHeuristic)
            if beta <= alpha:
                break

            if minHeuristic == heuris[0]:
                best_move = move
        return minHeuristic, best_move

def get_all_moves_2(game, player_turn):
    from Game import Game
    moves = []
    all_moves = game.get_all_moves(player_turn)
    for move in all_moves:
        # temp_game = deepcopy(game)
        temp_game = Game()
        temp_game.current_state.board = deepcopy(game.current_state.board)
        x1, y1 = int(move['xy1'][0]), int(move['xy1'][1])
        x2, y2 = int(move['xy2'][0]), int(move['xy2'][1])
        temp_game.current_state.board[x2][y2] = player_turn
        temp_game.current_state.board[x1][y1] = 0
        moves.append([temp_game, move['xy2']])

    return moves

def minimax_2(game, depth, max_player, alpha, beta):
    if depth == 0:
        return heuristic(game, 0), game
    
    if max_player:
        maxHeuristic = float('-inf')
        best_move = None
        for list_of_moves in get_all_moves_2(game, "B"):
            move = list_of_moves[0]
            last_move = list_of_moves[1]
            if move.is_mice(last_move, "B"):
                move1 = minimax_mice(move, "W")
                x, y = int(move1[0]), int(move1[1])
                move.current_state.board[x][y] = 0
            heuris = minimax_2(move, depth-1, False, alpha, beta)
            maxHeuristic = max(maxHeuristic, heuris[0])

            alpha = max(alpha, maxHeuristic)
            if beta <= alpha:
                break

            if maxHeuristic == heuris[0]:
                best_move = move
    
        return maxHeuristic, best_move
    else:
        minHeuristic = float('inf')
        best_move = None
        for list_of_moves in get_all_moves_2(game, "W"):
            move = list_of_moves[0]
            last_move = list_of_moves[1]
            if move.is_mice(last_move, "W"):
                move1 = minimax_mice(move, "B")
                x, y = int(move1[0]), int(move1[1])
                move.current_state.board[x][y] = 0
            heuris = minimax_2(move, depth-1, True, alpha, beta)
            minHeuristic = min(minHeuristic, heuris[0])

            beta = min(beta, minHeuristic)
            if beta <= alpha:
                break

            if minHeuristic == heuris[0]:
                best_move = move
        return minHeuristic, best_move




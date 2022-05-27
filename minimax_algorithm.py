from copy import deepcopy
from tracemalloc import start
from Game import game
import time
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

def heuristic(game, phase_of_game):
    h = 0

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
        h = (26 * mices) + (blocked * 1) + (all_pieces * 9) + (double_mices * 10) 
        print(h)
    else:
        h = (43 * mices) + (blocked * 10) + (all_pieces * 11) + (double_mices * 8) + (win * 1086)
    return h

def minimax_1(game, position, depth, max_player):
    game = deepcopy(game)
    end, player_win = game.is_end()
    if end or depth == 0:
        return heuristic(game, 0), position
    
    if max_player:
        maxHeuristic = float('-inf')
        best_move = None
        all_moves = game.get_all_free_positions()
        for move in all_moves:
            x, y = int(move['xy'][0]), int(move['xy'][1])
            game.current_state.board[x][y] = "B"
            print(game.current_state)
            heuris = minimax_1(game, move, depth-1, False)
            maxHeuristic = max(maxHeuristic, heuris[0])
            if maxHeuristic == heuris[0]:
                best_move = move
        return maxHeuristic, best_move
    else:
        minHeuristic = float('inf')
        best_move = None
        all_moves = game.get_all_free_positions()
        for move in all_moves:
            x, y = int(move['xy'][0]), int(move['xy'][1])
            game.current_state.board[x][y] = "W"
            print(game.current_state)
            heuris = minimax_1(game, move, depth-1, True)
            minHeuristic = min(minHeuristic, heuris[0])
            if minHeuristic == heuris[0]:
                best_move = move
        return minHeuristic, best_move

# def minimax_2(game):
#     game = deepcopy(game)
#     # game.current_state.board[0][0] = "W"
#     # print(game.current_state)
#     print(heuristic(game, 0))
#     # print(heuristic(game))
start = time.time()
# print(minimax_1(game, None, 4, True))
end = time.time()
print(game.current_state)
print(end - start)
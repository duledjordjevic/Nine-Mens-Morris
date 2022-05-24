from Board import Board
import time
from copy import deepcopy
class Game(object):

    def __init__(self):
        self.current_state = Board()
        self.player_turn = None
        self.black_pieces_in_hand = 0
        self.white_pieces_in_hand = 0

    def get_all_moves(self, player_turn):
        possible_moves = []
        
        if self.current_state.board[0][0] == player_turn:
            if self.current_state.board[0][3] == 0:
                position = {"xy1" : "00", "xy2" : "03"}
                possible_moves.append(position)
            if self.current_state.board[3][0] == 0:
                position = {"xy1" : "00", "xy2" : "30"}
                possible_moves.append(position)
        
        if self.current_state.board[0][3] == player_turn:
            if self.current_state.board[0][0] == 0:
                position = {"xy1" : "03", "xy2" : "00"}
                possible_moves.append(position)
            if self.current_state.board[0][6] == 0:
                position = {"xy1" : "03", "xy2" : "06"}
                possible_moves.append(position)
            if self.current_state.board[1][3] == 0:
                position = {"xy1" : "03", "xy2" : "13"}
                possible_moves.append(position)

        if self.current_state.board[0][6] == player_turn:
            if self.current_state.board[0][3] == 0:
                position = {"xy1" : "03", "y" : 3}
                possible_moves.append(position)
            if self.current_state.board[3][6] == 0:
                position = {"xy1" : "03", "xy2" : "36"}
                possible_moves.append(position)
        
        if self.current_state.board[1][1] == player_turn:
            if self.current_state.board[1][3] == 0:
                position = {"xy1" : "13", "xy2" : "13"}
                possible_moves.append(position)
            if self.current_state.board[3][1] == 0:
                position = {"xy1" : "13", "xy2" : "31"}
                possible_moves.append(position)

        if self.current_state.board[1][3] == player_turn:
            if self.current_state.board[0][3] == 0:
                position = {"xy1" : "13", "xy2" : "03"}
                possible_moves.append(position)
            if self.current_state.board[1][1] == 0:
                position = {"xy1" : "13", "xy2" : "11"}
                possible_moves.append(position)
            if self.current_state.board[1][5] == 0:
                position = {"xy1" : "13", "xy2" : "15"}
                possible_moves.append(position)
            if self.current_state.board[2][3] == 0:
                position = {"xy1" : "13", "xy2" : "23"}
                possible_moves.append(position)

        if self.current_state.board[1][5] == player_turn:
            if self.current_state.board[1][3] == 0:
                position = {"xy1" : "15", "xy2" : "13"}
                possible_moves.append(position)
            if self.current_state.board[3][5] == 0:
                position = {"xy1" : "15", "xy2" : "35"}
                possible_moves.append(position)

        if self.current_state.board[2][2] == player_turn:
            if self.current_state.board[3][2] == 0:
                position = {"xy1" : "22", "xy2" : "32"}
                possible_moves.append(position)
            if self.current_state.board[2][3] == 0:
                position = {"xy1" : "22", "xy2" : "23"}
                possible_moves.append(position)

        if self.current_state.board[2][3] == player_turn:
            if self.current_state.board[2][2] == 0:
                position = {"xy1" : "23", "xy2" : "22"}
                possible_moves.append(position)
            if self.current_state.board[2][4] == 0:
                position = {"xy1" : "23", "xy2" : "24"}
                possible_moves.append(position)
            if self.current_state.board[1][3] == 0:
                position = {"xy1" : "23", "xy2" : "13"}
                possible_moves.append(position)

        if self.current_state.board[2][4] == player_turn:
            if self.current_state.board[2][3] == 0:
                position = {"xy1" : "24", "xy2" : "23"}
                possible_moves.append(position)
            if self.current_state.board[3][4] == 0:
                position = {"xy1" : "24", "xy2" : "34"}
                possible_moves.append(position)
            
        if self.current_state.board[3][0] == player_turn:
            if self.current_state.board[0][0] == 0:
                position = {"xy1" : "30", "xy2" : "00"}
                possible_moves.append(position)
            if self.current_state.board[6][0] == 0:
                position = {"xy1" : "30", "xy2" : "60"}
                possible_moves.append(position)
            if self.current_state.board[3][1] == 0:
                position = {"xy1" : "30", "xy2" : "31"}
                possible_moves.append(position)

        if self.current_state.board[3][1] == player_turn:
            if self.current_state.board[3][0] == 0:
                position = {"xy1" : "31", "xy2" : "30"}
                possible_moves.append(position)
            if self.current_state.board[3][2] == 0:
                position = {"xy1" : "31", "xy2" : "32"}
                possible_moves.append(position)
            if self.current_state.board[1][1] == 0:
                position = {"xy1" : "31", "xy2" : "11"}
                possible_moves.append(position)
            if self.current_state.board[5][1] == 0:
                position = {"xy1" : "31", "xy2" : "51"}
                possible_moves.append(position)

        if self.current_state.board[3][2] == player_turn:
            if self.current_state.board[3][1] == 0:
                position = {"xy1" : "32", "xy2" : "31"}
                possible_moves.append(position)
            if self.current_state.board[2][2] == 0:
                position = {"xy1" : "32", "xy2" : "22"}
                possible_moves.append(position)
            if self.current_state.board[4][2] == 0:
                position = {"xy1" : "32", "xy2" : "42"}
                possible_moves.append(position)

        if self.current_state.board[3][4] == player_turn:
            if self.current_state.board[2][4] == 0:
                position = {"xy1" : "34", "xy2" : "24"}
                possible_moves.append(position)
            if self.current_state.board[4][4] == 0:
                position = {"xy1" : "34", "xy2" : "44"}
                possible_moves.append(position)
            if self.current_state.board[3][5] == 0:
                position = {"xy1" : "34", "xy2" : "35"}
                possible_moves.append(position)
        
        if self.current_state.board[3][5] == player_turn:
            if self.current_state.board[3][4] == 0:
                position = {"xy1" : "35", "xy2" : "34"}
                possible_moves.append(position)
            if self.current_state.board[2][5] == 0:
                position = {"xy1" : "35", "xy2" : "25"}
                possible_moves.append(position)
            if self.current_state.board[5][5] == 0:
                position = {"xy1" : "35", "xy2" : "55"}
                possible_moves.append(position)
            if self.current_state.board[3][6] == 0:
                position = {"xy1" : "35", "xy2" : "36"}
                possible_moves.append(position)
        
        if self.current_state.board[3][6] == player_turn:
            if self.current_state.board[3][5] == 0:
                position = {"xy1" : "36", "xy2" : "35"}
                possible_moves.append(position)
            if self.current_state.board[0][6] == 0:
                position = {"xy1" : "36", "xy2" : "06"}
                possible_moves.append(position)
            if self.current_state.board[6][6] == 0:
                position = {"xy1" : "36", "xy2" : "66"}
                possible_moves.append(position)

        if self.current_state.board[4][2] == player_turn:
            if self.current_state.board[3][2] == 0:
                position = {"xy1" : "42", "xy2" : "32"}
                possible_moves.append(position)
            if self.current_state.board[4][3] == 0:
                position = {"xy1" : "42", "xy2" : "43"}
                possible_moves.append(position)
        
        if self.current_state.board[4][3] == player_turn:
            if self.current_state.board[4][2] == 0:
                position = {"xy1" : "43", "xy2" : "42"}
                possible_moves.append(position)
            if self.current_state.board[4][4] == 0:
                position = {"xy1" : "43", "xy2" : "44"}
                possible_moves.append(position)
            if self.current_state.board[5][3] == 0:
                position = {"xy1" : "43", "xy2" : "53"}
                possible_moves.append(position)

        if self.current_state.board[4][4] == player_turn:
            if self.current_state.board[4][3] == 0:
                position = {"xy1" : "44", "xy2" : "43"}
                possible_moves.append(position)
            if self.current_state.board[3][4] == 0:
                position = {"xy1" : "44", "xy2" : "34"}
                possible_moves.append(position)

        if self.current_state.board[5][1] == player_turn:
            if self.current_state.board[3][1] == 0:
                position = {"xy1" : "51", "xy2" : "31"}
                possible_moves.append(position)
            if self.current_state.board[5][3] == 0:
                position = {"xy1" : "51", "xy2" : "53"}
                possible_moves.append(position)
        
        if self.current_state.board[5][3] == player_turn:
            if self.current_state.board[5][1] == 0:
                position = {"xy1" : "53", "xy2" : "51"}
                possible_moves.append(position)
            if self.current_state.board[6][3] == 0:
                position = {"xy1" : "53", "xy2" : "63"}
                possible_moves.append(position)
            if self.current_state.board[5][5] == 0:
                position = {"xy1" : "53", "xy2" : "55"}
                possible_moves.append(position)
            if self.current_state.board[4][3] == 0:
                position = {"xy1" : "53", "xy2" : "43"}
                possible_moves.append(position)

        if self.current_state.board[5][5] == player_turn:
            if self.current_state.board[5][3] == 0:
                position = {"xy1" : "55", "xy2" : "31"}
                possible_moves.append(position)
            if self.current_state.board[3][5] == 0:
                position = {"xy1" : "55", "xy2" : "35"}
                possible_moves.append(position)

        if self.current_state.board[6][0] == player_turn:
            if self.current_state.board[6][3] == 0:
                position = {"xy1" : "60", "xy2" : "63"}
                possible_moves.append(position)
            if self.current_state.board[3][0] == 0:
                position = {"xy1" : "60", "xy2" : "30"}
                possible_moves.append(position)
        
        if self.current_state.board[6][3] == player_turn:
            if self.current_state.board[6][0] == 0:
                position = {"xy1" : "63", "xy2" : "60"}
                possible_moves.append(position)
            if self.current_state.board[6][6] == 0:
                position = {"xy1" : "63", "xy2" : "66"}
                possible_moves.append(position)
            if self.current_state.board[5][3] == 0:
                position = {"xy1" : "63", "xy2" : "53"}
                possible_moves.append(position)
        
        if self.current_state.board[6][6] == player_turn:
            if self.current_state.board[6][3] == 0:
                position = {"xy1" : "66", "xy2" : "63"}
                possible_moves.append(position)
            if self.current_state.board[3][6] == 0:
                position = {"xy1" : "66", "xy2" : "36"}
                possible_moves.append(position)

        return possible_moves

    def get_all_free_positions(self):
        positions = []
        for i in range(len(self.current_state.board)):
            for x in range(len(self.current_state.board[i])):
                if self.current_state.board[i][x] == 0:
                    position = {"xy" : str(i) + str(x)}
                    positions.append(position)
        return positions


    def is_mice(self, player_turn, last_move):
        pass
    def is_end(self):
        if self.black_pieces_in_hand == 0 and self.white_pieces_in_hand == 0:
            count_white = 0
            count_black = 0
            black_moves = self.get_all_moves("B")
            white_moves = self.get_all_moves("W")
            if len(white_moves) == 0:
                return True, "B"
            elif len(black_moves) == 0:
                return True, "W"

            for row in self.board:
                count_white += row.count("W")
                count_black += row.count("B")

                if count_white == 2:
                    return True, "B"
                elif count_black == 2:
                    return True, "W"
            

        return False, None
        
game = Game()
start = time.time()
print(game.current_state)
end = time.time()

print(round(start-end, 7))
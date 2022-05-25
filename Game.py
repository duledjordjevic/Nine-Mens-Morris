from Board import Board
import time
from copy import deepcopy
class Game(object):

    def __init__(self):
        self.current_state = Board()
        self.player_turn = None
        self.black_pieces_in_hand = 9
        self.white_pieces_in_hand = 9
        self.black_pieces_on_board = 0
        self.white_pieces_on_board = 0
        self.all_positions = ["00", "03", "06", "11", "13", "15", "22", "23", "24", "30", "31", "32", "34", "35", "36", "42", "43", "44", "51", "53", "55", "60", "63", "66"]

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
                position = {"xy1" : "06", "xy2" : "03"}
                possible_moves.append(position)
            if self.current_state.board[3][6] == 0:
                position = {"xy1" : "06", "xy2" : "36"}
                possible_moves.append(position)
        
        if self.current_state.board[1][1] == player_turn:
            if self.current_state.board[1][3] == 0:
                position = {"xy1" : "11", "xy2" : "13"}
                possible_moves.append(position)
            if self.current_state.board[3][1] == 0:
                position = {"xy1" : "11", "xy2" : "31"}
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
    def is_move_correct_1(self, move):
        if move in self.all_positions:
            free_positions = self.get_all_free_positions()
            for i in free_positions:
                if move == i['xy']:
                    return True
        return False

    def is_move_correct_2(self, position_of_piece, move,  player_turn):
        if position_of_piece in self.all_positions and move in self.all_positions:
            possible_moves = self.get_all_moves(player_turn)
            for i in possible_moves:
                if i['xy1'] == position_of_piece and i['xy2'] == move:
                    return True

        return False

    def first_moves(self, player_turn):
        move = input("Unesite poziciju na koju hocete da postavite figuru: ")
        while not self.is_move_correct_1(move):
            print("Molim vas da unesete slobodnu poziciju")
            move = input("Unesite poziciju na koju hocete da postavite figuru: ")
        x, y = int(move[0]), int(move[1])
        self.current_state.board[x][y] = player_turn
        return move

    def get_all_used_positions(self, player_turn):
        positions = []
        for i in self.all_positions:
            x, y = int(i[0]), int(i[1])
            if self.current_state.board[x][y] == player_turn:
                positions.append(i)

        return positions
    
    def is_mice(self, last_move, player_turn):
        x = self.current_state.hashmap_mices[last_move]
        first_list = x[0]
        second_list = x[1]
        x1, y1 = int(first_list[0][0]), int(first_list[0][1])
        x2, y2 = int(first_list[1][0]), int(first_list[1][1])
        x3, y3 = int(second_list[0][0]), int(second_list[0][1])
        x4, y4 = int(second_list[1][0]), int(second_list[1][1])
        
        if self.current_state.board[x1][y1] == player_turn and self.current_state.board[x2][y2] == player_turn:
            return True
        if self.current_state.board[x3][y3] == player_turn and self.current_state.board[x4][y4] == player_turn:
            return True
        return False
    def play(self):
        while True:
            while self.black_pieces_in_hand > 0:
                print(self.current_state)
                player_turn = "W"
                other_player = "B"
                move = self.first_moves(player_turn)
                self.white_pieces_in_hand -= 1
                self.white_pieces_on_board += 1
                if self.is_mice(move, player_turn):
                    delete = input("Dobili ste micu. Izaberite koju protivnicku figuru uzimate: ")
                    other_player_positions = self.get_all_used_positions(other_player)
                    while delete not in other_player_positions:
                        print("Molim vas da unesete tacnu poziciju.")
                        delete = input("Dobili ste micu. Izaberite koju protivnicku figuru uzimate: ")
                    x, y = int(delete[0]), int(delete[1])
                    self.current_state.board[x][y] = 0
                    self.black_pieces_on_board -= 1
                print(self.current_state)
                player_turn = "B"
                other_player = "W"
                move = self.first_moves(player_turn)
                self.black_pieces_in_hand -= 1
                self.black_pieces_on_board += 1
                if self.is_mice(move, player_turn):
                    delete = input("Dobili ste micu. Izaberite koju protivnicku figuru uzimate: ")
                    other_player_positions = self.get_all_used_positions(other_player)
                    while delete not in other_player_positions:
                        print("Molim vas da unesete tacnu poziciju.")
                        delete = input("Dobili ste micu. Izaberite koju protivnicku figuru uzimate: ")
                    x, y = int(delete[0]), int(delete[1])
                    self.current_state.board[x][y] = 0
                    self.white_pieces_on_board -= 1
            
                
            break



game = Game()
start = time.time()
game.play()
end = time.time()

print(start - end)
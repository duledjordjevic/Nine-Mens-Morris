from timeit import timeit
import time
from tracemalloc import start
from hashmap import HashMap
class Board(object):

    def __init__(self):
        self.board = [
            ["W", None, None, 0, None, None, "B"],
            [None, 0, None, "B", None, 0, None],
            [None, None, 0, "B", 0 , None, None],
            ["B", 0, "B", None, 0, 0, 0],
            [None, None, "W", "B", "W" , None, None],
            [None, 0, None, "B", None, "W", None],
            ["B", None, None, "W", None, None, "B"]
        ]
        self.all_mices = [
            ["00", "03", "06"],
            ["00", "30", "60"],
            ["60", "63", "66"],
            ["06", "36", "66"],
            ["11", "13", "15"],
            ["11", "31", "51"],
            ["51", "53", "55"],
            ["15", "35", "55"],
            ["22", "23", "24"],
            ["22", "32", "42"],
            ["42", "43", "44"],
            ["24", "34", "44"],
            ["03", "13", "23"],
            ["30", "31", "32"],
            ["63", "53", "43"],
            ["34", "35", "36"]
        ]
        ["00", "03", "06", "11", "13", "15", "22", "23", "24", "30", "31", "32", "34", "35", "36", "42", "43", "44", "51", "53", "55", "60", "63", "66"]
        self.all_deuces = [
            ["00", "03"],
            ["00", "30"],
            ["03", "13"],
            ["03", "06"],
            ["06", "36"],
            ["11", "13"],
            ["11", "31"],
            ["13", "23"],
            ["13", "15"],
            ["15", "35"],
            ["22", "32"],
            ["22", "23"],
            ["23", "24"],
            ["24", "34"],
            ["30", "60"],
            ["30", "31"],
            ["31", "32"],
            ["31", "51"],
            ["32", "42"],
            ["34", "35"],
            ["34", "44"],
            ["35", "36"],
            ["35", "55"],
            ["36", "66"],
            ["42", "43"],
            ["43", "44"],
            ["43", "53"],
            ["51", "53"],
            ["53", "55"],
            ["53", "63"],
            ["60", "63"],
            ["63", "66"]
        ]
        self.hashmap_mices = self.hashmap_of_mices()
        self.hashmap_deuces = self.hashmap_of_deuces()
    def hashmap_of_mices(self):
        h = HashMap(67)
        for i in self.all_mices:
            h[i[0]] = [i[1], i[2]]
            h[i[1]] = [i[0], i[2]]
            h[i[2]] = [i[1], i[0]]
            
        return h
    def hashmap_of_deuces(self):
        h = HashMap(67)
        for i in self.all_deuces:
            h[i[0]] = i[1]
            h[i[1]] = i[0]

        return h
    def __str__(self):
        ret = "    0   1   2   3   4   5   6\n"
        ret += "-----------------------------\n"
        ret += "0 | " + str(self.board[0][0]) + "-----------" + str(self.board[0][3]) + "-----------" + str(self.board[0][6]) + "\n"
        ret += "  | |"  "           " + "|" + "           " + "|" + "\n"
        ret += "1 | |"  + "   " + str(self.board[1][1]) + "-------" + str(self.board[1][3]) + "-------" + str(self.board[1][5])+ "   |" + "\n"
        ret += "  | |" + "   |       " + "|" + "       |   " +  "|" + "\n"
        ret += "2 | |"  + "   |" +  "   " + str(self.board[2][2]) + "---" + str(self.board[2][3]) +"---" + str(self.board[2][4])+ "   |   |" + "\n"
        ret += "  | |" + "   |   |   " + " " + "   |   |   " +  "|" + "\n"
        ret += "3 | " + str(self.board[3][0])  + "---" + str(self.board[3][1]) +  "---" + str(self.board[3][2]) + "       " + str(self.board[3][4])+ "---" + str(self.board[3][5])  + "---" + str(self.board[3][6])  + "\n"
        ret += "  | |" + "   |   |   " + " " + "   |   |   " +  "|" + "\n"
        ret += "4 | |"  + "   |" +  "   " + str(self.board[4][2]) + "---" + str(self.board[4][3]) +"---" + str(self.board[4][4])+ "   |   |" + "\n"
        ret += "  | |" + "   |       " + "|" + "       |   " +  "|" + "\n"
        ret += "5 | |"  + "   " + str(self.board[5][1]) + "-------" + str(self.board[5][3]) + "-------" + str(self.board[5][5])+ "   |" + "\n"
        ret += "  | |"  "           " + "|" + "           " + "|" + "\n"
        ret += "6 | " + str(self.board[6][0]) + "-----------" + str(self.board[6][3]) + "-----------" + str(self.board[6][6]) + "\n"

        return ret


from display import *
from itertools import chain


class piece:

    def __init__(self, color="none", p_icon="none", pos=(0,0), life=True):
        self.color = color
        self.pos = pos
        self.life = life
        self.p_icon = p_icon
        self.first_move = True

class pawn(piece):

    def move(self, x, y):
        '''X and Y are the current position'''
        X, Y = self.pos
        i = 1

        if not isinstance(x, int) or not isinstance(y, int):
            return False
        elif self.color is "white":
            '''so that it go in the oppset dirction'''
            i *= -1
            i *= -1
        passed = True
        pos_mov = self.possible_moves()

        if (x,y) in pos_mov:

            # first two statment Check for eating positions
            if valide_move((X+i,Y+i)) == False and (x == X+i and y == Y+i):
                passed = True
            elif valide_move((X-i,Y+i)) == False and (x == X-i and y == Y+i):
                passed = True
            elif valide_move((x,y)) == False:
                '''check if there is already piece at new pos'''
                passed = False
            elif (y-Y == 2 and self.first_move == False):
                ''' if pawn already moved before it can't move 2 steps again '''
                passed = False

            if passed:
                self.pos = (x,y)
                self.first_move = False
            return passed

        return False

    def possible_moves(self):
        '''all possible moves for pawn '''
        X,Y = self.pos
        w_valid = [(X,Y-1),(X,Y-1),(X-1,Y-1),(X+1,Y-1),(X,Y-2)]
        b_valid = [(X,Y+1),(X,Y+1),(X+1,Y+1),(X-1,Y+1),(X,Y+2)]

        if self.color is "white":
            W = [x for x in w_valid if valide_move(x) is True or board_pieces[get_piece_at(x)].color == "black"]
        else:    
            W = [x for x in b_valid if valide_move(x) is True or board_pieces[get_piece_at(x)].color == "white"]

        return W 


class queen(piece):

    def move(self, x, y):
        '''X and Y are the current position'''
        X, Y = self.pos

        if not isinstance(x, int) or not isinstance(y, int):
            return False

        pos_mov = self.possible_moves()

        if (x, y) in pos_mov:
            if valide_move((x, y)) == False:
                return False

            self.pos = (x, y)
            return True

        return False

    def possible_moves(self):
        '''all possible moves for queen'''
        X, Y = self.pos
        moves = []

        # Horizontal and vertical moves
        for i in range(8):
            if i != X:
                moves.append((i, Y))
            if i != Y:
                moves.append((X, i))

        # Diagonal moves
        for i in range(1, 8):
            if X + i < 8 and Y + i < 8:
                moves.append((X + i, Y + i))
            if X - i >= 0 and Y + i < 8:
                moves.append((X - i, Y + i))
            if X + i < 8 and Y - i >= 0:
                moves.append((X + i, Y - i))
            if X - i >= 0 and Y - i >= 0:
                moves.append((X - i, Y - i))

        return moves

class king(piece):
    def move(self, x, y):
        '''X and Y are the current position'''
        X, Y = self.pos

        if not isinstance(x, int) or not isinstance(y, int):
            return False

        pos_mov = self.possible_moves()

        if (x, y) in pos_mov:
            if valide_move((x, y)) == False:
                return False

            self.pos = (x, y)
            return True

        return False

    def possible_moves(self):
        '''all possible moves for king'''
        X, Y = self.pos
        moves = []

        # Horizontal and vertical moves
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if X + i >= 0 and X + i < 8 and Y + j >= 0 and Y + j < 8:
                    moves.append((X + i, Y + j))

        return moves

class bishop(piece):
    def move(self, x, y):
        '''X and Y are the current position'''
        X, Y = self.pos

        if not isinstance(x, int) or not isinstance(y, int):
            return False

        pos_mov = self.possible_moves()

        if (x, y) in pos_mov:
            if valide_move((x, y)) == False:
                return False

            self.pos = (x, y)
            return True

        return False

    def possible_moves(self):
        '''all possible moves for bishop'''
        X, Y = self.pos
        moves = []

        # Diagonal moves
        for i in range(-7, 8):
            if i == 0:
                continue
            if X + i >= 0 and X + i < 8 and Y + i >= 0 and Y + i < 8:
                moves.append((X + i, Y + i))
            if X + i >= 0 and X + i < 8 and Y - i >= 0 and Y - i < 8:
                moves.append((X + i, Y - i))

        return moves

class knight(piece):
    def move(self, x, y):
        '''X and Y are the current position'''
        X, Y = self.pos

        if not isinstance(x, int) or not isinstance(y, int):
            return False

        pos_mov = self.possible_moves()

        if (x, y) in pos_mov:
            if valide_move((x, y)) == False:
                return False

            self.pos = (x, y)
            return True

        return False

    def possible_moves(self):
        '''all possible moves for knight'''
        X, Y = self.pos
        moves = []

        # Knight moves
        knight_moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

        for move in knight_moves:
            new_x = X + move[0]
            new_y = Y + move[1]
            if new_x >= 0 and new_x < 8 and new_y >= 0 and new_y < 8:
                moves.append((new_x, new_y))

        return moves

class rock(piece):
    def move(self, x, y):
        '''X and Y are the current position'''
        X, Y = self.pos

        if not isinstance(x, int) or not isinstance(y, int):
            return False

        pos_mov = self.possible_moves()

        if (x, y) in pos_mov:
            if valide_move((x, y)) == False:
                return False

            self.pos = (x, y)
            return True

        return False

    def possible_moves(self):
        '''all possible moves for rock'''
        X, Y = self.pos
        moves = []

        # Horizontal and vertical moves
        for i in range(8):
            if i != X:
                moves.append((i, Y))
            if i != Y:
                moves.append((X, i))

        return moves


# add pieces images:
b_pawn_im = pygame.image.load("./image/b_pawn.png")
w_pawn_im = pygame.image.load("./image/w_pawn.png")

w_quuen_im = pygame.image.load("./image/w_quuen.png")
b_quuen_im = pygame.image.load("./image/b_quuen.png")

b_king_im = pygame.image.load("./image/b_king.png")
w_king_im = pygame.image.load("./image/w_king.png")

b_bishop_im = pygame.image.load("./image/b_bishop.png")
w_bishop_im = pygame.image.load("./image/w_bishop.png")

b_knight_im = pygame.image.load("./image/b_knight.png")
w_knight_im = pygame.image.load("./image/w_knight.png")

b_rock_im = pygame.image.load("./image/b_rock.png")
w_rock_im = pygame.image.load("./image/w_rock.png")


# Set the black pawns
b_pawns = [pawn("black", pos=(i, 1), p_icon=b_pawn_im) for i in range(8)]

# Set kings
kings = [king("black", pos=(4, 0), p_icon=b_king_im), king("white", pos=(4, 7), p_icon=w_king_im)]

# Set queens
queens = [queen("black", pos=(3, 0), p_icon=b_quuen_im), queen("white", pos=(3, 7), p_icon=w_quuen_im)]

# Set knights
knights = [knight("white", pos=(1, 7), p_icon=w_knight_im), knight("white", pos=(6, 7), p_icon=w_knight_im),
           knight("black", pos=(1, 0), p_icon=b_knight_im), knight("black", pos=(6, 0), p_icon=b_knight_im)]

# Set bishops
bishops = [bishop("white", pos=(2, 7), p_icon=w_bishop_im), bishop("white", pos=(5, 7), p_icon=w_bishop_im),
           bishop("black", pos=(2, 0), p_icon=b_bishop_im), bishop("black", pos=(5, 0), p_icon=b_bishop_im)]

# Set rocks
rocks = [rock("white", pos=(0, 7), p_icon=w_rock_im), rock("white", pos=(7, 7), p_icon=w_rock_im),
         rock("black", pos=(0, 0), p_icon=b_rock_im), rock("black", pos=(7, 0), p_icon=b_rock_im)]

# Set the white pawns
w_pawns = [pawn("white", pos=(i, 6), p_icon=w_pawn_im) for i in range(8)]

# List containing lists of all the pieces of the game
board_pieces = [kings, b_pawns, w_pawns, queens, knights, bishops, rocks]


def valide_move(move=(0,0)):
    # check if the move is valid
    for board_piece in board_pieces:
        for each in board_piece:
            if (move == each.pos):
                return False
    return True

def get_piece_at(move=(0,0)):
    ''' return the index of the piece at the given position'''

    for i,board_piece in enumerate(board_pieces):
        # each board_piece is a list of pieces of the same color and type
        for j,each in enumerate(board_piece):
            # each is a piece object
            if (move == each.pos):
                return ((i,j))
    return False

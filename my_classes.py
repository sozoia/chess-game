from display import *
import pygame

class piece:

    def __init__(self, color, p_icon="none", pos=(0,0), life=True):
        self.color = color
        self.pos = pos
        self.life = life
        self.p_icon = p_icon
        self.first_move = True

class pawn(piece):

    def move(self, x, y):
        X, Y = self.pos

        if not isinstance(x, int) or not isinstance(y, int):
            return False
        if self.color is "white":
            '''so that it go in the oppset dirction'''
            x *= -1
            y *= -1

        # Check for eating positions
        if  (valide_move((X + 1, Y + 1) != True) and x == X+1 and y == Y+1):
            self.pos = (x, y)
            self.first_move = False
            return True
        elif not valide_move((X - 1, Y + 1)) and  x == X-1 and y == Y+1:
            self.pos = (x, y)
            self.first_move = False
            return True

        if (x != X):
            return False
        elif (y - Y == 2 and self.first_move):
            self.pos = (x,y)
            self.first_move = False
            return True

        elif (y < Y):
            return False
        elif (y > Y and y - Y == 1):
            self.pos = (x, y)
            self.first_move = False
            return True
        return False

    def possible_moves(self):
        '''all valid moves for pawn '''

        X,Y = self.pos
        valid = []

        valid.append((X,Y+1))
        valid.append(X,Y+1)
        valid.append(X+1,Y+1)
        valid.append(X-1,Y+1)
        return valid
    



class queen(piece):

    def move():
        return(True)

class king(piece):
    pass
class bishop(piece):
    pass
class knight(piece):
    pass
class rock(piece):
    pass


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


'''set the black pawns:'''
bp1 = pawn("black", pos = (0,1), p_icon=b_pawn_im)
bp2 = pawn("black", pos = (1,1), p_icon=b_pawn_im)
bp3 = pawn("black", pos = (2,1), p_icon=b_pawn_im)
bp4 = pawn("black", pos = (3,1), p_icon=b_pawn_im)
bp5 = pawn("black", pos = (4,1), p_icon=b_pawn_im)
bp6 = pawn("black", pos = (5,1), p_icon=b_pawn_im)
bp7 = pawn("black", pos = (6,1), p_icon=b_pawn_im)
bp8 = pawn("black", pos = (7,1), p_icon=b_pawn_im)
b_pawns = [bp1, bp2, bp3,bp4,bp5, bp6, bp7, bp8]


'''set kings'''
b_king = king("black",pos=(4,0), p_icon=b_king_im)
w_king = king("white",pos=(4,7), p_icon=w_king_im)
kings = [b_king, w_king]


'''set queens'''
b_queen = queen("black",pos=(3,0), p_icon=b_quuen_im)
w_queen = queen("white",pos=(3,7), p_icon=w_quuen_im)
queens = [b_queen, w_queen]


'''set knights'''
w_knight1 = knight("white",pos=(1,7), p_icon=w_knight_im)
w_knight2 = knight("white",pos=(6,7), p_icon=w_knight_im)
b_knight1 = knight("black",pos=(1,0), p_icon=b_knight_im)
b_knight2 = knight("black",pos=(6,0), p_icon=b_knight_im)
knights = [w_knight1, w_knight2, b_knight1, b_knight2]


'''set bishops'''
w_bishop1 = bishop("white",pos=(2,7), p_icon=w_bishop_im)
w_bishop2 = bishop("white",pos=(5,7), p_icon=w_bishop_im)
b_bishop1 = bishop("black",pos=(2,0), p_icon=b_bishop_im)
b_bishop2 = bishop("black",pos=(5,0), p_icon=b_bishop_im)
bishops = [w_bishop1, w_bishop2, b_bishop1, b_bishop2]


'''set rocks'''
w_rock1 = rock("white",pos=(0,7), p_icon=w_rock_im)
w_rock2 = rock("white",pos=(7,7), p_icon=w_rock_im)
b_rock1 = rock("black",pos=(0,0), p_icon=b_rock_im)
b_rock2 = rock("black",pos=(7,0), p_icon=b_rock_im)
rocks = [w_rock1, w_rock2, b_rock1, b_rock2]


'''set the white pawns:'''
wp1 = pawn("white", pos = (0,6), p_icon=w_pawn_im)
wp2 = pawn("white", pos = (1,6), p_icon=w_pawn_im)
wp3 = pawn("white", pos = (2,6), p_icon=w_pawn_im)
wp4 = pawn("white", pos = (3,6), p_icon=w_pawn_im)
wp5 = pawn("white", pos = (4,6), p_icon=w_pawn_im)
wp6 = pawn("white", pos = (5,6), p_icon=w_pawn_im)
wp7 = pawn("white", pos = (6,6), p_icon=w_pawn_im)
wp8 = pawn("whtie", pos = (7,6), p_icon=w_pawn_im)
w_pawns = [wp1, wp2, wp3,wp4,wp5, wp6, wp7, wp8]


''' list contain lists of all the pieces of the game'''
board_pieces = [kings,b_pawns, w_pawns, queens, knights, bishops, rocks]


def valide_move(move=(0,0)):

    for board_piece in board_pieces:
        for each in board_piece:
            if (move == each.pos):
                return False
    return True

def get_piece_at(move=(0,0)):

    for i,board_piece in enumerate(board_pieces):
        for j,each in enumerate(board_piece):
            if (move == each.pos):
                return ((i,j))
    return False
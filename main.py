import chess
import chess.engine
import os
import sys
from Chessnut import Game

Knight = 3 pawns (3 points)
Bishop = knight (3 points)
Rook = knight plus 2 pawns (5 points)
queen = 2 rooks = 3 knights (10 or 9 points)
king = the game. 

#Let's try with the positions(fen):
fen = str(input('FEN, pls: '))

board = chess.Board(fen)

chessgame = Game(fen)
white = 20
black = 20
# the correct location for the stockfish engine file
engine = chess.engine.SimpleEngine.popen_uci('Windows/stockfish_11_x64')

if board.turn:
    print('White to move \n')
    print(board)

else:
    print('black to move\n', board)
    print(board)

for el in board.legal_moves:
    info = engine.analyse(board, chess.engine.Limit(time=1), root_moves=[el])
    t = str(info["score"])

    if t.startswith('#'):
        print('\n', str(board.san(el)), " eval = mate in ", t)
    else:
        print('\n', str(board.san(el)), " eval = ", round(int(t) / 100., 2))

if board.is_game_over():
    #print(board.is_game_over())
    print('the game introduced, has been won.')
    sys.exit()

if 'rnbqkbnr' and 'RNBQKBNR' in fen:
    print('black and WHITE have all of its peaces')
else:
    n = fen.count('r')
    if 'r' in fen:
        if n < 2:
            black -= 5
            white += 5
        n = fen.count('n')
    if 'n' in fen:
        if n < 2:
            black -= 3
            white += 3
        n = fen.count('b')
    if 'b' in fen:
        if n < 2:
            black -= 3
            white += 3
        n = fen.count('q')
    if 'q' in fen:
        if n < 2:
            black -= 9
            white += 9
    if 'p' in fen:
        n = fen.count('p')
        if n < 8:
            black -= 1
            white += 1

    print('Black has ', black, ' points')
    n = fen.count('R')
    if 'R' in fen:
        if n < 2:
            white -= 5
            black += 5
        n = fen.count('N')
    if 'N' in fen:
        if n < 2:
            white -= 3
            black += 3
        n = fen.count('B')
    if 'B' in fen:
        if n < 2:
            white -= 3
            black += 3
        n = fen.count('Q')
    if 'Q' in fen:
        if n < 2:
            white -= 9
            black += 9
    if 'P' in fen:
        n = fen.count('P')
        if n < 8:
            white -= 1
            black += 1
    print('White has ', white, ' points')

#engine.quit()

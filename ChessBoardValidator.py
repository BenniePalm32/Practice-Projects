# This program contains a function that will validate that the chessboard and the pieces on the board are valid
# 1. All pieces must be on a valid space from '1a' to '8h'
# 2. One black king and exactly one white king on the board at all times
# 3. Each player can only have at most 16 pieces, at most 8 pawns

def isValidChessBoard(board):
    validBoard = {'8a': '', '8b': '', '8c': '', '8d': '', '8e': '', '8f': '', '8g': '', '8h': '',
                  '7a': '', '7b': '', '7c': '', '7d': '', '7e': '', '7f': '', '7g': '', '7h': '',
                  '6a': '', '6b': '', '6c': '', '6d': '', '6e': '', '6f': '', '6g': '', '6h': '',
                  '5a': '', '5b': '', '5c': '', '5d': '', '5e': '', '5f': '', '5g': '', '5h': '',
                  '4a': '', '4b': '', '4c': '', '4d': '', '4e': '', '4f': '', '4g': '', '4h': '',
                  '3a': '', '3b': '', '3c': '', '3d': '', '3e': '', '3f': '', '3g': '', '3h': '',
                  '2a': '', '2b': '', '2c': '', '2d': '', '2e': '', '2f': '', '2g': '', '2h': '',
                  '1a': '', '1b': '', '1c': '', '1d': '', '1e': '', '1f': '', '1g': '', '1h': '',}
    
    pieceColor = 'wb' 
    pieceCount = {'wking': 0, 'bking': 0, 'wpawn': 0, 'bpawn': 0}
    validPieces = {'king', 'queen', 'rook', 'bishop', 'knight', 'pawn'}
    blackPieces = 0
    whitePieces = 0

    for position, piece in board.items():
        if position not in validBoard:
            print(f'Invalid spot: {position}')
            return False
        
        if  len(piece) < 2 or piece[0] not in pieceColor or piece[1:] not in validPieces:
            print(f'Invalid piece: {piece} at position: {position}')
            return False
        
        if piece in pieceCount:
            pieceCount[piece] += 1

        if piece[0] == 'w':
            whitePieces += 1
        elif piece[0] == 'b':
            blackPieces += 1

    if pieceCount['wpawn'] > 8 or pieceCount['bpawn'] > 8:
        print('One side has too many pawns on the board')
        return False
    if pieceCount['wking'] != 1 or pieceCount['bking'] != 1:
        print('Invalid amount of kings on the board')
        return False
    if blackPieces > 16 or whitePieces > 16:
        print('One side has too many pieces on the board')
        return False
    
    print('This is a valid chessboard')

#------------------------------Main Code--------------------------------#

chessBoard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '1e': 'wking'} 

isValidChessBoard(chessBoard)

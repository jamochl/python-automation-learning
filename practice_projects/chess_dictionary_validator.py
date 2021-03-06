#!/bin/env python

# The objective is to create a function to validate a chess board that is
# described by a dictionary data structure

# The data structure involves keys from '1a' to '8h', which are in string
# format, and values of which the first character is 'w' for white or 'b' for
# black, followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'

# We want to do this without Regex for now (That would be easier)

# A player can have at most 16 pieces and 8 pawns

# Each player must have 1 king

# SAMPLE DICTIONARIES

valid_board = {
    '1a': 'bknight',
    '2g': 'wking',
    '8h': 'bbishop',
    '4b': 'wrook',
    '5c': 'bqueen',
    '6d': 'wknight',
    '7e': 'bking',
}

simplest_valid_board = {
    '7e': 'bking',
    '2g': 'wking',
}


board_too_many_pieces = {
    '1a': 'bknight',
    '2a': 'bknight',
    '3a': 'bknight',
    '4a': 'bknight',
    '5a': 'bknight',
    '6a': 'bknight',
    '7a': 'bknight',
    '8a': 'bknight',
    '1b': 'bknight',
    '2b': 'bknight',
    '3b': 'bknight',
    '4b': 'bknight',
    '5b': 'bknight',
    '6b': 'bknight',
    '7b': 'bknight',
    '8b': 'bknight',
    '1c': 'bknight',
    '4b': 'wking',
    '7e': 'bking',
}

board_missing_king = {
    '1a': 'bknight',
    '8h': 'bbishop',
    '4b': 'wrook',
    '5c': 'bqueen',
    '6d': 'wknight',
    '7e': 'bking',
}

# Returns a bool validation
def validate_chess(board) -> bool:
    valid_pieces = ('pawn', 'knight', 'bishop', 'rook', 'queen', 'king')

    player_statistics = {
        'w': {
            'num': 0,
            'pawns': 0,
            'kings': 0
        },
        'b': {
            'num': 0,
            'pawns': 0,
            'kings': 0
        }
    }

    for key, value in board.items():
        # Validate the key
        num_coor = int(key[0])
        str_coor = key[1]
        if num_coor < 1 or num_coor > 8 or str_coor < 'a' or str_coor > 'h':
            return False

        # Validate the value
        player = value[0]
        if player != 'w' and player != 'b':
            return False

        # Validate the piece
        piece = value[1:]
        if piece not in valid_pieces:
            return False

        # Determine 'num', 'pawns' and 'kings'
        player_statistics[player]['num'] += 1

        if piece == 'pawn':
            player_statistics[player]['pawns'] += 1
        elif piece == 'king':
            player_statistics[player]['kings'] += 1

    # Validate the number of pieces
    for player_dict in player_statistics.values():
        if player_dict['num'] > 16 or \
           player_dict['pawns'] > 8 or \
           player_dict['kings'] != 1:
            return False

    # Default return true if tests pass
    return True


print(validate_chess(valid_board))
print(validate_chess(simplest_valid_board))
print(validate_chess(board_missing_king))
print(validate_chess(board_too_many_pieces))

#!/usr/bin/env python
#
# Copyright (c) 2019 Maria Bornski
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

# Standard library modules
import argparse
import pdb

EMPTY_SPACE = "*"
PLAYER_X = "X"
PLAYER_O = "O"

def get_empty_board():
    board = [[EMPTY_SPACE,EMPTY_SPACE, EMPTY_SPACE],[EMPTY_SPACE,EMPTY_SPACE, EMPTY_SPACE],[EMPTY_SPACE, EMPTY_SPACE, EMPTY_SPACE]]
    return board

def record_move(board, row, column, player):
    if board[row][column] == EMPTY_SPACE:
        board[row][column] = player
        return board
    else:
        return board

def pretty_print_board(board):
    print(board[0][0], board[0][1], board[0][2])
    print(board[1][0], board[1][1], board[1][2])
    print(board[2][0], board[2][1], board[2][2])

def is_there_a_winner(board):
    winner = "none"
    game_over = False

    if (board[0][0] == board[0][1] == board[0][2] and not (board[0][0] == EMPTY_SPACE)):
        game_over = True
        winner = board[0][1]

    return (game_over,winner)

def is_valid_location(loc):
    return (loc >= 0 and loc <= 2)

def get_move_location():

    row = int(input("What row (0, 1, 2) would you like?: "))
    column = int(input("What column (0, 1, 2) would you like?: "))
    
    while not is_valid_location(row):
        row = int(input("Your row is invalid, please try again: "))
    while not is_valid_location(column):
        column = int(input("Your column is invalid, please try again: "))
    return (row, column)

def are_boards_identical(boardA, boardB):
    for r in range(3):
        for c in range(3):
            if boardA[r][c] != boardB[r][c]:
                return False
    return True

def copy_board(old_board):
    new_board = get_empty_board()
    for r in range(3):
        for c in range(3):
            new_board[r][c] = old_board[r][c]
    return new_board


def main():
    board = get_empty_board()
    game_over = False
    current_player = PLAYER_X
    while not game_over:
        print("The current board is:")
        pretty_print_board(board)
        print("The current player is:", current_player)

        old_board = copy_board(board)
        (row, column) = get_move_location()
        board = record_move(board, row, column, current_player)
        pretty_print_board(board)
        while (are_boards_identical(board, old_board)):
            print("Space is already occupied, please choose a different space")
            (row, column) = get_move_location()
            board = record_move(board, row, column, current_player)
        

        (game_over, winner) = is_there_a_winner(board)
        current_player = PLAYER_X if current_player == PLAYER_O else PLAYER_O

    print(winner, "wins!")
    exit(0)


if __name__ == "__main__":
    main()

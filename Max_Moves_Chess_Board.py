import copy

from Knight_moves import workout_next_square, is_square_free, does_move_cross_path

# specify size of the board (default 8 * 8)
# must be a square board but could be extended to support rectangles
board_size = 8
chess_board_array = [[0 for _ in range(board_size)] for _ in range(board_size)]

# specify x & y values of the square the knight will start from
# axis values range from 0 to (board_size - 1)
current_square = [int(3), int(3)]
current_direction = chess_board_array[current_square[0]][current_square[1]]
list_of_moves = []
longest_path_board = []
longest_list_of_moves = []
count_iterations = 0


def workout_next_direction(current_square_coordinates, chess_board_values):
    global longest_list_of_moves, longest_path_board, list_of_moves, count_iterations
    next_direction = chess_board_values[current_square_coordinates[0]][current_square_coordinates[1]] + 1

    while next_direction <= 8:
        next_square_coordinates = workout_next_square(current_square_coordinates, next_direction)

        if (is_square_free(next_square_coordinates, chess_board_values, board_size) and
                not does_move_cross_path(current_square_coordinates, next_direction, chess_board_values, board_size)):
            chess_board_values[current_square_coordinates[0]][current_square_coordinates[1]] = next_direction
            list_of_moves.append(next_direction)

            if len(list_of_moves) > len(longest_list_of_moves):
                longest_list_of_moves = copy.copy(list_of_moves)
                longest_path_board = copy.deepcopy(chess_board_values)
                print("longest list of moves " + str(longest_list_of_moves))
                for r in range(board_size): print(longest_path_board[r])

            new_next_square_coordinates = copy.copy(next_square_coordinates)
            new_chess_board_values = copy.deepcopy(chess_board_values)
            workout_next_direction(new_next_square_coordinates, new_chess_board_values)
            list_of_moves.pop()

        next_direction = next_direction + 1
        count_iterations = count_iterations + 1


workout_next_direction(current_square, chess_board_array)
print("The longest list of moves " + str(longest_list_of_moves))
for m in range(board_size): print(longest_path_board[m])


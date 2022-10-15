def workout_next_square(square, direction) -> (int, int):
    if direction == 1:
        return [square[0] + 1, square[1] + 2]
    elif direction == 2:
        return square[0] + 2, square[1] + 1
    elif direction == 3:
        return square[0] + 2, square[1] - 1
    elif direction == 4:
        return square[0] + 1, square[1] - 2
    elif direction == 5:
        return square[0] - 1, square[1] - 2
    elif direction == 6:
        return square[0] - 2, square[1] - 1
    elif direction == 7:
        return square[0] - 2, square[1] + 1
    elif direction == 8:
        return square[0] - 1, square[1] + 2


def is_square_free(square_coordinates, chess_board_values, board_size):
    if 0 <= square_coordinates[0] <= (board_size - 1) and 0 <= square_coordinates[1] <= (board_size - 1):
        if chess_board_values[square_coordinates[0]][square_coordinates[1]] == 0:
            return True
    else:
        return False


def does_move_cross_path(current_square, direction, chess_board_values, board_size):
    def lookup_board(square_x, square_y, square_values):
        if 0 <= square_x <= board_size - 1 and 0 <= square_y <= board_size - 1:
            return square_values[square_x][square_y]
        else:
            return 99
    if direction == 1:
        return does_direction_1_cross_path(current_square, lookup_board, chess_board_values)
    elif direction == 2:
        return does_direction_2_cross_path(current_square, lookup_board, chess_board_values)
    elif direction == 3:
        return does_direction_3_cross_path(current_square, lookup_board, chess_board_values)
    elif direction == 4:
        return does_direction_4_cross_path(current_square, lookup_board, chess_board_values)
    elif direction == 5:
        return does_direction_5_cross_path(current_square, lookup_board, chess_board_values)
    elif direction == 6:
        return does_direction_6_cross_path(current_square, lookup_board, chess_board_values)
    elif direction == 7:
        return does_direction_7_cross_path(current_square, lookup_board, chess_board_values)
    elif direction == 8:
        return does_direction_8_cross_path(current_square, lookup_board, chess_board_values)


def does_direction_1_cross_path(current_square, lookup_chess_board, chess_board_values):
    if (lookup_chess_board(current_square[0] - 1, current_square[1], chess_board_values) == 2 or
            lookup_chess_board(current_square[0] - 1, current_square[1] + 1, chess_board_values) == 3 or
            lookup_chess_board(current_square[0] - 1, current_square[1] + 2, chess_board_values) == 3 or
            lookup_chess_board(current_square[0], current_square[1] + 1, chess_board_values) in (2, 3, 4) or
            lookup_chess_board(current_square[0], current_square[1] + 2, chess_board_values) in (3, 4) or
            lookup_chess_board(current_square[0], current_square[1] + 3, chess_board_values) == 4 or
            lookup_chess_board(current_square[0] + 1, current_square[1] - 1, chess_board_values) == 8 or
            lookup_chess_board(current_square[0] + 1, current_square[1], chess_board_values) in (7, 8) or
            lookup_chess_board(current_square[0] + 1, current_square[1] + 1, chess_board_values) in (6, 7, 8) or
            lookup_chess_board(current_square[0] + 2, current_square[1], chess_board_values) == 7 or
            lookup_chess_board(current_square[0] + 2, current_square[1] + 1, chess_board_values) == 7 or
            lookup_chess_board(current_square[0] + 2, current_square[1] + 2, chess_board_values) == 6):
        return True
    else:
        return False


def does_direction_2_cross_path(current_square, lookup_chess_board, chess_board_values):
    if (lookup_chess_board(current_square[0], current_square[1] + 1, chess_board_values) in (3, 4) or
            lookup_chess_board(current_square[0] + 1, current_square[1] + 1, chess_board_values) in (3, 4, 5) or
            lookup_chess_board(current_square[0] + 1, current_square[1], chess_board_values) in (1, 7, 8) or
            lookup_chess_board(current_square[0] + 2, current_square[1], chess_board_values) in (7, 8) or
            lookup_chess_board(current_square[0] + 3, current_square[1], chess_board_values) == 7 or
            lookup_chess_board(current_square[0] - 1, current_square[1] + 1, chess_board_values) == 3 or
            lookup_chess_board(current_square[0], current_square[1] + 2, chess_board_values) == 4 or
            lookup_chess_board(current_square[0] + 1, current_square[1] + 2, chess_board_values) == 4 or
            lookup_chess_board(current_square[0] + 2, current_square[1] + 2, chess_board_values) == 5 or
            lookup_chess_board(current_square[0], current_square[1] - 1, chess_board_values) == 1 or
            lookup_chess_board(current_square[0] + 1, current_square[1] - 1, chess_board_values) == 8 or
            lookup_chess_board(current_square[0] + 2, current_square[1] - 1, chess_board_values) == 8):
        return True
    else:
        return False


def does_direction_3_cross_path(current_square, lookup_chess_board, chess_board_values):
    if (lookup_chess_board(current_square[0] - 1, current_square[1] - 1, chess_board_values) == 2 or
            lookup_chess_board(current_square[0], current_square[1] - 2, chess_board_values) == 1 or
            lookup_chess_board(current_square[0], current_square[1] - 1, chess_board_values) in (1, 2) or
            lookup_chess_board(current_square[0], current_square[1] + 1, chess_board_values) == 4 or
            lookup_chess_board(current_square[0] + 1, current_square[1] - 2, chess_board_values) == 1 or
            lookup_chess_board(current_square[0] + 1, current_square[1] - 1, chess_board_values) in (1, 2, 8) or
            lookup_chess_board(current_square[0] + 1, current_square[1], chess_board_values) in (4, 5, 6) or
            lookup_chess_board(current_square[0] + 1, current_square[1] + 1, chess_board_values) == 5 or
            lookup_chess_board(current_square[0] + 2, current_square[1] - 2, chess_board_values) == 8 or
            lookup_chess_board(current_square[0] + 2, current_square[1], chess_board_values) in (5, 6) or
            lookup_chess_board(current_square[0] + 2, current_square[1] + 1, chess_board_values) == 5 or
            lookup_chess_board(current_square[0] + 3, current_square[1], chess_board_values) == 6):
        return True
    else:
        return False


def does_direction_4_cross_path(current_square, lookup_chess_board, chess_board_values):
    if (lookup_chess_board(current_square[0] - 1, current_square[1] - 2, chess_board_values) == 2 or
            lookup_chess_board(current_square[0] - 1, current_square[1] - 1, chess_board_values) == 2 or
            lookup_chess_board(current_square[0] - 1, current_square[1], chess_board_values) == 3 or
            lookup_chess_board(current_square[0], current_square[1] - 1, chess_board_values) in (1, 2, 3) or
            lookup_chess_board(current_square[0], current_square[1] - 2, chess_board_values) in (1, 2) or
            lookup_chess_board(current_square[0], current_square[1] - 3, chess_board_values) == 1 or
            lookup_chess_board(current_square[0] + 1, current_square[1] + 1, chess_board_values) == 5 or
            lookup_chess_board(current_square[0] + 1, current_square[1], chess_board_values) in (5, 6) or
            lookup_chess_board(current_square[0] + 1, current_square[1] - 1, chess_board_values) in (5, 6, 7) or
            lookup_chess_board(current_square[0] + 2, current_square[1], chess_board_values) == 6 or
            lookup_chess_board(current_square[0] + 2, current_square[1] - 1, chess_board_values) == 6 or
            lookup_chess_board(current_square[0] + 2, current_square[1] - 2, chess_board_values) == 7):
        return True
    else:
        return False


def does_direction_5_cross_path(current_square, lookup_chess_board, chess_board_values):
    if (lookup_chess_board(current_square[0] - 2, current_square[1] - 2, chess_board_values) == 2 or
            lookup_chess_board(current_square[0] - 2, current_square[1] - 1, chess_board_values) == 3 or
            lookup_chess_board(current_square[0] - 2, current_square[1], chess_board_values) == 3 or
            lookup_chess_board(current_square[0] - 1, current_square[1] - 1, chess_board_values) in (2, 3, 4) or
            lookup_chess_board(current_square[0] - 1, current_square[1], chess_board_values) in (3, 4) or
            lookup_chess_board(current_square[0] - 1, current_square[1] + 1, chess_board_values) == 4 or
            lookup_chess_board(current_square[0], current_square[1] - 3, chess_board_values) == 8 or
            lookup_chess_board(current_square[0], current_square[1] - 2, chess_board_values) in (7, 8) or
            lookup_chess_board(current_square[0], current_square[1] - 1, chess_board_values) in (6, 7, 8) or
            lookup_chess_board(current_square[0] + 1, current_square[1] - 2, chess_board_values) == 7 or
            lookup_chess_board(current_square[0] + 1, current_square[1] - 1, chess_board_values) == 7 or
            lookup_chess_board(current_square[0] + 1, current_square[1], chess_board_values) == 6):
        return True
    else:
        return False


def does_direction_6_cross_path(current_square, lookup_chess_board, chess_board_values):
    if (lookup_chess_board(current_square[0] - 3, current_square[1], chess_board_values) == 3 or
            lookup_chess_board(current_square[0] - 2, current_square[1] - 2, chess_board_values) == 1 or
            lookup_chess_board(current_square[0] - 2, current_square[1], chess_board_values) in (3, 4) or
            lookup_chess_board(current_square[0] - 2, current_square[1] + 1, chess_board_values) == 4 or
            lookup_chess_board(current_square[0] - 1, current_square[1] - 2, chess_board_values) == 8 or
            lookup_chess_board(current_square[0] - 1, current_square[1] - 1, chess_board_values) in (1, 7, 8) or
            lookup_chess_board(current_square[0] - 1, current_square[1], chess_board_values) in (3, 4, 5) or
            lookup_chess_board(current_square[0] - 1, current_square[1] + 1, chess_board_values) == 4 or
            lookup_chess_board(current_square[0], current_square[1] - 2, chess_board_values) == 8 or
            lookup_chess_board(current_square[0], current_square[1] - 1, chess_board_values) in (7, 8) or
            lookup_chess_board(current_square[0], current_square[1] + 1, chess_board_values) == 5 or
            lookup_chess_board(current_square[0] + 1, current_square[1] - 1, chess_board_values) == 7):
        return True
    else:
        return False


def does_direction_7_cross_path(current_square, lookup_chess_board, chess_board_values):
    if (lookup_chess_board(current_square[0] - 3, current_square[1], chess_board_values) == 2 or
            lookup_chess_board(current_square[0] - 2, current_square[1] - 1, chess_board_values) == 1 or
            lookup_chess_board(current_square[0] - 2, current_square[1], chess_board_values) in (1, 2) or
            lookup_chess_board(current_square[0] - 2, current_square[1] + 2, chess_board_values) == 4 or
            lookup_chess_board(current_square[0] - 1, current_square[1] - 1, chess_board_values) == 1 or
            lookup_chess_board(current_square[0] - 1, current_square[1], chess_board_values) in (1, 2, 8) or
            lookup_chess_board(current_square[0] - 1, current_square[1] + 1, chess_board_values) in (4, 5, 6) or
            lookup_chess_board(current_square[0] - 1, current_square[1] + 2, chess_board_values) == 5 or
            lookup_chess_board(current_square[0], current_square[1] - 1, chess_board_values) == 8 or
            lookup_chess_board(current_square[0], current_square[1] + 1, chess_board_values) in (5, 6) or
            lookup_chess_board(current_square[0], current_square[1] + 2, chess_board_values) == 5 or
            lookup_chess_board(current_square[0] + 1, current_square[1] + 1, chess_board_values) == 6):
        return True
    else:
        return False


def does_direction_8_cross_path(current_square, lookup_chess_board, chess_board_values):
    if (lookup_chess_board(current_square[0] - 2, current_square[1], chess_board_values) == 2 or
            lookup_chess_board(current_square[0] - 2, current_square[1] + 1, chess_board_values) == 2 or
            lookup_chess_board(current_square[0] - 2, current_square[1] + 2, chess_board_values) == 3 or
            lookup_chess_board(current_square[0] - 1, current_square[1] - 1, chess_board_values) == 1 or
            lookup_chess_board(current_square[0] - 1, current_square[1], chess_board_values) in (1, 2) or
            lookup_chess_board(current_square[0] - 1, current_square[1] + 1, chess_board_values) in (1, 2, 3) or
            lookup_chess_board(current_square[0], current_square[1] + 1, chess_board_values) in (5, 6, 7) or
            lookup_chess_board(current_square[0], current_square[1] + 2, chess_board_values) in (5, 6) or
            lookup_chess_board(current_square[0], current_square[1] + 3, chess_board_values) == 5 or
            lookup_chess_board(current_square[0] + 1, current_square[1], chess_board_values) == 7 or
            lookup_chess_board(current_square[0] + 1, current_square[1] + 1, chess_board_values) == 6 or
            lookup_chess_board(current_square[0] + 1, current_square[1] + 2, chess_board_values) == 6):
        return True
    else:
        return False

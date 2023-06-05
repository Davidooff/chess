from pieces_logic import check_vertical_and_horizontal, check_diagonal, knight, get_enemy_color


def is_watching(coordinate, color, board, youre_color):  # coordinate = {x,y}
    global check_vertical_and_horizontal, check_diagonal
    piece_color = get_enemy_color(color)
    knight_posible_ways = knight(
        coordinate["x"], coordinate["y"], color, board)
    for posible_way in knight_posible_ways:
        if "square-" + str(posible_way["x"]) + str(posible_way["y"]) in board[piece_color]:
            if board[piece_color]["square-" + str(posible_way["x"]) + str(posible_way["y"])] == "n":
                return True

    horizontal_ways = check_vertical_and_horizontal(
        coordinate["x"], coordinate["y"], color, board)
    for horizontal_way in horizontal_ways:
        if "square-" + str(horizontal_way["x"]) + str(horizontal_way["y"]) in board[piece_color]:
            piece = board[piece_color]["square-" +
                                       str(horizontal_way["x"]) + str(horizontal_way["y"])]
            if piece == "r" or piece == "q":
                return True

    diagonal_ways = check_diagonal(
        coordinate["x"], coordinate["y"], color, board)
    for diagonal_way in diagonal_ways:
        if "square-" + str(diagonal_way["x"]) + str(diagonal_way["y"]) in board[piece_color]:
            piece = board[piece_color]["square-" +
                                       str(diagonal_way["x"]) + str(diagonal_way["y"])]
            if piece == "b" or piece == "q":
                return True
            if piece == "p":
                if youre_color == "white":
                    a = -1
                else:
                    a = 1
                if piece_color == "white":
                    if coordinate["y"] + a == diagonal_way["y"]:
                        return True
                else:
                    if coordinate["y"] - a == diagonal_way["y"]:
                        return True
    return False

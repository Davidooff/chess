from pieces_logic import check_vertical_and_horizontal, check_diagonal, knight, get_enemy_color

def is_watching(coordinate, color, board): #coordinate = {x,y}
    global check_diagonal, knight
    color_inversed = get_enemy_color(color) # bks every def bottom inverting color for logic
    vertical_and_horizontals = check_vertical_and_horizontal(coordinate["x"], coordinate["y"], color_inversed, board)
    for vertical_and_horizontal in vertical_and_horizontals:
        piece = board[color]["square-" + str(vertical_and_horizontal["x"]) + str(vertical_and_horizontal["y"])]
        if piece == "q" and piece == "r":
            return True
    
    check_diagonals = check_diagonal(coordinate["x"], coordinate["y"], color_inversed, board)
    
    for check_diagonal in check_diagonals:
        piece = board[color]["square-" + str(check_diagonal["x"]) + str(check_diagonal["y"])]
        if piece == "q" and piece == "b":
            return True
        if piece == "p":
            if color == "white":
                if str(check_diagonal["y"]) == check_diagonal["y"] + 1:
                    return True
            else:
                if str(check_diagonal["y"]) == check_diagonal["y"] - 1:
                    return True
    
    knights = knight(coordinate["x"], coordinate["y"], color_inversed, board)

    for knight in knights:
        piece = board[color]["square-" + str(knight["x"]) + str(knight["y"])]
        if piece == "n":
            return True
        

    return False
def get_enemy_color(color):
    if color == 'white':
        enemy_color = 'black'
    else:
        enemy_color = 'white'
    return enemy_color
    

def check_vertical_and_horizontal(x, y, color, board):
    enemy_color = get_enemy_color(color)

    addHighlitesDict = []
    x_temp = x
    while x_temp < 8: # check on x on board (from x to 8)
        x_temp += 1
        if "square-" + str(x_temp) + str(y) in board[color]:
            break
        elif "square-" + str(x_temp) + str(y) in board[enemy_color]:
            addHighlitesDict.append({'x': x_temp, 'y':y})
            break
    x_temp = x
    while x_temp > 0: # check on x on board (from x to 0)
        x_temp -= 1
        if "square-" + str(x_temp) + str(y) in board[color]:
            break
        elif "square-" + str(x_temp) + str(y) in board[enemy_color]:
            addHighlitesDict.append({'x': x_temp, 'y':y})
            break

    y_temp = y
    while y_temp < 8: # check on y on board (from y to 8)
        y_temp += 1
        if "square-" + str(x) + str(y_temp) in board[color]:
            break
        elif "square-" + str(x) + str(y_temp) in board[enemy_color]:
            addHighlitesDict.append({'x': x, 'y':y_temp})
            break
    y_temp = y
    while y_temp > 0: # check on y on board (from y to 0)
        y_temp -= 1
        if "square-" + str(x) + str(y_temp) in board[color]:
            break
        elif "square-" + str(x) + str(y_temp) in board[enemy_color]:
            addHighlitesDict.append({'x': x, 'y':y_temp})
            break
    return addHighlitesDict

def check_diagonal(x,y, color, board):
    enemy_color = get_enemy_color(color)
    addHighlitesDict = []
    temp_x = x
    temp_y = y
    while temp_x < 8 and temp_y < 8: # check on x,y on board (from x,y to 8)
        temp_x += 1
        temp_y += 1
        if "square-" + str(temp_x) + str(temp_y) in board[color]:
            break
        elif "square-" + str(temp_x) + str(temp_y) in board[enemy_color]:
            addHighlitesDict.append({'x': temp_x, 'y':temp_y})
            break
    temp_x = x
    temp_y = y
    while temp_x < 8 and temp_y > 0: # check on x,y on board (from x to 8, y to 0)
        temp_x += 1
        temp_y -= 1
        if "square-" + str(temp_x) + str(temp_y) in board[color]:
            break
        elif "square-" + str(temp_x) + str(temp_y) in board[enemy_color]:
            addHighlitesDict.append({'x': temp_x, 'y':temp_y})
            break

    temp_x = x
    temp_y = y
    while temp_x > 0 and temp_y > 0: # check on x,y on board (from x, y to 0)
        temp_x -= 1
        temp_y -= 1
        if "square-" + str(temp_x) + str(temp_y) in board[color]:
            break
        elif "square-" + str(temp_x) + str(temp_y) in board[enemy_color]:
            addHighlitesDict.append({'x': temp_x, 'y':temp_y})
            break
    
    temp_x = x
    temp_y = y
    while temp_x > 0 and temp_y < 8: # check on x,y on board (from x to 0, y to 8)
        temp_x -= 1
        temp_y += 1
        if "square-" + str(temp_x) + str(temp_y) in board[color]:
            break
        elif "square-" + str(temp_x) + str(temp_y) in board[enemy_color]:
            addHighlitesDict.append({'x': temp_x, 'y':temp_y})
            break
    return addHighlitesDict
    
def rook(x,y, color, board):
    return check_vertical_and_horizontal(x, y, color, board)

def queen(x,y, color, board):
    addHighlightsDict = []
    addHighlightsDict.extend(check_vertical_and_horizontal(x, y, color, board))
    addHighlightsDict.extend(check_diagonal(x, y, color, board))
    return addHighlightsDict

def bishop(x, y, color, board):
    return check_diagonal(x, y, color, board)

def knight(x, y, color, board):
    enemy_color = get_enemy_color(color)
    addHighlitesDict = []
    step_long = 2
    step_short = 1

    x_temp = x + step_long
    y_temp = y + step_short
    if "square-" + str(x_temp) + str(y_temp) in board[enemy_color]:
        addHighlitesDict.append({'x': x_temp, 'y':y_temp})
    
    x_temp = x + step_long
    y_temp = y - step_short
    if "square-" + str(x_temp) + str(y_temp) in board[enemy_color]:
        addHighlitesDict.append({'x': x_temp, 'y':y_temp})
    
    x_temp = x - step_long
    y_temp = y + step_short
    if "square-" + str(x_temp) + str(y_temp) in board[enemy_color]:
        addHighlitesDict.append({'x': x_temp, 'y':y_temp})

    x_temp = x - step_long
    y_temp = y - step_short
    if "square-" + str(x_temp) + str(y_temp) in board[enemy_color]:
        addHighlitesDict.append({'x': x_temp, 'y':y_temp})
    


    x_temp = x + step_short
    y_temp = y + step_long
    if "square-" + str(x_temp) + str(y_temp) in board[enemy_color]:
        addHighlitesDict.append({'x': x_temp, 'y':y_temp})

    x_temp = x + step_short
    y_temp = y - step_long
    if "square-" + str(x_temp) + str(y_temp) in board[enemy_color]:
        addHighlitesDict.append({'x': x_temp, 'y':y_temp})

    x_temp = x - step_short
    y_temp = y + step_long
    if "square-" + str(x_temp) + str(y_temp) in board[enemy_color]:
        addHighlitesDict.append({'x': x_temp, 'y':y_temp})

    x_temp = x - step_short
    y_temp = y - step_long
    if "square-" + str(x_temp) + str(y_temp) in board[enemy_color]:
        addHighlitesDict.append({'x': x_temp, 'y':y_temp})

    return addHighlitesDict


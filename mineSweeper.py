# MineSweeper

def countMines(field, i, j):
    count = 0 
    dir = [-1, 0, 1]
    for dr in dir:
        for dc in dir:
            if dr == 0 and dc == 0:
                continue
            nr, nc = i + dr, j + dc

            if 0 <= nr < len(field) and 0 <= nc < len(field[0]) and field[nr][nc] == "*":
                count += 1
    return count

def countAllMines(field):
    for i in range(len(field)):
        for j in range(len(field)):
            if field[i][j] == "*":
                continue
            field[i][j] = str(countMines(field, i, j))
    return field
field = [
    list("*..."),
    list("...."),
    list(".*.."),
    list("....")
]
print(countAllMines(field))
            

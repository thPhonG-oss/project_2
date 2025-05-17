
def get_neighbors(i, j, height, width):
    neighbors = []
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == 0 and dj == 0:
                continue
            ni, nj = i + di, j + dj
            if 0 <= ni < height and 0 <= nj < width:
                neighbors.append((ni, nj))
    return neighbors

def get_var_id(i, j, width):
    return i * width + j + 1 

def get_coord(var_id, width):
    var_id -= 1
    return var_id // width, var_id % width


import random

def start_game():
    mat = [[0, 0, 0, 0] for _ in range(4)]
    add_new_2(mat)
    add_new_2(mat)
    
    print("Commands are as follows:")
    print("'W' or 'w': Move Up")
    print("'S' or 's': Move Down")
    print("'A' or 'a': Move Left")
    print("'D' or 'd': Move Right")
    
    return mat

def add_new_2(mat):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if mat[i][j] == 0]
    if not empty_cells:
        return
    
    r, c = random.choice(empty_cells)
    mat[r][c] = 2

def get_current_state(mat):
    for row in mat:
        if 2048 in row:
            return 'WON'
    
    for row in mat:
        if 0 in row:
            return 'GAME NOT OVER'
    
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j + 1]:
                return 'GAME NOT OVER'
            if mat[j][i] == mat[j + 1][i]:
                return 'GAME NOT OVER'
    
    return 'LOST'

def compress(mat):
    new_mat = [[0, 0, 0, 0] for _ in range(4)]
    changed = False
    
    for i in range(4):
        pos = 0
        for j in range(4):
            if mat[i][j] != 0:
                new_mat[i][pos] = mat[i][j]
                if j != pos:
                    changed = True
                pos += 1
    
    return new_mat, changed

def merge(mat):
    changed = False
    
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j + 1] and mat[i][j] != 0:
                mat[i][j] *= 2
                mat[i][j + 1] = 0
                changed = True
    
    return mat, changed

def reverse(mat):
    new_mat = []
    for row in mat:
        new_mat.append(row[::-1])
    return new_mat

def transpose(mat):
    new_mat = [[mat[j][i] for j in range(4)] for i in range(4)]
    return new_mat

def move_left(mat):
    new_mat, changed1 = compress(mat)
    new_mat, changed2 = merge(new_mat)
    new_mat, _ = compress(new_mat)
    changed = changed1 or changed2
    return new_mat, changed

def move_right(mat):
    new_mat = reverse(mat)
    new_mat, changed = move_left(new_mat)
    new_mat = reverse(new_mat)
    return new_mat, changed

def move_up(mat):
    new_mat = transpose(mat)
    new_mat, changed = move_left(new_mat)
    new_mat = transpose(new_mat)
    return new_mat, changed

def move_down(mat):
    new_mat = transpose(mat)
    new_mat = reverse(new_mat)
    new_mat, changed = move_left(new_mat)
    new_mat = reverse(new_mat)
    new_mat = transpose(new_mat)
    return new_mat, changed

def print_grid(mat):
    for row in mat:
        print(row)
    print()

def main():
    mat = start_game()
    while True:
        print_grid(mat)
        x = input("Press the command: ").strip().lower()
        if x == 'w':
            mat, changed = move_up(mat)
        elif x == 's':
            mat, changed = move_down(mat)
        elif x == 'a':
            mat, changed = move_left(mat)
        elif x == 'd':
            mat, changed = move_right(mat)
        else:
            print("Invalid Key Pressed")
            continue
        
        if changed:
            add_new_2(mat)
        
        state = get_current_state(mat)
        if state == 'WON':
            print_grid(mat)
            print("Congratulations! You have won the game!")
            break
        elif state == 'LOST':
            print_grid(mat)
            print("Game Over! You have lost the game.")
            break

if __name__ == "__main__":
    main()
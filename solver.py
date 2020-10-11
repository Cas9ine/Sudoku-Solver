
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def solve(sbo):

    find = find_empty(sbo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(sbo, i, (row, col)):
            sbo[row][col] = i

            if solve(sbo):
                return True

            sbo[row][col] = 0

    return False




def valid(sbo, num, pos):
    #check row
    for i in range(len(sbo[0])):
        if sbo[pos[0]][i] == num and pos[1] != i:
            return False

    #check column
    for i in range(len(sbo)):
        if sbo[i][pos[1]] == num and pos[0] != i:
            return False

    # check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if sbo[i][j] == num and (i,j) != pos:
                return False

    return True

def board_print(sbo):

    for i in range(len(sbo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(sbo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                    print(sbo[i][j])
            else:
                    print(str(sbo[i][j]) + " ", end="")


def find_empty(sbo):
    for i in range(len(sbo)):
        for j in range(len(sbo[0])):
            if sbo[i][j] == 0:
                return (i, j) # row, col

    return None

print("**************************")
print("Here's the unsolved board: :)")
print("**************************")
board_print(board)

solve(board)
print("**************************")
print("   Solution is below! :)")
print("**************************")
board_print(board)
print("**************************")
print("Thanks for using my solver! :)")
print("**************************")

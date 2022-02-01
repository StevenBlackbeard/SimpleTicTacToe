def check_cols(letter):
    output = False
    if vals[0] == vals[1] == vals[2] == letter:
        output = True
    if vals[3] == vals[4] == vals[5] == letter:
        output = True
    if vals[6] == vals[7] == vals[8] == letter:
        output = True
    return output

def check_rows(letter):
    output = False
    if vals[0] == vals[3] == vals[6] == letter:
        output = True
    if vals[1] == vals[4] == vals[7] == letter:
        output = True
    if vals[2] == vals[5] == vals[8] == letter:
        output = True
    return output
    
def check_diag(letter):
    output = False
    if vals[0] == vals[4] == vals[8] == letter:
        output = True
    if vals[2] == vals[4] == vals[6] == letter:
        output = True
    return output

def print_grid(vals):
    output = ("""
---------
| {0} {1} {2} |
| {3} {4} {5} |
| {6} {7} {8} |
---------
""".format(vals[0], vals[1], vals[2], vals[3], vals[4], vals[5],
               vals[6], vals[7], vals[8]))
    return output

vals = "_________"
# vals = input("Enter cells:")
vals = [i if i != "_" else " " for i in vals]
print(print_grid(vals))
coord_avail = [[i + 1, j + 1] for i in range(3) for j in range(3)]
count = 1

while True:
    letter = "X" if count % 2 == 1 else "O"
    # coord = "2 1".split()
    # coord = "4 1".split()
    # coord = "one".split()
    coord = input("Enter the coordinates:").split()
    try:
        coord = [int(x) for x in coord]
    except ValueError:
        print("You should enter numbers!")
        continue

    if coord not in coord_avail:
        print("Coordinates should be from 1 to 3!")
        continue
    else:
        coord_val = vals[coord_avail.index(coord)]

    if coord_val != " ":
        print("This cell is occupied! Choose another one!")
        continue
    else:
        vals[coord_avail.index(coord)] = letter
        print(print_grid([i if i != "_" else " " for i in vals]))

    if check_cols(letter) or check_rows(letter) or check_diag(letter):
        print(f'{letter} wins')
        break
    elif ''.join(vals).find(" ") == -1:
        print('Draw')
        break
    else:
        count += 1
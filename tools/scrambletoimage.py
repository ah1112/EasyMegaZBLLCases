import picturetopython as ptp
import json

# Take last layer face to be the top face, and the light green face as front
# Starts at UFR sticker CW
u_face = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Starts at RUBr sticker CW
f_face = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# Starts at the LUF sticker CW
l_face = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
# Starts at the BlUL sticker CW
bl_face = [30, 31, 32, 33, 34, 35, 36, 37, 38, 39]
# Starts at the BrUR sticker CW
br_face = [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
# Starts at the BrBlU sticker CW
r_face = [50, 51, 52, 53, 54, 55, 56, 57, 58, 59]

# ---------- Lower ring ---------- All starting stickers are the top - most sticker in that face

# Face between F and R (down-front-right)
dfr_face = [60, 61, 62, 63, 64, 65, 66, 67, 68, 69]

# Face between R and BR (down-back-right)
drbr_face = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]

# Face between BR and BL (down-back-left)
dbrbl_face = [90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

# Face between BL and L (down-front-left)
dbll_face = [80, 81, 82, 83, 84, 85, 86, 87, 88, 89]

# Face between L and F (down-left-front belt continuation)
dfl_face = [70, 71, 72, 73, 74, 75, 76, 77, 78, 79]


# ---------- Bottom face ---------- Starting sticker is the white sticker between Dfl and Dfr

# Bottom face (opposite U)
# Starts at sticker CW
d_face = [110, 111, 112, 113, 114, 115, 116, 117, 118, 119]


# ------------------------------ Cycles for each move:

"""
U cycles:
(0 2 4 6 8)
(1 3 5 7 9)
(10 20 30 40 50)
(11 21 31 41 51)
(12 22 32 42 52)

R cycles:
(50 58 56 54 52)
(51 59 57 55 53)
(0 42 100 68 18)
(9 43 101 69 19)
(8 44 102 60 10)

F cycles:
(10 18 16 14 12)
(11 19 17 15 13)
(0 54 62 70 20)
(1 53 61 79 29)
(2 52 60 78 28)

L cycles:
(20 28 26 24 22)
(21 29 27 25 23)
(2 14 72 80 30)
(3 13 71 89 39)
(4 12 70 88 38)

Br cycles:
(40 48 46 44 42)
(41 49 47 45 43)
(6 34 92 100 50)
(7 33 91 109 59)
(8 32 90 108 58)

Dfr cycles:
(60 68 66 64 62)
(61 69 67 65 63)
(16 54 102 118 76)
(17 55 103 119 77)
(18 56 104 110 78)

Dbr cycles:
(100 108 106 104 102)
(101 109 107 105 103)
(44 92 116 66 56)
(45 93 117 67 57)
(46 94 118 68 58)
"""

solved_state = {i : i for i in range(120)}


"""
U cycles:
(0 2 4 6 8)
(1 3 5 7 9)
(10 20 30 40 50)
(11 21 31 41 51)
(12 22 32 42 52)
"""

def move_maker(state, batches):
    new_state = state.copy()
    for i in range(5):
        for j in range(5):
            new_state[batches[i][j]] = state[batches[i][(j + 4) % 5]]
    return new_state

def u_move(state):
    return move_maker(state, [[0, 2, 4, 6, 8], [1, 3, 5, 7, 9], [10, 20, 30, 40, 50], [11, 21, 31, 41, 51], [12, 22, 32, 42, 52]])

def u2_move(state):
    return u_move(u_move(state))

def uprime_move(state):
    return u2_move(u2_move(state))

def u2prime_move(state):
    return u_move(u_move(u_move(state)))

"""
R cycles:
(50 58 56 54 52)
(51 59 57 55 53)
(0 42 100 68 18)
(9 43 101 69 19)
(8 44 102 60 10)
"""
def r_move(state):
    return move_maker(state, [[50, 58, 56, 54, 52], [51, 59, 57, 55, 53], [0, 42, 100, 68, 18], [9, 43, 101, 69, 19], [8, 44, 102, 60, 10]])

def r2_move(state):
    return r_move(r_move(state))

def rprime_move(state):
    return r2_move(r2_move(state))

def r2prime_move(state):
    return r_move(r_move(r_move(state)))

"""
F cycles:
(10 18 16 14 12)
(11 19 17 15 13)
(0 54 62 70 20)
(1 53 61 79 29)
(2 52 60 78 28)
"""

def f_move(state):
    return move_maker(state, [[10, 18, 16, 14, 12], [11, 19, 17, 15, 13], [0, 54, 62, 70, 20], [1, 53, 61, 79, 29], [2, 52, 60, 78, 28]])

def f2_move(state):
    return f_move(f_move(state))

def fprime_move(state):
    return f2_move(f2_move(state))

def f2prime_move(state):
    return f_move(f_move(f_move(state)))

"""
L cycles:
(20 28 26 24 22)
(21 29 27 25 23)
(2 14 72 80 30)
(3 13 71 89 39)
(4 12 70 88 38)
"""

def l_move(state):
    return move_maker(state, [[20, 28, 26, 24, 22], [21, 29, 27, 25, 23], [2, 14, 72, 80, 30], [3, 13, 71, 89, 39], [4, 12, 70, 88, 38]])

def l2_move(state):
    return l_move(l_move(state))

def lprime_move(state):
    return l2_move(l2_move(state))

def l2prime_move(state):
    return l_move(l_move(l_move(state)))

"""
Br cycles:
(40 48 46 44 42)
(41 49 47 45 43)
(6 34 92 100 50)
(7 33 91 109 59)
(8 32 90 108 58)
"""

def br_move(state):
    return move_maker(state, [[40, 48, 46, 44, 42], [41, 49, 47, 45, 43], [6, 34, 92, 100, 50], [7, 33, 91, 109, 59], [8, 32, 90, 108, 58]])

def br2_move(state):
    return br_move(br_move(state))

def brprime_move(state):
    return br2_move(br2_move(state))

def br2prime_move(state):
    return br_move(br_move(br_move(state)))

"""
Dfr cycles:
(60 68 66 64 62)
(61 69 67 65 63)
(16 54 102 118 76)
(17 55 103 119 77)
(18 56 104 110 78)
"""

def dfr_move(state):
    return move_maker(state, [[60, 68, 66, 64, 62], [61, 69, 67, 65, 63], [16, 54, 102, 118, 76], [17, 55, 103, 119, 77], [18, 56, 104, 110, 78]])

def dfr2_move(state):
    return dfr_move(dfr_move(state))

def dfrprime_move(state):
    return dfr2_move(dfr2_move(state))

def dfr2prime_move(state):
    return dfr_move(dfr_move(dfr_move(state)))

"""
Dbr cycles:
(100 108 106 104 102)
(101 109 107 105 103)
(44 92 116 66 56)
(45 93 117 67 57)
(46 94 118 68 58)
"""

def dbr_move(state):
    return move_maker(state, [[100, 108, 106, 104, 102], [101, 109, 107, 105, 103], [44, 92, 116, 66, 56], [45, 93, 117, 67, 57], [46, 94, 118, 68, 58]])

def dbr2_move(state):
    return dbr_move(dbr_move(state))

def dbrprime_move(state):
    return dbr2_move(dbr2_move(state))

def dbr2prime_move(state):
    return dbr_move(dbr_move(dbr_move(state)))

#[[, , , , ], [, , , , ], [, , , , ], [, , , , ], [, , , , ]]

#--------------------------------
# """

# """

# def _move(state):
#     return move_maker(state, [[, , , , ], [, , , , ], [, , , , ], [, , , , ], [, , , , ]])

# def 2_move(state):
#     return _move(_move(state))

# def prime_move(state):
#     return 2_move(2_move(state))

# def 2prime_move(state):
#     return _move(_move(_move(state)))


#[[, , , , ], [, , , , ], [, , , , ], [, , , , ], [, , , , ]]
#----------------------------------------------------

move_to_fn = {
    "U" : u_move,
    "U'" : uprime_move,
    "U2" : u2_move,
    "U2'" : u2prime_move,
    "R" : r_move,
    "R2" : r2_move,
    "R2'" : r2prime_move,
    "R'" : rprime_move,
    "F" : f_move,
    "F2" : f2_move,
    "F'" : fprime_move,
    "F2'" : f2prime_move,
    "L" : l_move,
    "L2" : l2_move,
    "L'" : lprime_move,
    "L2'" : l2prime_move,
    "Br" : br_move,
    "Br2" : br2_move,
    "Br'" : brprime_move,
    "Br2'" : dfr2prime_move,
    "Dfr" : dfr_move,
    "Dfr2" : dfr2_move,
    "Dfr'" : dfrprime_move,
    "Dfr2'" : dfr2prime_move,
    "Dbr" : dbr_move,
    "Dbr2" : dbr2_move,
    "Dbr'" : dbrprime_move,
    "Dbr2'" : dbr2prime_move
}

def alg_on_state(s, alg):
    moves = alg.split(" ")
    for move in moves:
        s = move_to_fn[move](s)
    return s


black = list(range(10))
green = [10, 11, 12]
orange = [20, 21, 22]
blue = [30, 31, 32]
cream = [40, 41, 42]
pink = [50, 51, 52]

sticker_to_color = {
    10 : 'g',
    11 : 'g',
    12 : 'g',
    20 : 'o',
    21 : 'o',
    22 : 'o',
    30 : 'b',
    31 : 'b',
    32 : 'b',
    40 : 'y',
    41 : 'y',
    42 : 'y',
    50 : 'p',
    51 : 'p',
    52 : 'p'
}

for i in range(10):
    sticker_to_color[i] = 'k'

def picture_from_state(state):
    pic = ''
    pic += sticker_to_color[state[10]]
    pic += sticker_to_color[state[11]]
    pic += sticker_to_color[state[12]]
    pic += sticker_to_color[state[20]]
    pic += sticker_to_color[state[21]]
    pic += sticker_to_color[state[22]]
    pic += sticker_to_color[state[30]]
    pic += sticker_to_color[state[31]]
    pic += sticker_to_color[state[32]]
    pic += sticker_to_color[state[40]]
    pic += sticker_to_color[state[41]]
    pic += sticker_to_color[state[42]]
    pic += sticker_to_color[state[50]]
    pic += sticker_to_color[state[51]]
    pic += sticker_to_color[state[52]]
    pic += sticker_to_color[state[0]]
    pic += sticker_to_color[state[1]]
    pic += sticker_to_color[state[2]]
    pic += sticker_to_color[state[3]]
    pic += sticker_to_color[state[4]]
    pic += sticker_to_color[state[5]]
    pic += sticker_to_color[state[6]]
    pic += sticker_to_color[state[7]]
    pic += sticker_to_color[state[8]]
    pic += sticker_to_color[state[9]]
    pic += 'k'

    return pic

def make_json_from_svg(setups):

    states = [alg_on_state(solved_state, setups[i]) for i in range(len(setups))]

    # # For debugging purposes
    # count = 0
    # for key in state:
    #     if state[key] != key:
    #         count += 1
    #         print(key, state[key])

    # print(count)

    def pauf_for_green(i, state):
        dic = {
            'g' : "",
            'o' : "U ",
            'b' : "U2 ",
            'y' : "U2' ",
            'p' : "U' "
        }
        pic_string = picture_from_state(state)
        pauf = dic[pic_string[1]]
        new_state = alg_on_state(solved_state, pauf + setups[i])
        return picture_from_state(new_state)

    pic_strings = [pauf_for_green(i, states[i]) for i in range(len(states))]
    # Brackets in here because we could give a list of states
    svg_dict = ptp.make_svg(pic_strings, 1)

    with open("ZBLL-Trainer/combined.json", "w") as f:
        json.dump(svg_dict, f, indent=4)

    print("combined.json written successfully.")

    return svg_dict

# # To view the picture locally:
# from pathlib import Path

# # Create folder "images" if it doesn't exist
# output_dir = Path("images")
# output_dir.mkdir(exist_ok=True)

# # Write each SVG to its own file
# for key, svg in svg_dict.items():
#     output_file = output_dir / f"{key}.svg"
#     output_file.write_text(svg) 

# print("All SVGs written to images/")
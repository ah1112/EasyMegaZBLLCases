def invert_algorithm(alg: str) -> str:
    moves = alg.split()
    inverted = []

    for move in reversed(moves):
        if move.endswith("'"):
            inverted.append(move[:-1])  # remove prime
        else:
            inverted.append(move + "'")  # add prime

    return " ".join(inverted)


# # Example usage
# alg =  [
#             "R U2 R U2' R2' U' R2 U2' R' U2 R'"
#         ]
# inv = []
# for al in alg:
#     inv.append(invert_algorithm(al))

# print(inv)

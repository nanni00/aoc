with open('2024/input/6.txt') as fr:
    board = [line.strip() for line in fr.readlines()]

sr, sc = [(r, c) for r in range(len(board)) for c in range(len(board[0])) if board[r][c] in '^v><'][0]

moves = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def move(r, c):
    positions = {(r, c)}
    while True:
        mr, mc = moves.pop(0)
        if not (0 <= r + mr < len(board) and 0 <= c + mc < len(board[0])):
            break

        if board[r + mr][c + mc] != '#':
            r, c = r + mr, c + mc
            positions.add((r, c))
            moves.insert(0, [mr, mc])
        else:
            moves.insert(len(moves), [mr, mc])
    return positions


moves = [
    [-1, 0], # ^ up 
    [0, 1],  # > right
    [1, 0],  # v down
    [0, -1]  # < left
]
last_move = [-1, 0]

part_1 = len(move(sr, sc))
print(f'{part_1=}')


# TODO finish geom solution of part 2

"""
Best solution for part 2 (not mine)
Complex numbers to store both directions and positions in the same place
Very elegant, remeber to use such stuff in other exercises

G = {i+j*1j: c for i,r in enumerate(open('2024/input/6.txt'))
               for j,c in enumerate(r.strip())}

start = min(p for p in G if G[p] == '^')

def walk(G):
    pos, dir, seen = start, -1, set()
    while pos in G and (pos,dir) not in seen:
        seen |= {(pos,dir)}
        if G.get(pos+dir) == "#":
            dir *= -1j
        else: pos += dir
    return {p for p,_ in seen}, (pos,dir) in seen

path = walk(G)[0]
print(len(path),
      sum(walk(G | {o: '#'})[1] for o in path if o != start))
"""


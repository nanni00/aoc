with open('2024/input/4.txt') as fr:
    s = [line.strip() for line in fr.readlines()]


def find_XMAS(r, c, s):
    cnt = 0
    
    #right
    cnt += s[r][c:c+4] == 'XMAS'
    
    # left
    cnt += s[r][c-3:c+1] == 'SAMX'

    if r >= 3:
        # up
        cnt += ''.join(s[r - x][c] for x in range(0, 4)) == 'XMAS'
        
        # left up
        cnt += c >= 3 and ''.join(s[r - x][c - x] for x in range(0, 4)) == 'XMAS'
        
        # right up
        cnt += c < len(s[0]) - 3 and ''.join(s[r - x][c + x] for x in range(0, 4)) == 'XMAS'
    
    if r < len(s) - 3:
        # down
        cnt += ''.join(s[r + x][c] for x in range(0, 4)) == 'XMAS'
        
        # left down
        cnt += c >= 3 and ''.join(s[r + x][c - x] for x in range(0, 4)) == 'XMAS'

        # right down
        cnt += c < len(s[0]) - 3 and ''.join(s[r + x][c + x] for x in range(0, 4)) == 'XMAS'
    return cnt


def find_X_MAS(r, c, s):
    cnt = 0
    if 1 <= r < len(s) - 1 and 1 <= c < len(s[0]) - 1:
        if ''.join(sorted([s[r-1][c-1], s[r][c], s[r+1][c+1]])) == ''.join(sorted([s[r-1][c+1], s[r][c], s[r+1][c-1]])) == 'AMS':
            cnt += 1
    return cnt


part_1 = 0
part_2 = 0

for r in range(len(s)):
    for c in range(len(s[0])):
        if s[r][c] == 'X':
            part_1 += find_XMAS(r, c, s)
        if s[r][c] == 'A':
            part_2 += find_X_MAS(r, c, s)

print(f"{part_1=}")
print(f"{part_2=}")

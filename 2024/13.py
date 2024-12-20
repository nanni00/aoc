import re
from math import floor, gcd
from sympy import solve, symbols, Eq


mp =[x for x in map(int, re.findall(r'\d+', open('2024/input/13.txt').read()))]
mp = [[mp[i:i+6:2], mp[i+1:i+6:2]] for i in range(0, len(mp), 6)]

def calc(part):
    res = 0
    for (xa, xb, xp), (ya, yb, yp) in mp:
        m = 0 if part == 1 else 10000000000000
        if (m + xp) % gcd(xa, xb) == 0 and (m + yp) % gcd(ya, yb) == 0:
            x1, x2 = symbols('x1 x2')

            eqx = Eq(xa * x1 + xb * x2, m + xp)
            eqy = Eq(ya * x1 + yb * x2, m + yp)
            sol = solve((eqx, eqy), (x1, x2))
            x1, x2 = sol[x1], sol[x2]

            if ((part == 1 and 0 <= x1 <= 100 and 0 <= x2 <= 100) or part == 2) and x1 == floor(x1) and x2 == floor(x2):
                res += 3 * x1 + x2
    return res

print(f'part_1={calc(1)}')
print(f'part_2={calc(2)}')

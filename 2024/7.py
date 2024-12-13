import re
import operator


tests = [[int(x) for x in re.findall(r'\d+', line.strip())] for line in open('2024/input/7.txt').readlines()]

# TODO add dynamic prog stuff to improve part 2
def check(v, c, n, operators):
    if v == c and n == []:
        return True
    if n == [] or c > v:
        return False
    for op in operators:
        if check(v, op(c, n[0]), n[1:], operators):
            return True
    return False


part_1 = sum([test[0] for test in tests if check(test[0], test[1], test[2:], [operator.add, operator.mul])])
part_2 = sum([test[0] for test in tests if check(test[0], test[1], test[2:], [operator.add, operator.mul, lambda x, y: int(f'{x}{y}')])])

print(f'{part_1=}')
print(f'{part_2=}')

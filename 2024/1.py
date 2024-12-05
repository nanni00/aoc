from collections import Counter


with open('2024/input/1.txt') as fr:
    f = fr.readlines()

part_1 = sum([abs(int(x) - int(y)) for x, y in zip(*list(map(sorted, list(zip(*[line.split() for line in f])))))])

left, right = list(map(Counter, zip(*[map(int, line.split()) for line in f])))
part_2  = sum([k * v * (right[k] if k in right else 0) for k, v in left.items()])


print(f"{part_1=}")
print(f"{part_2=}")


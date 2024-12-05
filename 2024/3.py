import re
import operator


with open('2024/input/3.txt') as fr:
    f = fr.read().replace('\n', ' ')

part_1 = sum([operator.mul(*[int(n) for n in re.findall(r'\d+', m)]) for m in re.findall(r'mul\(\d+,\d+\)', f)])

part_2 = sum(
    [
        operator.mul(*[int(n) for n in re.findall(r'\d+', m)])
        for mout in re.finditer(r'(do\(\)|^)(.*?)(don\'t\(\)|$)', f)
        for m in re.findall(r'mul\(\d+,\d+\)', mout.group())
    ]
)

print(f"{part_1=}")
print(f"{part_2=}")


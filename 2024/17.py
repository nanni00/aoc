import re


def run(A, B, C, program):
    def combo(operand):
        match operand:
            case 0|1|2|3: return operand
            case 4: return A
            case 5: return B
            case 6: return C

    output = []
    ip = 0
    while ip < len(program):
        opcode, operand = program[ip:ip + 2]
        match opcode:
            case 0: A >>= combo(operand)
            case 1: B ^= operand                      
            case 2: B = combo(operand) & 7
            case 3: ip = ip if A == 0 else operand - 2
            case 4: B ^= C      
            case 5: output.append(combo(operand) & 7)
            case 6: B = A >> combo(operand)
            case 7: C = A >> combo(operand)
        ip += 2
    return output


def part_2(program):
    A = {0}
    for r in program[::-1]:
        cand = []
        for a in A:
            cand += list(filter(lambda x: x[1] == r, ((v, run(v, 0, 0, program[:-2])[0]) for v in range(a * 8, (a + 1) * 8))))
        A = {x[0] for x in cand}    

    for a in sorted(A):
        if run(a, 0, 0, program) == program:
            return a


with open('2024/input/17.txt') as fr:
    n = [int(x) for x in re.findall(r'\d+', fr.read())]
    A, B, C, program = *n[0:3],  n[3:]

print(f'part 1 = {",".join(map(str, run(A, B, C, program)))}')
print(f'part 2 = {part_2(program)}')

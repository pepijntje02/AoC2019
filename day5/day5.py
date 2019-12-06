def readPuzzle(fname):
    f = open(fname, 'r')
    puzzle =  f.read().rstrip().split(',')
    return list(map(int, puzzle))

def intcodeComputer(puzzle, ID, part):
    pointer = 0
    output = 0
    while True:
        instruction = list(map(int, str(puzzle[pointer])))
        opcode = int(''.join(map(str, instruction[-2:])))
        mode = [0]*3
        if len(instruction) > 2:
            for i in range(len(instruction[:-2])):
                mode[i] = instruction[:-2][::-1][i]

        if opcode in {1, 2}:
            n1 = puzzle[puzzle[pointer + 1]] if mode[0] == 0 else puzzle[pointer+1]
            n2 = puzzle[puzzle[pointer + 2]] if mode[1] == 0 else puzzle[pointer+2]
            if mode[2] == 0:
                if opcode == 1: puzzle[puzzle[pointer+3]] = n1+n2
                if opcode == 2: puzzle[puzzle[pointer+3]] = n1*n2
            else:
                print('write parameter is not zero')
                break
            pointer += 4
        if opcode == 3:
            puzzle[puzzle[pointer+1]] = ID
            pointer += 2
        if opcode == 4:
            output = puzzle[puzzle[pointer+1]] if mode[0] == 0 else puzzle[pointer+1]
            pointer += 2
        if opcode == 99:
            return output
        if part == 2: # second part of the puzzle
            if opcode in {5, 6, 7, 8}:
                p1 = puzzle[puzzle[pointer + 1]] if mode[0] == 0 else puzzle[pointer+1]
                p2 = puzzle[puzzle[pointer + 2]] if mode[1] == 0 else puzzle[pointer+2]
                if opcode == 5:
                    if p1:
                        pointer = p2
                    else:
                        pointer += 3
                if opcode == 6:
                    if p1 == 0:
                        pointer = p2
                    else:
                        pointer += 3
                if opcode == 7:
                    puzzle[puzzle[pointer+3]] = 1 if p1 < p2 else 0
                    pointer += 4
                if opcode == 8:
                    puzzle[puzzle[pointer+3]] = 1 if p1 == p2 else 0
                    pointer += 4

if __name__ == '__main__':
    print(80*'-')
    print('Advent of code day 5')
    print(80*'-')
    fname = 'input.txt'
    puzzle = readPuzzle(fname)
    print(intcodeComputer(puzzle[:], ID=1, part=1))
    print(intcodeComputer(puzzle[:], ID=5, part=2))

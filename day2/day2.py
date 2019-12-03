def readPuzzle(fname):
    f = open(fname, 'r')
    puzzle =  f.read().rstrip().split(',')
    return list(map(int, puzzle))

def intcodeComputer(puzzle):
    i = 0
    while i < len(puzzle):
        if puzzle[i] == 1:
            puzzle[puzzle[i+3]] = puzzle[puzzle[i+1]] + puzzle[puzzle[i+2]]
            i += 4
        elif puzzle[i] == 2:
            puzzle[puzzle[i+3]] = puzzle[puzzle[i+1]] * puzzle[puzzle[i+2]]
            i += 4
        elif puzzle[i] == 99:
            break
        else:
            i += 1
    return puzzle

def part1(fname):
    puzzle = readPuzzle(fname)
    programAlarm(puzzle)
    intcodeComputer(puzzle)
    return puzzle

def programAlarm(puzzle):
    puzzle[1] = 12
    puzzle[2] = 2

def part2(fname):
    puzzle = readPuzzle(fname)
    noun = [i for i in range(0,99)]
    verb = [j for j in range(0,99)]
    for i in noun:
        for j in verb:
            p = puzzle.copy()
            p[1] = i
            p[2] = j
            intcodeComputer(p)
            if p[0] == 19690720:
                break
        if p[0] == 19690720:
            break
    return 100*i + j




if __name__ == '__main__':
    print(80*'-')
    print('Advent of code day 2')
    print(80*'-')
    fname = 'input.txt'
    print(part1(fname))
    print(part2(fname))

def readPuzzle(fname):
    with open(fname, 'r') as f:
        puzzle = [line.rstrip().split(')') for line in f.readlines()]
    return puzzle

def pathFinding(path, puzzle, start, value):
    path[start] = value
    nex = [puzzle[1][i] for i,x in enumerate(puzzle[0]) if x == start]
    if nex:
        for n in nex:
            pathFinding(path, puzzle, n, value+1)

def part1(puzzle):
    puzzle = list(map(list, zip(*puzzle)))
    path = dict()
    pathFinding(path, puzzle, 'COM', 0)
    print('Total number of direct and indirect orbits: ', sum(path.values()))

def part2(puzzle):
    puzzle = list(map(list, zip(*puzzle)))
    pathYou = findPath("YOU", puzzle)
    pathSanta = findPath("SAN", puzzle)
    orbitTransfer = len(set(pathYou) - set(pathSanta)) + len(set(pathSanta) - set(pathYou)) - 2
    print('Minimum number of orbital transfers required: ', orbitTransfer)

def findPath(name, puzzle):
    p = [name]
    while not p[-1] == 'COM':
        p.append(puzzle[0][puzzle[1].index(p[-1])])
    return p

if __name__ == '__main__':
    fname = 'input.txt'
    puzzle = readPuzzle(fname)
    part1(puzzle[:])
    part2(puzzle[:])

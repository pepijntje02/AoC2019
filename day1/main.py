import math
def fuel(mass):
    return math.floor(mass/3)-2

def readPuzzle(fname):
    with open(fname, 'r') as f:
        contents = [int(line) for line in f]
    return contents

def sumFuel(masses):
    total = 0
    for mass in masses:
        total += fuel(mass)
    return total

def sumFuel2(masses):
    total = 0
    for mass in masses:
        total += fuelPart2(mass)
    return total

def fuelPart2(mass):
    fuelmass = fuel(mass)
    if fuelmass < 0:
        return 0
    else:
        return fuelmass + fuelPart2(fuelmass)


def test():
    test = [12, 14, 1969, 100756]
    ans = [2, 2, 654, 33583]
    for i in range(len(test)):
        print(fuel(test[i]))
        print(fuel(test[i]) == ans[i])

if __name__ == '__main__':
    fname = 'input.txt'
    masses = readPuzzle(fname)
    totalFuel = sumFuel(masses)
    print('Part 1 total fuel: ', totalFuel)
    totalFuelPart2 = sumFuel2(masses)
    print('Part 2 total fuel: ', totalFuelPart2)

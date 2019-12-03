def readPuzzle(fname):
    line = []
    with open(fname, 'r') as f:
        data = [line.rstrip() for line in f]
    for i in range(len(data)):
        data[i] = data[i].split(',') #split the data
    return data

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def print(self):
        print('(X, Y) cooridnate is: (', self.x, ',', self.y,')')
    def manhattanDist(self):
        return abs(self.x) + abs(self.y)

class line():
    def __init__(self, p1, p2, length):
        self.p1 = p1
        self.p2 = p2
        self.length = length
        self.checkOrientation()
    def checkOrientation(self):
        if self.p1.x == self.p2.x:
            self.orientation = 'vertical'
        elif self.p1.y == self.p2.y:
            self.orientation = 'horizontal'
        else:
            print('Orientation not vertical of horizontal!!')
    def check_intersect(self, line):
        if ((self.p1.x <= line.p1.x and self.p1.x >= line.p2.x) or \
            (self.p1.x <= line.p2.x and self.p1.x >= line.p1.x)) and \
            ((line.p1.y <= self.p1.y and line.p1.y >= self.p2.y) or \
            (line.p1.y <= self.p2.y and line.p1.y >= self.p1.y)):
                return Point(self.p1.x, line.p1.y)
    def intersect(self, line):
        if self.orientation == 'vertical':
            int_point = self.check_intersect(line)
        else:
            int_point = line.check_intersect(self)
        return int_point

def move(move, p1):
    p2 = Point(p1.x, p1.y)
    if move[0] == 'R':
        p2.x += int(move[1:])
    elif move[0] == 'L':
        p2.x -= int(move[1:])
    elif move[0] == 'U':
        p2.y += int(move[1:])
    elif move[0] == 'D':
        p2.y -= int(move[1:])
    else:
        print('Not known which direction!')
    return p2

def intersect_distance(point, line1, line2):
    l = line1.length + line2.length
    for line in [line1, line2]:
        if line.orientation == 'horizontal':
            l -= abs(line.p2.x - point.x)
        if line.orientation == 'vertical':
            l -= abs(line.p2.y - point.y)
    return l

def searchIntersect(lines):
    intersectDists = []
    d = {}
    for i in range(len(lines[0])):
        for j in range(len(lines[1])):
            intersectPoint = lines[0][i].intersect(lines[1][j])
            if intersectPoint is not None:
                intersectDists.append(intersectPoint.manhattanDist())
                dist = intersect_distance(intersectPoint, lines[0][i], lines[1][j])
                if d.get((intersectPoint.x, intersectPoint.y)) is None or \
                        d[(intersectPoint.x, intersectPoint.y)] > dist:
                        d[(intersectPoint.x, intersectPoint.y)] = dist
    return intersectDists, d

def getLines(data):
    lines = []
    for i in range(len(data)):
        lines.append([])
        p1 = Point(0,0)
        length = 0
        for j in range(len(data[i])):
            length += int(data[i][j][1:])
            p2 = move(data[i][j], p1)
            lines[i].append(line(p1, p2, length))
            p1 = Point(p2.x, p2.y)
    return lines

def part1(data):
    lines = getLines(data)
    [intersectDists,d] = searchIntersect(lines)
    intersectDists.sort()
    print(intersectDists[1])

def part2(data):
    lines = getLines(data)
    [intersectDists,d] = searchIntersect(lines)
    print(sorted(d.values())[1])

if __name__ == '__main__':
    fname = 'input.txt'
    data = readPuzzle(fname)
    part1(data)
    part2(data)

import math
with open('inputs/input08.txt') as inputfile:
    inp = inputfile.read()

def parse_input():
    g = []
    for l in inp.split('\n'):
        t = []
        for c in l:
            t.append(c)
        g.append(t)
    return g

g = parse_input()
def sol1():
    d = {}
    n = len(g)
    m = len(g[0])
    for i in range(n):
        for j in range(m):
            if g[i][j] != '.':
                l = d.get(g[i][j], [])
                sorted(l, key=lambda tup: tup[1])
                l.append((i, j))
                d[g[i][j]] = l
                
    for k in d:
        antennas = d[k]
        new_r1, new_c1, new_r2, new_c2 = -1, -1, -1, -1
        
        for i in range(len(antennas)):
            for j in range(i + 1, len(antennas)):
                r1, c1 = antennas[i]
                r2, c2 = antennas[j]
                x, y = abs(r1 - r2), abs(c1 - c2)
                
                if r1 > r2 and c1 < c2:
                    new_r1 = r1 + x
                    new_c1 = c1 - y
                    new_r2 = r2 - x
                    new_c2 = c2 + y
                elif r1 < r2 and c1 < c2:
                    new_r1 = r1 - x
                    new_c1 = c1 - y
                    new_r2 = r2 + x
                    new_c2 = c2 + y
                elif r1 < r2 and c1 > c2:
                    new_r1 = r1 - x
                    new_c1 = c1 + y
                    new_r2 = r2 + x
                    new_c2 = c2 - y
                elif r1 > r2 and c1 > c2:
                    new_r1 = r1 + x
                    new_c1 = c1 + y
                    new_r2 = r2 - x
                    new_c2 = c2 - y
                elif r1 == r2:
                    new_r1 = r1
                    new_r2 = r2
                    if c1 < c2:
                        new_c1 = c1 - y
                        new_c2 = c2 + y
                    else:
                        new_c2 = c2 - y
                        new_c1 = c1 + y
                elif c1 == c2:
                    new_c1 = c1
                    new_c2 = c2
                    if r1 < r2:
                        new_r1 = r1 - x
                        new_r2 = r2 + x
                    else:
                        new_r2 = r2 - x
                        new_r1 = r1 + x

                if new_r1 >=0 and new_r1 < n and new_c1 >= 0 and new_c1 < m:
                    g[new_r1][new_c1] = '#' #if g[new_r1][new_c1] == '.'  else g[new_r1][new_c1]
                if new_r2 >= 0 and new_r2 < n and new_c2 >= 0 and new_c2 < m:
                    g[new_r2][new_c2] = '#' #if g[new_r2][new_c2] == '.'  else g[new_r2][new_c2]
    
    count = 0
    for i in range(n):
        for j in range(m):
            if g[i][j] == '#':
                count += 1
    return count

def sol2():
    d = {}
    n = len(g)
    m = len(g[0])
    for i in range(n):
        for j in range(m):
            if g[i][j] != '.':
                l = d.get(g[i][j], [])
                sorted(l, key=lambda tup: tup[1])
                l.append((i, j))
                d[g[i][j]] = l
                
    for k in d:
        antennas = d[k]
        new_r1, new_c1, new_r2, new_c2 = -1, -1, -1, -1
        
        for i in range(len(antennas)):
            for j in range(i + 1, len(antennas)):
                r1, c1 = antennas[i]
                r2, c2 = antennas[j]
                x, y = abs(r1 - r2), abs(c1 - c2)
                while True:
                    if (r1 < 0 or r1 >= n or c1 < 0 or c1 >= m) and\
                        (r2 < 0 or r2 >= n or c2 < 0 or c2 >= m):
                            break
                    if r1 > r2 and c1 < c2:
                        new_r1 = r1 + x
                        new_c1 = c1 - y
                        new_r2 = r2 - x
                        new_c2 = c2 + y
                    elif r1 < r2 and c1 < c2:
                        new_r1 = r1 - x
                        new_c1 = c1 - y
                        new_r2 = r2 + x
                        new_c2 = c2 + y
                    elif r1 < r2 and c1 > c2:
                        new_r1 = r1 - x
                        new_c1 = c1 + y
                        new_r2 = r2 + x
                        new_c2 = c2 - y
                    elif r1 > r2 and c1 > c2:
                        new_r1 = r1 + x
                        new_c1 = c1 + y
                        new_r2 = r2 - x
                        new_c2 = c2 - y
                    elif r1 == r2:
                        new_r1 = r1
                        new_r2 = r2
                        if c1 < c2:
                            new_c1 = c1 - y
                            new_c2 = c2 + y
                        else:
                            new_c2 = c2 - y
                            new_c1 = c1 + y
                    elif c1 == c2:
                        new_c1 = c1
                        new_c2 = c2
                        if r1 < r2:
                            new_r1 = r1 - x
                            new_r2 = r2 + x
                        else:
                            new_r2 = r2 - x
                            new_r1 = r1 + x

                    if new_r1 >=0 and new_r1 < n and new_c1 >= 0 and new_c1 < m:
                        g[new_r1][new_c1] = '#'
                    if new_r2 >= 0 and new_r2 < n and new_c2 >= 0 and new_c2 < m:
                        g[new_r2][new_c2] = '#'
                    
                    r1, c1 = new_r1, new_c1
                    r2, c2 = new_r2, new_c2
                    
    
    count = 0
    for i in range(n):
        for j in range(m):
            for v in g[i][j]:
                if v != '.':
                    count += 1
    return count

def printg():
    for i in range(len(g)):
        print(g[i])
        
g = parse_input()
printg()
print(sol1())

g = parse_input()
printg()
print(sol2())

# printg()
# print()

with open('inputs/input06.txt') as inputfile:
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

def get_pos():
    for i in range(len(g)):
        for j in range(len(g[0])):
            if g[i][j] == '^':
                return i, j
def sol1():
    up, down, left, right = True, False, False, False
    i, j = get_pos()
    n = len(g)
    m = len(g[0])
    while(True):
        if up:
            if (i - 1) >= 0 and g[i-1][j] == '#':
                right = True
                up = False
            else:
                i -= 1
        elif right:
            if (j + 1) < m  and  g[i][j + 1] == '#':
                right = False
                down = True
            else:
                j += 1
        elif down:
            if (i + 1) < n and g[i + 1][j] == '#':
                left = True
                down = False
            else:
                i += 1
        elif left:
            if (j - 1) >=0 and g[i][j - 1] == '#':
                up = True
                left = False
            else:
                j -= 1
        if i < 0 or j < 0 or i >= n or j >= m or g[i][j] == '#':
            break
        else:
            g[i][j] = 'X'
    
  
    ans = 0
    for i in range(len(g)):
        for j in range(len(g[0])):
            if g[i][j] == 'X':
                ans += 1
    return ans

def init_visited(n ,m):
    visited = []
    for i in range(n):
        l = []
        for j in range(m):
            l.append(0)
        visited.append(l)
    return visited

def sol2():
    up, down, left, right = True, False, False, False
    ans = 0
    n = len(g)
    m = len(g[0])
    for r in range(n):
        for c in range(m):
            temp = g[r][c]
            if temp == '^':
                continue
            g[r][c] = '#'
            i, j = get_pos()
            
            visited = set()
            up, down, left, right = True, False, False, False
            while(True):
                key = str(i) + "_" + str(j)
                if up:
                    key = key + "_up"
                elif down:
                    key = key + "down"
                elif left:
                    key = key + "left"
                elif right:
                    key = key + "right"
                print(ans)
                if visited.__contains__(key):
                    ans += 1
                    break
                visited.add(key)
                if up:
                    if (i - 1) >= 0 and g[i-1][j] == '#':
                        right = True
                        up = False
                    else:
                        i -= 1
                elif right:
                    if (j + 1) < m  and  g[i][j + 1] == '#':
                        right = False
                        down = True
                    else:
                        j += 1
                elif down:
                    if (i + 1) < n and g[i + 1][j] == '#':
                        left = True
                        down = False
                    else:
                        i += 1
                elif left:
                    if (j - 1) >=0 and g[i][j - 1] == '#':
                        up = True
                        left = False
                    else:
                        j -= 1
                if i < 0 or j < 0 or i >= n or j >= m or g[i][j] == '#':
                    break
            g[r][c] = temp

    return ans

g = parse_input() 
print(sol1())    

g = parse_input()
print(sol2())    
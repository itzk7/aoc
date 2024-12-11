def parse_input():
    with open('inputs/input10.txt') as inputfile:
        inp = inputfile.read()
    g = []
    for l in inp.split('\n'):
        t = []
        for c in l:
            t.append(int(c))
        g.append(t)
    return g

def init_visited():
    visited = []
    for i in range(n):
        l = []
        for j in range(m):
            l.append(False)
        visited.append(l)
    return visited

def dfs(r, c, next, visited):
    if r < 0 or r >= n or c < 0 or c >= m:
        return 0
    if visited[r][c]:
        return 0
    
    visited[r][c] = True
    if g[r][c] == 9:
        return 1
    
    ans = 0
    if r - 1 >= 0 and g[r - 1][c] == next:
        ans += dfs(r - 1, c, next + 1, visited)
    if r + 1 < n and g[r + 1][c] == next:
        ans += dfs(r + 1, c, next + 1, visited)
    if c - 1 >= 0 and g[r][c - 1] == next:
        ans += dfs(r, c - 1, next + 1, visited)
    if c + 1 < m and g[r][c + 1] == next:
        ans += dfs(r, c + 1, next + 1, visited)
    return ans

def sol1():
    trials = []
    for i in range(n):
        for j in range(m):
            if g[i][j] == 0:
                trials.append((i, j))

    ans = 0
    for t in trials:
        visited = init_visited()
        ans += dfs(t[0], t[1],1, visited)
    
    return ans

def dfs2(r, c, next):
    if r < 0 or r >= n or c < 0 or c >= m:
        return 0
    
    if g[r][c] == 9:
        return 1
    
    ans = 0
    if r - 1 >= 0 and g[r - 1][c] == next:
        ans += dfs2(r - 1, c, next + 1)
    if r + 1 < n and g[r + 1][c] == next:
        ans += dfs2(r + 1, c, next + 1)
    if c - 1 >= 0 and g[r][c - 1] == next:
        ans += dfs2(r, c - 1, next + 1)
    if c + 1 < m and g[r][c + 1] == next:
        ans += dfs2(r, c + 1, next + 1)
    return ans
def sol2():
    trials = []
    for i in range(n):
        for j in range(m):
            if g[i][j] == 0:
                trials.append((i, j))

    ans = 0
    for t in trials:
        ans += dfs2(t[0], t[1],1)
    
    return ans

import time
s = time.time()
g = parse_input()
n = len(g)
m = len(g[0])
print(sol1())
print(sol2())
print('total ', time.time() - s)

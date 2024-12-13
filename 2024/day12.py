with open('inputs/input12.txt') as inputfile:
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
def dfs(visited, i, j, fence,curr, count):
    n = len(visited)
    m = len(visited[0])
    
    if i < 0 or j < 0 or i >= n or j >= m:
        return
    if visited[i][j] or g[i][j] != curr:
        return
    visited[i][j] = True
    
    area, perimeter = (1, 4)
    if i - 1 >= 0 and g[i-1][j] == curr:
        perimeter-=1
    if i + 1 < n and g[i+1][j] == curr:
        perimeter-=1
    if j + 1 < m and g[i][j+1] == curr:
        perimeter-=1
    if j - 1 >= 0 and g[i][j-1] == curr:
        perimeter-=1
    key = str(curr) + "_" + str(count)
    old_area, old_perimeter = fence.get(key, (0, 0))
    fence[key] = (area + old_area, perimeter + old_perimeter)
    
    dfs(visited, i - 1, j, fence, curr, count)
    dfs(visited, i + 1, j, fence, curr, count)
    dfs(visited, i, j - 1, fence, curr, count)
    dfs(visited, i, j + 1, fence, curr, count)
    
    
    
def sol1():
    n = len(g)
    m = len(g[0])
    
    visited = []
    fence = {}
    for i in range(n):
        l = []
        t = []
        for j in range(m):
            l.append(False)
            t.append(0)
        visited.append(l)

    count = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                dfs(visited, i, j, fence, g[i][j], count)
                count += 1

    ans = 0
    for l in fence:
        a, p = fence[l][0], fence[l][1]
        ans += a * p
    return ans          

print(sol1())


def dfs2(visited, i, j, fence,curr, count):
    n = len(visited)
    m = len(visited[0])
    
    if i < 0 or j < 0 or i >= n or j >= m:
        return
    if visited[i][j] or g[i][j] != curr:
        return
    visited[i][j] = True
    
    area, perimeter = (1, 4)
    if i - 1 >= 0 and g[i-1][j] == curr:
        perimeter-=1
    if i + 1 < n and g[i+1][j] == curr:
        perimeter-=1
    if j + 1 < m and g[i][j+1] == curr:
        perimeter-=1
    if j - 1 >= 0 and g[i][j-1] == curr:
        perimeter-=1
    key = str(curr) + "_" + str(count)
    
    old_area, old_points = fence.get(key, (0, []))
    old_points.append([i, j])
    fence[key] = (area + old_area, old_points)
    
    
    prev_i, prev_j = i, j
    dfs2(visited, i - 1, j, fence, curr, count)
    dfs2(visited, i + 1, j, fence, curr, count)
    dfs2(visited, i, j - 1, fence, curr, count)
    dfs2(visited, i, j + 1, fence, curr, count)
    
def calc_sides(points, n, m):
    traversal = []
    for i in range(n):
        t = []
        for j in range(m):
            t.append('')
        traversal.append(t)
        
    for p in points:
        traversal[p[0]][p[1]] = '*'
    
    ans = 0
    t = {}
    for i in range(n):
        for j in range(m):
            if traversal[i][j] == '*':
                k = j
                while(k < m and traversal[i][k] == '*'):
                    k+=1
                t[j] = 1
                t[k] = 1
                if j == k:
                    t[k] = 2
                j = k - 1
    ans = 0
    for i in t:
        ans += t[i]
    t = {}
    for j in range(m):
        for i in range(n):
            if traversal[i][j] == '*':
                k = i
                while(k < n and traversal[k][j] == '*'):
                    k+=1
                t[i] = 1
                t[k] = 1
                i = k - 1
    for i in t:
        ans += t[i]
    return ans
        
    
    
def sol2():
    n = len(g)
    m = len(g[0])
    
    visited = []
    fence = {}
    for i in range(n):
        l = []
        t = []
        for j in range(m):
            l.append(False)
            t.append(0)
        visited.append(l)

    count = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                dfs2(visited, i, j, fence, g[i][j], count)
                count += 1

    ans = 0
    for l in fence:
        a, points = fence[l][0], fence[l][1]
        sides = calc_sides(points, n, m)
        ans += a * sides
    return ans          

print(sol2())
with open('inputs/input04.txt') as inputfile:
    inp = inputfile.read()


def parse_input():
    g = []
    for l in inp.split('\n'):
        t = []
        for c in l:
            t.append(c)
        if t:
            g.append(t)
    return g

g = parse_input()


def sol1(g):
    indices = []
    count = 0
    for i in range(len(g)):
        for j in range(len(g[0])):
            if g[i][j] == 'X':
                indices.append((i, j))
    for index in indices:
        count += dfs(g, index)
    return count

def sol2(g):
    indices = []
    count = 0
    for i in range(len(g)):
        for j in range(len(g[0])):
            if g[i][j] == 'A':
                indices.append((i, j))
    for index in indices:
        count += dfs2(g, index)
    return count

def dfs2(g, index):    
    r = index[0]
    c = index[1]
    
    n = len(g)
    m = len(g[0])
    down_left = r + 1, c - 1
    down_right = r + 1, c + 1
    up_left = r - 1, c - 1
    up_right = r - 1, c + 1
    
    if is_valid(down_left, n, m) and is_valid(down_right, n, m) and is_valid(up_left, n, m) and is_valid(up_right, n, m):
        # print(g[down_left[0]][down_left[1]], g[down_right[0]][down_right[1]], g[up_left[0]][up_left[1]], g[up_right[0]][up_right[1]])
        a= g[down_left[0]][down_left[1]], g[up_right[0]][up_right[1]]
        b = g[up_left[0]][up_left[1]], g[down_right[0]][down_right[1]]
        if "".join(sorted(a)) == "MS" and "".join(sorted(b)) == "MS":
            return 1
    return 0

def is_valid(index, n, m):
    return index[0] >= 0 and index[0] < n and index[1] >= 0 and index[1] < m
def dfs(g, index):
    r = index[0]
    c = index[1]
    
    s = 'XMAS'
    ans = 0

    i = r
    j = c
    cnt = 0
    while(i < len(g) and j < len(g[0])and cnt < len(s) and g[i][j] == s[cnt]):
        cnt += 1
        i += 1
        j += 1
    
    if cnt == 4:
        ans+=1
   
    i = r
    j = c
    cnt = 0
    while(i>=0 and j>=0 and i < len(g) and j < len(g[0])and cnt < len(s) and g[i][j] == s[cnt]):
        cnt += 1
        i -= 1
        j -= 1
    
    if cnt == 4:
        ans+=1

    i = r
    j = c
    cnt = 0
    while(i>=0 and j>=0 and i < len(g) and j < len(g[0])and cnt < len(s) and g[i][j] == s[cnt]):
        cnt += 1
        i -= 1
        j += 1
    
    if cnt == 4:
        ans+=1

    i = r
    j = c
    cnt = 0
    while(i>=0 and j>=0 and i < len(g) and j < len(g[0])and cnt < len(s) and g[i][j] == s[cnt]):
        cnt += 1
        i += 1
        j -= 1
    
    if cnt == 4:
        ans+=1
    
    i = r
    j = c
    cnt = 0
    while(i < len(g) and j < len(g[0]) and cnt < len(s) and g[i][j] == s[cnt]):
        cnt += 1
        i += 1
    if cnt == 4:
        ans+=1
    
    i = r
    j = c
    cnt = 0
    while(i < len(g) and j < len(g[0]) and cnt < len(s) and g[i][j] == s[cnt]):
        cnt += 1
        j += 1
    if cnt == 4:
        ans+=1


    i = r
    j = c
    cnt = 0
    while(i >= 0 and j>=0 and cnt < len(s) and g[i][j] == s[cnt]):
        cnt += 1
        i -= 1
    if cnt == 4:
        ans+=1
    
    i = r
    j = c
    cnt = 0
    while(i >= 0 and j>=0 and cnt < len(s) and g[i][j] == s[cnt]):
        cnt += 1
        j -= 1
    if cnt == 4:
        ans+=1
        
    return ans

print(sol2(g))
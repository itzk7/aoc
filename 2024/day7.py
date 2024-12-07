with open('inputs/input07.txt') as inputfile:
    inp = inputfile.read()


def parse_input():
    g = []
    for l in inp.split('\n'):
        t = []
        total, vals = l.split(":")
        key = int(total.strip())
        vals = list(map(lambda x: x.strip(), vals.split(" ")))
        vals = list(filter(lambda x: x!='', vals))
        vals = list(map(int, vals))
        g.append([key, vals])
    return g

g = parse_input()
dp = {}
def backtrack(total, l, curr, idx):
    if total == curr:
        # print(total)
        return True

    if curr > total or idx >= len(l):
        return False
        
    num = l[idx]
    return backtrack(total, l, curr + num, idx + 1) or backtrack(total, l, curr * num, idx + 1)
    
    
def sol1():
    ans = 0
    for l in g:
        if backtrack(l[0], l[1], 0, 0):
            ans += l[0]
    return ans


def backtrack2(total, l, curr, idx):
    if total == curr:
        print(total)
        return True

    if idx >= len(l):
        return False
        
    num = l[idx]
    print(curr,num, int(str(curr) + '' + str(num)))
    return backtrack2(total, l, curr + num, idx + 1) or backtrack2(total, l, curr * num, idx + 1) or backtrack2(total, l, int(str(curr) + '' + str(num)), idx + 1)
    
    
def sol2():
    ans = 0
    for l in g:
        if backtrack2(l[0], l[1], 0, 0):
            ans += l[0]
    return ans

print(sol1())
print(sol2())
        

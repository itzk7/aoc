inp = ''
def parse_input():
    with open('inputs/input09.txt') as inputfile:
        inp = inputfile.read()
    return inp

def sol1():
    a, _, _ = populate()
    j = len(a) - 1
    i = 0
    while i < len(a) and i < j:
        if a[i] == '.':
            t = a[i]
            a[i] = a[j]
            a[j] = t
            j -= 1
            while(j >= 0 and a[j] == '.'):
                j-=1
        i += 1
    ans = 0
    for i in range(len(a)):
        if(a[i] != '.'):
            ans += i * a[i]

    return ans


def sol2():
    a, dot, number = populate()
    j = len(number) - 1
    i = 0
    while j >=0:
        for i in range(len(dot)):
            if dot[i][0] > dot[i][1]:
                continue
            
            num_length = number[j][1] - number[j][0] + 1
            dot_length = dot[i][1] - dot[i][0] + 1
            if num_length <= dot_length and number[j][0] >= dot[i][0]:
                t = a[number[j][0]]
                for k in range(dot[i][0], dot[i][0] + num_length):
                    a[k] = t
                dot[i][0] = dot[i][0] + num_length
                for k in range(number[j][0], number[j][1] + 1):
                    a[k] = '.'
                break
        j-=1
    ans = 0
    for i in range(len(a)):
        if(a[i] != '.'):
            ans += i * a[i]

    return ans

def populate():
    id = 0
    toggle = 0
    a = []
    dot = []
    number = []
    index = 0
    for i in inp:
        n = int(i)
        if toggle % 2 == 0:
            a.extend([id] * n)
            number.append([index, index + n - 1])
            id+=1
        else:
            a.extend(['.'] * n)
            dot.append([index, index + n - 1])
        index += n
        toggle += 1
    return a,dot,number

inp = parse_input()
print(sol1())
inp = parse_input()
print(sol2())
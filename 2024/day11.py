with open('inputs/input11.txt') as inputfile:
        inp = inputfile.read()

def parse_input():
    l = inp.split(" ")
    l = list(map(int, l))
    return l

dp = {}
def apply_rules(l, count):
    print(count)
    if count >= 75:
        return l
    
    new_l = []
    for i in range(len(l)):
        if l[i] == 0:
            new_l.append(1)
        elif len(str(l[i]))%2 == 0:
            temp = str(l[i])
            left_half = temp[0:len(temp)//2]
            right_half = temp[len(temp)//2:]
            new_l.append(int(left_half))
            new_l.append(int(right_half))
        else:
            new_l.append(l[i] * 2024)
    return apply_rules(new_l, count + 1)

def sol1():
    l = parse_input()
    l = apply_rules(l, 0)
    return len(l)

# optimised after hint
def progress_blinks(dp, count, blinks = 25):
    
    if count >= blinks:
        return dp
    
    new_dp = {}
    for i in dp:
        k = blink(i)
        for j in k:
            new_dp[j] = new_dp.get(j, 0) + dp[i]

    return progress_blinks(new_dp, count + 1, blinks)

def blink(l):
    if l == 0:
        return [1]
    elif len(str(l))%2 == 0:
        temp = str(l)
        left_half = temp[0:len(temp)//2]
        right_half = temp[len(temp)//2:]
        return [int(left_half), int(right_half)]
    else:
        return [(l * 2024)]
def sol(blinks = 25):
    l = parse_input()
    dp = {}
    for i in l:
        dp[i] = 1

    dp = progress_blinks(dp, 0, blinks)
    
    ans = 0
    for i in dp:
        ans += dp[i]
    
    return ans

print(sol())
print(sol(75))


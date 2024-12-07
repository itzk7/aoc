with open('inputs/input05.txt') as inputfile:
    inp = inputfile.read()

def parse_input():
    rules = {}
    pages = []
    for l in inp.split('\n'):
        if '|' in l:
            a, b = l.split('|')
            a = int(a)
            b = int(b)
            t = rules.get(b, [])
            t.append(a)
            rules[b] = t 
        else:
            if not l:
                continue
            p = l.split(',')
            p = list(map(int, p))
            pages.append(p)
    return rules, pages

rules, pages = parse_input()

def sol1(rules, pages):
    ans = 0
    for page in pages:
        valid_page = True
        for r in rules:
            for i in range(len(page)): 
                if page[i] == r:
                    for j in range(i + 1, len(page)):
                        if page[j] in rules[r]:
                            valid_page = False
                            break
                if not valid_page:
                    break
        if valid_page:
            ans += page[len(page) // 2]
    return ans

def sol2(rules, pages):
    ans = 0
    for page in pages:
        valid_page = True
        for r in rules:
            for i in range(len(page)): 
                if page[i] == r:
                    for j in range(i + 1, len(page)):
                        if page[j] in rules[r]:
                            valid_page = False
                            break
                if not valid_page:
                    break
        if not valid_page:
            for i in range(len(page)):
                for j in range(i + 1, len(page)):
                    if page[i] in rules and page[j] in rules[page[i]]:
                        t = page[i]
                        page[i] = page[j]
                        page[j] = t
                        j += 1
            ans += page[len(page) // 2]
    return ans

print(sol1(rules, pages))
print(sol2(rules, pages))


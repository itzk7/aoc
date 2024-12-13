with open('inputs/input13.txt') as inputfile:
    inp = inputfile.read()

class Button:
    def __init__(self, x, y, unit) -> None:
        self.x = x
        self.y = y
        self.unit = unit
        self.cnt = 0
        pass
    
    @staticmethod
    def parse(s, unit):
        # Button B: X+27, Y+71
        _, r = s.split(":")
        x_str, y_str = r.split(",")
        _, x = x_str.split("+")
        _, y = y_str.split("+")
        return Button(int(x), int(y), unit)

class Dest:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        pass
    
    @staticmethod
    def parse(s):
        # Button B: X+27, Y+71
        _, r = s.split(":")
        x_str, y_str = r.split(",")
        _, x = x_str.split("=")
        _, y = y_str.split("=")
        return Dest(10000000000000 + int(x), 10000000000000 + int(y))
        # return Dest(int(x), int(y))
    

class Machine:
    def __init__(self, btn_a: Button, btn_b: Button, dest: Dest):
        self.btn_a = btn_a
        self.btn_b = btn_b
        
        self.dest = dest
        self.ans = -1
        self.dp = set()

    
    def _opt_dfs(self):
        ans = 0
        # for i in range(1, 10000):
        #     for j in range(1, 10000):
        #         key = str(i) + "_" + str(j)
        #         print(i * self.btn_a.x + j * self.btn_b.x \
        #             , i * self.btn_a.y + j * self.btn_b.y)
        #         if i * self.btn_a.x + j * self.btn_b.x == self.dest.x \
        #             and i * self.btn_a.y + j * self.btn_b.y == self.dest.y:
        #                 ans += i * self.btn_a.unit + j * self.btn_b.unit
        #                 return ans
        
        x1 = self.btn_a.x
        y1 = self.btn_b.x
        
        x2 = self.btn_a.y
        y2 = self.btn_b.y

        c1 = self.dest.x
        c2 = self.dest.y
        # a * x1 + b * x2 = c1
        # a * y1 + b * y2 = c2
        # a(x1-y1) + b * (x2 - y2) = c1 - c2
        # solve for b
        numerator = c2 - (c1 * x2) / x1
        denominator = y2 - (y1 * x2)/x1
        b = numerator / denominator
        # now solve for a
        a = (c1 - b * y1) / x1        
        a = round(a)
        b = round(b)
        ans = a * self.btn_a.unit + b * self.btn_b.unit
        
        if a * self.btn_a.x + b * self.btn_b.x == self.dest.x \
            and  a * self.btn_a.y + b * self.btn_b.y == self.dest.y:
            return int(ans)
        return 0
                        
    
    def find(self):
        return self._dfs(0, 0, 0, 0)

    def find2(self):
        return self._opt_dfs()
def parse_input() -> list:
    g = []
    for l in inp.split('\n\n'):
        if not l:
            continue
        b_a, b_b, p = l.split("\n")
        
        g.append(Machine(Button.parse(b_a, 3), Button.parse(b_b, 1), Dest.parse(p)))
    return g

g = parse_input()
ans = 0
for m in g:
    ans += m.find2()

print(ans)
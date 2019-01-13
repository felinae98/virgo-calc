import fractions
import random
import math

class Node:
    def __init__(self, power_symb = "^"):
        self.type = 0
        # 0 for empty
        # 1 for node
        # 2 for number
        self.operator = None
        self.left = None
        self.right = None
        self.number = 0
        self.power_symb = power_symb
    
    def _get_piority(self, operator):
        if operator == "^": return 3
        elif operator == "*" or operator == "/": return 2
        elif operator == "+" or operator == "-": return 1

    def __str__(self):
        if self.type == 2:
            return str(self.number)
        elif self.type == 1:
            rt = ''
            if self.left.type == 1 and self._get_piority(self.operator) > self._get_piority(self.left.operator):
                rt += "(" + str(self.left) + ")"
            else: 
                rt += str(self.left)
            if self.operator == "^":
                rt += self.power_symb
            else:
                rt += self.operator
            if self.right.type == 1 and self._get_piority(self.operator) >= self._get_piority(self.right.operator):
                rt += "(" + str(self.right) + ")"
            else:
                rt += str(self.right)
            return rt
        else:
            raise Exception
        
    def solve(self):
        if self.type == 2:
            return
        else:
            self.left.solve()
            self.right.solve()
            if self.operator == "+":
                self.number = self.left.number + self.right.number
            elif self.operator == "-":
                self.number = self.left.number - self.right.number
            elif self.operator == "*":
                self.number = self.left.number * self.right.number
            elif self.operator == "/":
                self.number = self.left.number / self.right.number
            elif self.operator == "^":
                self.number = self.left.number ** self.right.number
    
    def __hash__(self):
        # dfs polish notation
        # opt num num
        # 0-50 is number
        # 51 + 52 - 53 * 54 / 55 ^
        if self.type == 2:
            return int(self.number)
        elif self.type == 1:
            # dfs
            if self.operator == "+":
                res = 51
            elif self.operator == "-":
                res = 52
            elif self.operator == "*":
                res = 53
            elif self.operator == "/":
                res = 54
            elif self.operator == "^":
                res = 55
            if (self.operator == "*" or self.operator == "+") \
                and (self.left.number < self.right.number):
                right = hash(self.right)
                res <<= (math.ceil(right.bit_length() / 6) * 6)
                res = res | right
                left = hash(self.left)
                res <<= (math.ceil(left.bit_length() / 6) * 6)
                res = res | left
            else:
                left = hash(self.left)
                res <<= (math.ceil(left.bit_length() / 6) * 6)
                res = res | left
                right = hash(self.right)
                res <<= (math.ceil(right.bit_length() / 6) * 6)
                res = res | right
            return res

class Problem:

    def __init__(self):
        self.root = Node()
        self.operator_set = ["+", "-", "*", "/", "^"]
        self.operator_weight = [8, 8, 4, 2, 1]

    def generate(self):
        while True:
            empty_node_set = [self.root]
            hard_level = random.randrange(2, 5)
            # the number of calcs
            # generate structure
            for _ in range(hard_level):
                node = random.choice(empty_node_set)
                empty_node_set.remove(node)
                node.operator = random.choices(self.operator_set, weights=self.operator_weight)[0]
                node.type = 1
                if node.operator == "^":
                    node.left = Node()
                    node.right = Node()
                    node.right.type = 2
                    node.right.number = random.randrange(1,4)
                    empty_node_set.append(node.left)
                else:
                    node.left = Node()
                    empty_node_set.append(node.left)
                    node.right = Node()
                    empty_node_set.append(node.right)
            # fill number
            for node in empty_node_set:
                node.type = 2
                node.number = fractions.Fraction(random.randrange(0, 50))
            # test
            try:
                self.root.solve()
                if abs(self.root.number.numerator) + self.root.number.denominator > 100:
                    continue
                    # too hard
            except:
                continue
                # devide 0
            break
            

    def __str__(self):
        return str(self.root)
        
    def test(self):
        for _ in range(10):
            print(random.choices(self.operator_set, weights=self.operator_weight))

    def __hash__(self):
        return hash(self.root)

def _read_hash(h):
    rt = []
    while h:
        rt.insert(0, h % 64)
        h //= 64
    return rt

if __name__ == "__main__":
    a = Problem()
    a.generate()
    print(a)
    print(a.root.number)
    h = hash(a)
    print(h)
    print(_read_hash(h))

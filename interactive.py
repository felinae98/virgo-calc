#!/usr/bin/env python3
from problem import Problem
import argparse
from fractions import Fraction

def interactive(num, symb):
    right_ans = 0
    print("""Hello, welcome to virgo-calc.
The following are some problems and you need to answer it.
You need to answer it directly, like 9 or -5.
If the answer is decimal, please answer it in fraction like 4/9
Enjoy it!""")
    for _ in range(num):
        problem = Problem(symb)
        problem.generate()
        print(str(problem) + "=?")
        while True:
            ans = input("Your answer:")
            try:
                ans_num = Fraction(ans)
                break
            except:
                print("Your input is invalid, please try again")
        if ans_num == problem.root.number:
            right_ans += 1
            print("Gooood! You are right")
        else:
            print("Nonono, the correct answer is {}".format(problem.root.number))
    print("That's your score: {}/{}".format(right_ans, num))
        

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("num", help="the number of problems to solve", type=int)
    args.add_argument("-p", help="the simbol of power operation", choices=["^", "**"], default="^", dest="symb")
    arg = args.parse_args()
    interactive(arg.num, arg.symb)
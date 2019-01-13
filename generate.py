#!/usr/bin/env python3

from problem import Problem
import argparse

def generate(num, file, symb="^"):
    for _ in range(num):
        problem = Problem()
        file.write(str(problem) + "=?\n")
    file.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", help="The output file", type=argparse.FileType("w"), required=True, dest="file")
    parser.add_argument("-n", help="the number of problems to be generated", type=int, default=1000, dest="num")
    parser.add_argument("-p", help="power symbol", choices=['^', "**"], dest="symb", default="^")
    args = parser.parse_args()
    generate(args.num, args.file, args.symb)

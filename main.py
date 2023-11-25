import sys
from os.path import dirname as dirn
from copy import deepcopy as dcopy

CFILE = dirn(__file__)

def run(code):
    code = list(code + "\0")
    pos = 0

    stack = []
    retStack = []
    buf = ""

    while (code[pos] != "\0"):
        ch = code[pos]
        if (ch == ";"):
            sys.exit(0)
        elif (ch in "0123456789"):
            while (code[pos] in "0123456789"):
                buf += code[pos]
                pos += 1
            pos -= 1
            stack.append(int(buf))
            buf = ""
        elif (ch == "-"):
            stack.append(dcopy(stack[-1]))
        elif (ch == "."):
            print(stack.pop(), end = "")
        elif (ch == "~"):
            pos += 1
            ch = code[pos]
            if (ch == "s"):
                print(" ", end = "")
            elif (ch == "n"):
                print()
            elif (ch == "N"):
                print(69, end = "")
            elif (ch == "H"):
                print("Hello World!", end = "")
        elif (ch == "O"):
            stack.append([])
        elif (ch == "r"):
            pos += 1
            ch = code[pos]
            if (ch == "S"):
                sto = stack.pop()
                sta = stack.pop()
                stack.append(list(range(sta, sto)))
        elif (ch == "["):
            pos += 1
            ch = code[pos]
            if (ch == "s"):
                stack[-1] = sum(stack[-1])
        elif (ch == "i"):
            stack.append(int(input()))
        elif (ch == "+"):
            stack[-2] += stack[-1]
            stack.pop()
        pos += 1

assert sys.argv[1].endswith(".gj"), f"File extension `.{sys.argv[1].split('.')[-1]}` is not supported. The supported one is `.gj`"
with open(f"{CFILE}/{sys.argv[1]}") as fl:
    cdr = fl.read()
run(cdr)


#!/usr/bin/env python3
import sys

def shrink(string) -> str:
    return string[:8]

def enlarge(string) -> str:
    return string + "Z" * (8 - len(string))

def main():
    args = sys.argv[1:]
    if len(args) < 1:
        print("none")
        return
    for arg in args:
        if len(arg) > 8:
            print(shrink(arg))
        elif len(arg) < 8:
            print(enlarge(arg))
        else:
            print(arg)
main()

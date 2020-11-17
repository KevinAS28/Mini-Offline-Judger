#!/bin/python3

debug_step = 0
def debug(object, msg=""):
    global debug_step
    debug_msg = "[DEBUG]: " + str(debug_step)
    print(debug_msg)
    print("|",end="")
    print(object,end="")
    print("|")
    if msg!="":
        print(msg)
    print(debug_msg)
    input("Continue?")
    print("\n\n")
    debug_step += 1

def solution(x):
    return str(x)


if __name__=="__main__":
    solution()
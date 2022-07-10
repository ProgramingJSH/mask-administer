import select
import sys


def readInput(timeOut):

    i, o, e = select.select([sys.stdin], [], [], timeOut)

    if (i):
        return sys.stdin.readline().strip()
    else:
        return "nothing"

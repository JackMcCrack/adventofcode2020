#!/usr/bin/python3


def read_input(filename):
    a = []
    b = []
    tmp = []
    lines=open(filename, "r")
    for i in lines:
        if '\n' == i:
            a = tmp
            tmp = []
        else:
            if ':' not in i:
                tmp.append(int(i.strip()))
    b = tmp
    return a, b 

def play(a, b):
    if a[0] > b[0]:
        a.append(a[0])
        a.append(b[0])
    else:
        b.append(b[0])
        b.append(a[0])
    a.pop(0)
    b.pop(0)

def score(a):
    l = len(a)
    ret = 0
    for x in range(l):
        ret += (a[x] * (l-x))
    return ret

if __name__ == '__main__':
    a,b = read_input("input")
    while len(a) > 0 and len(b) > 0:
        play(a, b)
    print(score(a))
    print(score(b))


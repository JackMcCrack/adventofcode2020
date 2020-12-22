#!/usr/bin/python3
from copy import deepcopy

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

def play(tmpa, tmpb):
    print('subgame:', tmpa, tmpb)
    a = deepcopy(tmpa)
    b = deepcopy(tmpb)
    win = None
    while len(a) > 0 and len(b) > 0:
        # recursion - start a subgame
        if len(a) < a[0] and len(b) < b[0]:
            subgamewin = play(a[1:a[0]+1], b[1:b[0]+1])
            if subgamewin == 'a':
                a.append(a[0])
                a.append(b[0])
            else:
                b.append(b[0])
                b.append(a[0])


        # traditionla - bigger number wins
        else:
            if a[0] > b[0]:
                a.append(a[0])
                a.append(b[0])
            else:
                b.append(b[0])
                b.append(a[0])
        a.pop(0)
        b.pop(0)
        print('\t', a, b)
    if len(a) > 0:
        print(score(a), 'a\t', tmpa, tmpb, a, b)
        win = 'a'
    else:
        print(score(b), 'b\t', tmpa, tmpb, a, b)
        win = 'b'
        
    return win
        
def score(a):
    l = len(a)
    ret = 0
    for x in range(l):
        ret += (a[x] * (l-x))
    return ret

if __name__ == '__main__':
    a,b = read_input("input")
    play(a, b)


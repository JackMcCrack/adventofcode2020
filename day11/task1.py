#!/usr/bin/python3
from copy import deepcopy

def read_input(filename):
    read = []
    lines=open(filename, "r")
    for i in lines:
        read.append(Convert(i.strip()))
    return read

# Python code to convert string to list character-wise 
def Convert(string): 
    list1=[] 
    list1[:0]=string 
    return list1

def prnt(f):
    for x in range(0, len(f)):
        print("".join(f[x]))

def nextstep(f):
    cur = f
    nex = deepcopy(f)   # https://stackoverflow.com/questions/8744113
    chn = 0
    for x in range(0, len(f)):
        for y in range(0,len(f[x])):
            # walk line by line, left to right

            if cur[x][y] != '.':
                # do not change floor
                c = count(cur,x,y)
                #print(x,y,c)
                if c == 0 and cur[x][y] == 'L':
                    # next: '#' Seat occupied
                    nex[x][y] = '#'
                if c >= 4 and cur[x][y] == '#':
                    # next: 'L' Seat occupied
                    nex[x][y] = 'L'
                if cur[x][y] != nex[x][y]:
                    chn += 1
    return nex, chn

def count(f,x,y):
    # walk top to bottom line, left to right
    # '.' FLOOR
    # 'L' Seat empty
    # '#' Seat occupied
    occ = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if     x+i >= 0 and \
                   x+i < len(f) and \
                    y+j >= 0 and \
                    y+j < len(f[x+i]) and \
                    not (i ==0 and  j == 0):
                        #print(x,y,x+i,y+j,f[x+i][y+j])
                        if f[x+i][y+j] == '#':
                            occ += 1

    return occ

def countallocc(f):
    occ = 0
    for x in range(0, len(f)):
        for y in range(0,len(f[x])):
            if f[x][y] == '#':
                occ += 1
    return occ

if __name__ == '__main__':
    f = read_input("input")
    prnt(f)
    c = 1
    while c > 0: 
        n, c = nextstep(f)
        f = deepcopy(n)
        print('====', 'changes:', c)
        prnt(n)

    print(countallocc(f))


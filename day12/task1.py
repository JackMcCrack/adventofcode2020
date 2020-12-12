#!/usr/bin/python3


def read_input(filename):
    read = []
    lines=open(filename, "r")
    for i in lines:
        read.append([i.strip()[0], int (i.strip()[1:len(i.strip())])])
    return read

if __name__ == '__main__':
    f = read_input("input")
    lo = [ 0, 0 ] # [w/e, s/n]
    direct = ['E', 'S', 'W', 'N']
    di = direct[0]
    for co in f:
        
        if co[0] == 'F':
            c = di
        else:
            c = co[0]

        if c == 'S':
            lo = [ lo[0], lo[1] - co[1]]
        if c == 'N':
            lo = [ lo[0], lo[1] + co[1]]
        if c == 'E':
            lo = [ lo[0] + co[1], lo[1]]
        if c == 'W':
            lo = [ lo[0] - co[1], lo[1]]
        
        if c == 'L':
            di = direct[(direct.index(di) - (int(co[1]/90)) ) % 4]
        if c == 'R':
            di = direct[(direct.index(di) + (int(co[1]/90)) ) % 4]
        print(co, di, lo)
    print(lo, abs(lo[0])+abs(lo[1]))


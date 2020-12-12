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
    wp = [ 10, 1 ]
    for co in f:
        
        if co[0] == 'F':
            lo = [lo[0] + wp[0] * co[1], lo[1] + wp[1] * co[1]]
        
        c = co[0]

        if c == 'S':
            wp = [ wp[0], wp[1] - co[1]]
        if c == 'N':
            wp = [ wp[0], wp[1] + co[1]]
        if c == 'E':
            wp = [ wp[0] + co[1], wp[1]]
        if c == 'W':
            wp = [ wp[0] - co[1], wp[1]]
        
        if c == 'L':
            for s in range(int(co[1]/90) % 4 ):
                print("turn: %s\t%s\t%s\t%s" %(di, co, s, wp))
                wp = [wp[1] * -1, wp[0] * 1]
                di = direct[(direct.index(di) - 1) % 4]

        if c == 'R':
            for s in range(int(co[1]/90) % 4 ):
                print("turn: %s\t%s\t%s\t%s" %(di, co, s, wp))
                wp = [wp[1] * 1, wp[0] * -1]
                di = direct[(direct.index(di) + 1) % 4]


        print("%s\t%s\t%s\t%s" %(co, di, wp, lo))
    print(lo, abs(lo[0])+abs(lo[1]))


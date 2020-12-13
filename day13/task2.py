#!/usr/bin/python3


def read_input(filename):
    read = []
    lines=open(filename, "r")
    for i in lines:
        read.append(i.strip())
        #read.append(int(i.strip()))
        #read.append("".split(i.strip()))
    return read



if __name__ == '__main__':
    f = read_input("input")
    ts = 100000000000000
    bus = []
    o = []
    raw_bus = f[1].split(',')
    for b in f[1].split(','):
        if b != 'x':
            bus.append(int(b))
        else:
            bus.append(-1)
    tmp = bus[:]
    for b in bus:
        m = max(tmp)
        if m > 0:
            o.append(bus.index(m))
            tmp.remove(m)
            print(bus,o)
    run = True
    while run:
        m = 0
        while m < len(o):
            if (ts+o[m]) % bus[o[m]] == 0:
                #print(ts, m, o[m], bus[o[m]])
                m += 1
            else:
                m = 0
                ts += 1
        run = False 
    print(ts, m, o[m], bus[o[m]])

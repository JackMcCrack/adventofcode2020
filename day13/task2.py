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
        lts = []
        for i in o:
            lts.append(0)
        while m < len(o):
            if (ts+o[m]) % bus[o[m]] == 0:
                if m > (len(o)/3):
                    print(ts, m, o[m], bus[o[m]])
                lts[m] = ts
                m += 1
            else:
                m = 0
                if lts[m] > 0:
                    ts = lts[m] + bus[o[m]]
                else:
                    ts += 1
        run = False
    m -= 1
    print(ts, m, o[m], bus[o[m]])

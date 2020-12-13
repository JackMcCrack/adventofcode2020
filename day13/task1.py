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
    ts = int(f[0])

    for bus in f[1].split(','):
        if bus != 'x':
            b = int(bus)
            nxdep = ts + b - ( ts % b )
            res = (nxdep - ts) * b
            print(b - ( ts % b ), res)

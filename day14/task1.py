#!/usr/bin/python3


def read_input(filename):
    read = []
    lines=open(filename, "r")
    for i in lines:
        #read.append(i.strip())
        #read.append(int(i.strip()))
        read.append(i.strip().split(' = '))
    return read

def int2bit(i, mask=None):
    bit = '{0:036b}'.format(int(i))
    b = ''
    if mask is not None:
        for x in range( len(bit)):
            if mask[x] != 'X':
                b = b+mask[x]
            else:
                b = b+bit[x]
    return b

def bit2int(b):
    return int(b,2)

if __name__ == '__main__':
    f = read_input("input")
    mask = ''
    mem = dict()
    for line in f:
        if line[0] == 'mask':
            mask = line[1]
            print(line)
        elif line[0][0:3] == 'mem':
            mem.update({line[0][4:-1]: int2bit(line[1], mask)})
    print(mem)
    sum = 0
    for i, j in mem.items():
        sum += bit2int(j)
    print(sum)

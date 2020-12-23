#!/usr/bin/python3


def read_input(filename):
    read = []
    lines=open(filename, "r")
    for i in lines:
        for j in range(len(i.strip())):
            read.append(int(i[j]))
    return read


def turn(c, p):
    m = []
    dest = c[p] - 1
    np = -1
    print(c, '\t c[p]:', c[p],'\t')
    for x in range(3):
        # copy 3 numbers to m
        t = ( p + 1 + x ) % len(c)
        m.append(c[t])
        np = c[(t+1) % len(c)]
    for x in m:
        # remove numbers in m from c
        c.remove(x)
    print(m, '\t\t\t picked')
    while dest not in c:
        # if we cut the smaler number out, try lower, until we are below the lowest number.
        dest -= 1
        if dest < min(c):
            dest = max(c)
    print(dest, '\t\t\t\t dest')
    for x in range(3):
        c.insert(c.index(dest)+1+x, m[x])
        #print(c.index(dest)+1+x, p, c.index(dest)+1+x -p, '\t', end='')
    p = c.index(np)

# offset calculation is harrd ;)
#    off = c.index(dest)+4 -p
#    print(off, c.index(dest)+4, p)
#    if off < 3 :
#        p = ( p + 4 ) % len(c)
#    else:
#        p = ( p + 1 ) % len(c)
    return c, p


if __name__ == '__main__':
    cups = read_input("input")
    cur = 0
    count = 0
    while count < 100:
        cups, cur = turn(cups, cur)
        count += 1
    for x in range(len(cups)-1):
        print(cups[(cups.index(1) +1 + x)%len(cups)], end='')
    print('')

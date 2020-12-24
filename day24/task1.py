#!/usr/bin/python3

def read_input(filename):
    read = []
    lines=open(filename, "r")
    for i in lines:
        read.append(i.strip())
        #read.append(int(i.strip()))
        #read.append("".split(i.strip()))
    return read


def walk(d='', a=[0,0,0]):
    #print(d,a)
    # https://www.redblobgames.com/grids/hexagons/
    x = 0
    y = 1
    z = 2
    ret = a[:]    
    if d == 'e':
        ret[x] += 1
        ret[y] -= 1
    if d == 'w':
        ret[x] -= 1
        ret[y] += 1
    if d == 'nw':
        ret[y] += 1
        ret[z] -= 1
    if d == 'se':
        ret[y] -= 1
        ret[z] += 1
    if d == 'sw':
        ret[x] -= 1
        ret[z] += 1
    if d == 'ne':
        ret[x] += 1
        ret[z] -= 1


    return ret


if __name__ == '__main__':
            # x, y, z
    start = [ 0, 0, 0]
    tiles = dict()
    f = read_input("input")
    for line in f:
        a = start
        i = 0
        while i < (len(line)):
            if line[i] == 'w' or line[i] == 'e':
                a =walk(line[i], a)
            else:
                a =walk(line[i:i+2], a)
                i += 1

            i += 1
        if (a[0], a[1], a[2]) in tiles:
            tiles[a[0], a[1], a[2]] += 1
        else:
            tiles[a[0], a[1], a[2]] = 1
    black = 0
    white = 0
    for t,v in tiles.items():
        print(t,v%2)
        if v%2 == 1:
            black += 1
        else:
            white += 1
    print('b', black, 'w', white)

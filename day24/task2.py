#!/usr/bin/python3
from copy import deepcopy


directions = [ [+1, -1, 0], [+1, 0, -1], [0, +1, -1], [-1, +1, 0], [-1, 0, +1], [0, -1, +1] ]

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

def countbw(tiles):
    black = 0
    white = 0
    for t,v in tiles.items():
        #print(t,v%2)
        if v%2 == 1:
            black += 1
        else:
            white += 1
    print('b', black, 'w', white)

def counthere(tiles=dict(), a= [0,0,0]):
    ret = 0 # min 0, max 6 black tiles
    for i, j, k in directions:
        if not (i == 0 and j == 0 and k == 0):
            if (a[0]+i, a[1]+j, a[2]+k) in tiles and\
                    tiles[a[0]+i, a[1]+j, a[2]+k] %2 == 1:
                ret += 1
    return ret


def nxtstp(tiles=dict()):
    nxt = dict()
    for t, v in tiles.items():
        for i, j, k in directions:
            black = False
            a = ( t[0]+i, t[1]+j, t[2]+k )
            cnt = counthere(tiles, a)

            if a in tiles.keys():
                black = (tiles[a] % 2 == 1)
                if (black and (cnt < 1 or cnt > 2)) or\
                        (not black and cnt == 2):
                    nxt[a] = flipp(tiles, a) 
                else:
                    nxt[a] = tiles[a]
            else:
                if cnt == 2:
                    nxt[a] = flipp(tiles, a)
            #print(a, black, cnt, '\t > ', a in nxt.keys() and nxt[a] % 2 == 1, a in nxt.keys())
    return nxt


def flipp(t=dict(), a=[0,0,0]):
    ret = 0
    if (a[0], a[1], a[2]) in tiles:
        ret = t[a[0], a[1], a[2]] + 1
    else:
        ret = 1

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
        tiles[a[0], a[1], a[2]] =flipp(tiles, (a[0], a[1], a[2]))
    for i in range(100):
        print(i, '\t', end='')
        countbw(tiles) 
        tiles = nxtstp(tiles)
    
    countbw(tiles) 


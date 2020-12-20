#!/usr/bin/python3


def read_input(filename):
    tiles = dict()
    field = []
    lines=open(filename, "r")
    for i in lines:
        if len(i) > 1:
            if ':' in i:
                no = int(i[5:9])
            else:
                field.append(i.strip())
        else:
            tiles[no] = field
            field = []
    return tiles 

def addtosearch(s, side, no):
    if side not in s:
        s[side] = set()
    s[side].add(no)
    rev = side[::-1]
    if rev not in s:
        s[rev] = set()
    s[rev].add(no+'r')
    return s

if __name__ == '__main__':
    search = dict()
    fit = dict()
    nofit = dict()
    f = read_input("input")
    for line in f.items():
        no = line[0]
        a = line[1][0]
        b = ''
        d = ''
        for x in line[1]:
            b += x[9]
            d += x[0]
        c = line[1][9]
        search = addtosearch(search, a, str(no)+'a')
        search = addtosearch(search, b, str(no)+'b')
        search = addtosearch(search, c, str(no)+'c')
        search = addtosearch(search, d, str(no)+'d')
        nofit[no] = 0
        fit[no] = 0

    for pattern, match in search.items():
        if len(match) == 1:
            nofit[int(list(match)[0][0:4])] += len(match) 

    part1 = 1
    for x,v in nofit.items():
        if int(v/2) == 2:
           part1 *= x
           print(x)
    print(part1)

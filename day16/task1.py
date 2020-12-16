#!/usr/bin/python3


def read_input(filename):
    read = []
    rules = []
    lines=open(filename, "r")
    for i in lines:
        if '-' in i: 
            r = (i.split(':')[1].strip().split(' or '))
            rules.append([r[0].split('-'), r[1].split('-')])
        if ':' not in i and '-' not in i and len(i)>2:
            #read.append(int(i.strip()))
            r = []
            tmp = i.strip().split(',')
            for x in tmp:
                r.append(int(x))
            read.append(r)
        for x in range(len(rules)):
            for y in range(len(rules[x])):
                for z in range(len(rules[x][y])):
                    rules[x][y][z] = int(rules[x][y][z])
    return read, rules


def checkvalid(i = 0, r = None):
    ret = False
    if r is not None:
        for x in range(len(r)):
            for y in range(len(r[x])):
                print(x, y, r[x][y], i)
                if i >= r[x][y][0] and i <= r[x][y][1]:
                    ret = True

    return ret


if __name__ == '__main__':
    f, r = read_input("input")
    error = 0
    for line in r:
        print(line)
    for line in f:
        for i in line:
            if checkvalid(i, r) == False:
                error += i
    print(error)

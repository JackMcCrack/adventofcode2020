#!/usr/bin/python3


def read_input(filename):
    read = []
    lines=open(filename, "r")
    for i in lines:
        read.append(i.strip())
    return read

if __name__ == '__main__':
    trees = 0
    locx = 0
    locy = 0
    stepx = 3
    stepy = 1
    treemap = read_input("input")
    for line in treemap:
        
        if (line[locx]) == '#':
            trees += 1
        locx = (locx + stepx) % len(line)
        locy = locy + stepy

    print(trees)

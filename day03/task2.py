#!/usr/bin/python3


def read_input(filename):
    read = []
    lines=open(filename, "r")
    for i in lines:
        read.append(i.strip())
    return read

if __name__ == '__main__':
    trees = []
    treemap = read_input("input")
    steps = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    for (stepx, stepy) in steps:
        locx = 0
        locy = 0
        t=0
        for line in treemap:
            if locy % stepy == 0:
                if (line[locx]) == '#':
                    t += 1
                locx = (locx + stepx) % len(line)
            locy += 1
        trees.append(t)
    #print(trees)
    total = 1
    for x in trees:
        total = total * x
    print(total)


#!/usr/bin/python3


def read_input(filename):
    read = []
    lines=open(filename, "r")
    for i in lines:
        read.append(int(i.strip()))
    return read

if __name__ == '__main__':
    f = read_input("input")
    j = 0
    jdifsum = [0, 0, 1]
    unused = f
    while len(unused) > 0:
        for y in range(1,4):
            if j + y in unused:
                print(j, y, unused, jdifsum)
                unused.remove(j + y)
                j = j + y
                jdifsum[y-1] += 1
                break
        print(j, y, unused, jdifsum)
    print( jdifsum, jdifsum[0]*jdifsum[2])

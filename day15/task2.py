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
    for line in f:
        a = 1

#!/usr/bin/python3

def read_input(filename):
    read = []
    lines=open(filename, "r")
    for i in lines:
        read.append(int(i.strip()))
    return read

if __name__ == '__main__':
    f = read_input("input")
    read = []
    for i in f:
        read.append(i)
        for j in read:
            if i+j==2020:
                print(i, '+', j, "=", 2020)
                print(i, '*', j, "=", i*j)
                break


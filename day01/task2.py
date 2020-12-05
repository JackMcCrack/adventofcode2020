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
    done = False
    for i in f:
        read.append(i)
        for j in read:
            for k in read:
                if i+j+k==2020:
                    print(i, '+', j, '+', k, '=', 2020)
                    print(i, '*', j, '*', k, '=', i * j * k)
                    done = True
                    break
            if done:
                break


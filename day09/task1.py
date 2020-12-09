#!/usr/bin/python3


def read_input(filename):
    read = []
    lines=open(filename, "r")
    for i in lines:
        read.append(int(i.strip()))
    return read

if __name__ == '__main__':
    f = read_input("input")
    pre = 25
    pos = 0
    for line in f:
        if pos >= pre:
            s = f[pos-pre:pos]
            match = False
            for x in s:
                if line - x in s \
                        and line-(2 * x) != 0:
                    match = True
            if match == False:
                print(line, s)
                print(match)

        pos += 1
        

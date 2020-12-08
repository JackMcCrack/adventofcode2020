#!/usr/bin/python3


def read_input(filename):
    read = []
    lines=open(filename, "r")
    for i in lines:
        read.append(i.strip())
    return read

if __name__ == '__main__':
    acc = 0
    pos = 0
    ins = read_input("input")
    done = [False for i in range(len(ins))]
    while done[pos] == False:
        done[pos] = True
        print(done)
        i = ins[pos].split()
        if i[0] == "nop":
            pos += 1

        if i[0] == "acc":
            acc += int(i[1])
            pos += 1

        if i[0] == "jmp":
            pos += int(i[1])
    print(acc)

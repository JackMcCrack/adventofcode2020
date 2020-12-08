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
    stop = False
    ins = read_input("input")
    done = [False for i in range(len(ins)+1)]
    while done[pos] == False and stop == False:
        #lets write all executed instructions into loop.txt
        #print(pos+1, done[pos], ins[pos])
            

        done[pos] = True
        i = ins[pos].split()
        if i[0] == "nop":
            pos += 1

        if i[0] == "acc":
            acc += int(i[1])
            pos += 1

        if i[0] == "jmp":
            pos += int(i[1])

        if pos >= len(ins):
            print(pos, len(ins))
            stop = True
    print(acc)
    print(pos, done[pos], ins[pos])

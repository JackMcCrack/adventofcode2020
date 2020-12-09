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
                hit = line

        pos += 1
        

    pos = 0
    for line in f:
        su = 0
        x = 1
        while su < hit and pos + x < len(f):
            tmp = f[pos:pos+x]
            su = sum(tmp)
            x += 1
        if su == hit:
           print(tmp, "++++++> ",min(tmp)+max(tmp)) 
        pos += 1 


        

#!/usr/bin/python3


def read_input(filename):
    read = []
    lines=open(filename, "r")
    for i in lines:
        read.append(int(i.strip()))
    return read


knowpath = {}
def findnext(f, i):
    if i == len(f)-1:
        return 1
    if i in knowpath:
        return knowpath[i]
    ans = 0
    for j in range(i+1, len(f)):
        if f[j]-f[i]<=3:
            ans += findnext(f, j)
    knowpath[i] = ans
    return ans



if __name__ == '__main__':
    f = read_input("input")
    f.append(0)
    f.sort()
    print(f)
    path = []
    print(findnext(f, 0))

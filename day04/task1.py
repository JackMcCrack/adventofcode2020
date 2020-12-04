#!/usr/bin/python3


def read_input(filename):
    read = []
    lines=open(filename, "r")
    for i in lines:
        read.append(i.strip())
    return read

if __name__ == '__main__':
    f = read_input("input")
    passport = {}
    p = []
    validcouter = 0
    for line in f:
        if line == "":
            p.append(passport)
            passport = {}
        else:
            for i in line.split():
                passport[i.split(':')[0]]= i.split(':')[1]
    p.append(passport)
   
    print(p)
    for check in p:
        valid = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid' }
        result = True
        for v in valid:
            if v in check.keys():
                print(v, check[v])
            else:
                result = False
                print(v, None)
        if result:
            validcouter += 1
    print(validcouter)

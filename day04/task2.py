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
   
    for check in p:
        valid = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid' }
        result = True
        for v in valid:
            if v not in check.keys():
                result = False
                print('keys')
        if result:
            if int(check['byr']) < 1920 or int(check['byr']) > 2002:
                result = False
                print('keys-byr', check['byr'])

            if int(check['iyr']) < 2010 or int(check['iyr']) > 2020:
                result = False
                print('keys-iyr', check['iyr'])
            
            if int(check['eyr']) < 2020 or int(check['eyr']) > 2030:
                result = False
                print('keys-eyr', check['eyr'])

            if check['hgt'][-2:len(check['hgt'])] == 'cm' \
                    and (int(check['hgt'][0:-2]) < 150 \
                    or int(check['hgt'][0:-2]) > 193):
                result = False
                print('keys-cm', check['hgt'])
            if check['hgt'][-2:len(check['hgt'])] == "in" \
                    and (int(check['hgt'][0:-2]) < 59 \
                    or int(check['hgt'][0:-2]) > 76):
                result = False
                print('keys-in', check['hgt'])
            if check['hgt'][-2:len(check['hgt'])] != 'cm' and check['hgt'][-2:len(check['hgt'])] != "in":
                result = False
                print('keys-hgt', check['hgt'])


            if check['hcl'][0] != '#' or not all(c in '0123456789abcdefABCDEF' for c in check['hcl'][1:-1]):
                result = False
                print('keys-hcl'), check['hcl']
            
            if check['ecl'] not in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
                result = False
                print('keys-ecl', check['ecl'])

            if len(check['pid']) != 9:
                result = False
                print('keys-pid', check['pid'])




        if result:
            validcouter += 1
            print('OK', check)
    print(validcouter)

#!/usr/bin/python3


def read_input(filename):
    read = []
    lines=open(filename, "r")
    for i in lines:
        read.append(i.strip())
    return read

def findcontainer(rules, color):
    found = []
    for r, c in rules.items():
        if r[1] in color:
            found.append(r[0])
    for c in color:
        found.append(c)
    return list(dict.fromkeys(found))

def findbags(rules, color):
    found = []
    i = 0
    for r, c in rules.items():
        if r[0] in color and r[1] is not None:
            found.append(r[1])
            ret = findbags(rules, r[1])
            print(c, r[1], ret)
            if ret > 0:
                i+=(c*ret)
            i += c
    return i 

if __name__ == '__main__':
    f = read_input("input")
    colors = []
    rules = {}
    for line in f:
        rule = line.split() 
        bag = "-".join(rule[0:2]) 
        contain = (rule[4:len(rule)])
        colors.append(bag)
        for i in ' '.join(contain).split(','): 
            rule = i.strip().split()[0:3]
            if rule ==['no', 'other', 'bags.']:
                rule = [0, None]
            else:
                rule = [int(rule[0]), "-".join(rule[1:3])]
            rules[bag, rule[1]] = rule[0] 
    
    length = 0
    search = ['shiny-gold']
    while length < len(search):
        length = len(search)
        search = findcontainer(rules, search)
    #print(len(search)-1) 

    search = ['shiny-gold']
    print(findbags(rules, search)) 

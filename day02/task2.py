#!/usr/bin/python3
lines=open("input", "r")
valid = 0
for i in lines:
    i = i.strip()
    s = i.index(':')
    rule = i[0:s].split()
    pw = i[s+2:len(i)]
    rule_limit = rule[0].partition('-')
    rule_min = int(rule_limit[0])-1
    rule_max = int(rule_limit[2])-1
    count = pw.count(rule[1])
    print(pw[rule_min],rule[1],pw[rule_max],rule[1])
    if  (pw[rule_min] == rule[1] or pw[rule_max] == rule[1]) and not (pw[rule_min] == rule[1] and pw[rule_max] == rule[1]):
        valid += 1
print(valid)

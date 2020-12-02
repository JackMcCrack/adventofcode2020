#!/usr/bin/python3
lines=open("input", "r")
valid = 0
for i in lines:
    i = i.strip()
    s = i.index(':')
    rule = i[0:s].split()
    pw = i[s+2:len(i)]
    rule_limit = rule[0].partition('-')
    rule_min = int(rule_limit[0])
    rule_max = int(rule_limit[2])
    count = pw.count(rule[1])
    if count >= rule_min and count <= rule_max:
        print (rule_limit, pw, pw.count(rule[1]))
        valid += 1
print(valid)

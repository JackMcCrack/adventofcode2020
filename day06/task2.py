#!/usr/bin/python3

import string

def read_input(filename):
    read = []
    lines=open(filename, "r")
    for i in lines:
        read.append(i.strip())
    return read

def counter(group):
    q = []
    for c in string.ascii_lowercase:
        result = True
        for x in group:
            if c not in x:
                result = False
        if result:
            print('hello')
            q.append(c)
    print(group, len(set(q)))
    return len(set(q))

if __name__ == '__main__':
    f = read_input("input")
    questions = []
    group = []
    for line in f:
        if line == "":
            questions.append(counter(group))
            group = []
        else:
            group.append(line)

    questions.append(counter(group))

    qsum = 0
    for q in questions:
        qsum += q
    print(questions, qsum)



#!/usr/bin/python3


def read_input(filename):
    read = []
    lines=open(filename, "r")
    for i in lines:
        read.append(i.strip())
    return read

if __name__ == '__main__':
    f = read_input("input")
    q = []
    questions = []
    for line in f:
        if line == "":
            questions.append(set(q))
            q = []
        for c in line:
            if c not in questions:
                q.append(c)
    questions.append(set(q))
    qsum = 0
    for q in questions:
        qsum += len(q)
    print(questions, qsum)



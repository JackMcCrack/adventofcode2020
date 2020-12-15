#!/usr/bin/python3


def read_input(filename):
    r = []
    read = []
    lines=open(filename, "r")
    for i in lines:
        r = i.strip().split(',')
    for i in r:
        read.append(int(i))
    return read

def speak(s, i, t):
    if i in s:
        # has been spoken before
        if len(s.get(i)) > 1:
            a = s.get(i)[-2:-1][0]  # 2nd last time
            b = s.get(i)[-1:][0]    # last time
            i = b - a
            #print(t, b-a, i ,s)
        else:
            # it was the first time 
            i = 0
        if i in s:
            s.get(i).append(t)
        else:
            s.update({i: [t]})

    else:
        # has not been spoken yet
        s.update({i: [t]})
        i = 0
    return i

if __name__ == '__main__':
    f = read_input("input")
    turn = 1
    spoken = dict()
    last = int()

    # read the input
    for i in f: 
        spoken.update({i: [turn]})
        last = i
        turn += 1
    # run until 2020
    while turn <= 30000000:
        last = speak(spoken, last, turn) 
        turn += 1
        if turn % 1000 == 0:
            print(turn)
    #print(spoken)
    print(last)

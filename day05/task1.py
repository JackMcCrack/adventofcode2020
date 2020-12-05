#!/usr/bin/python3


def read_input(filename):
    read = []
    lines=open(filename, "r")
    for i in lines:
        read.append(i.strip())
    return read

if __name__ == '__main__':
    f = read_input("input")
    max_sid = 0
    for line in f:
        top = 127
        bot = 0
        stop = 7
        sbot = 0
        for c in line:
            #print (c, line, top, bot, '-', stop, sbot)
            if c == "F":
                top = (((top  + 1) - bot) / 2) - 1 + bot
            if c == "B":
                bot = ((top + 1) - bot ) / 2 + bot
            if c == "L":
                stop = (((stop  + 1) - sbot) / 2) - 1 + sbot
            if c == "R":
                sbot = ((stop + 1) - sbot ) / 2 + sbot
        sid = top*8 + stop
        print ('000', line, top, bot, '-', stop, sbot, 'id:', sid)
        if max_sid < sid:
            max_sid = sid
    print(max_sid)

#!/usr/bin/python3
numbers=open("input", "r")
read=[]
for i in numbers:
    i = int(i.strip())
    read.append(i)
    for j in read:
        for k in read:
            if i+j+k==2020:
                print(i, '+', j, '+', k, "=", 2020)
                print(i, '*', j, '*', k, "=", i*j*k)
                break


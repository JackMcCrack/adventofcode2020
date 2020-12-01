#!/usr/bin/python3
numbers=open("input", "r")
read=[]
for i in numbers:
    i = int(i.strip())
    read.append(i)
    for j in read:
        if i+j==2020:
            print(i, '+', j, "=", 2020)
            print(i, '*', j, "=", i*j)
            break


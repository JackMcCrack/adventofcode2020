#!/usr/bin/python3
from copy import deepcopy

def read_input(filename):
    read = []
    lines=open(filename, "r")
    for i in lines:
        read.append(i.strip())
        #read.append(int(i.strip()))
        #read.append("".split(i.strip()))
    return read

# '#'   active
# '.'   inactive
# 
#    If a cube is '#' and exactly 2 or 3 of its neighbors are also '#', the cube remains '#'. Otherwise, the cube becomes '.'.
#    If a cube is '.' but exactly 3 of its neighbors are '#', the cube becomes '#'. Otherwise, the cube remains '.'.

#start len(f) x len(f[0]) x 1
#6. cy len(f)+2*6 x len(f[0])+2*6 x 1+2*6   #worst case
#


#
# Calculate the next step
#
def nstep(f):
    
    n = deepcopy(f)
    for i in range(len(f)):
        for j in range(len(f[i])):
            for k in range(len(f[i][j])):
                cnt = cnthere(f, i, j, k)
                if      (f[i][j][k] == '#' and cnt >= 2 and cnt <= 3) or\
                        (f[i][j][k] == '.' and cnt == 3):
                    n[i][j][k] = '#'
                else:
                    n[i][j][k] = '.'
    return n

#
# Count all neighbors of the given position
#
def cnthere(f, x, y, z):
    count = 0
    for i in range(-1,2):
        for j in range(-1,2):
            for k in range(-1,2):
                if x+i >= 0 and x+i < len(f) and\
                        y+j >= 0 and y+j < len(f[i]) and\
                        z+k >= 0 and z+k < len(f[i][j]):
                    #print(x, y, z, i, j, k)
                    if  (not (i == 0 and j == 0 and k == 0)) and\
                        f[x+i][y+j][z+k] == '#':
                        count += 1
    return count

if __name__ == '__main__':
    f = read_input("input")
    maxcy = 6                       # max. cycles
    imax = len(f)+2*maxcy
    jmax = len(f[0])+2*maxcy
    kmax = 1+2*maxcy

    # lets extend the map, so we never have negativ indexes
    m = [ [ [ 0 for k in range(kmax) ] for j in range(jmax) ] for i in range(imax) ]


    # put input in "the center" of the map
    for i in range(0, imax):
        for j in range(0, jmax):
            for k in range(0,kmax):
                if      (i <= maxcy or i > imax-maxcy) or\
                        (j <= maxcy or j > jmax-maxcy) or\
                        (k <= maxcy or k > kmax-maxcy):
                    m[i][j][k] = '.'
                else:
                    #print(i,j,k, maxcy, imax, jmax, kmax)
                    m[i][j][k] = f[maxcy-i][maxcy-j]


    # run maxcy iterations
    for cy in range(0, maxcy):
        for k in range(0, kmax):
            print('\ncy=', cy, 'z=', k)
            for i in range(0, imax):
                print('')
                for j in range(0, jmax):
                    print(m[i][j][k], end='')
        m = nstep(m)


    # count all actives
    count = 0
    for i in range(0, imax):
        for j in range(0, jmax):
            for k in range(0,kmax):
                if m[i][j][k] == '#':
                    count += 1
    print(count)

#!/usr/bin/python3


def read_input(filename):
    read = []
    lines=open(filename, "r")
    for i in lines:
        #read.append(i.strip())
        #read.append(int(i.strip()))
        read.append(i.strip().split(' = '))
    return read


# convert the given address i with the mask into a list of addresses, returns the int address
def findalladdr(i, mask=None):
    bit = '{0:036b}'.format(int(i))
    b = ''
    print('bit:', bit)
    print('mas:', mask)
    if mask is not None:
        for x in range( len(bit)):
            if mask[x] == '0':
                b = b+bit[x]
            else: 
                b = b+mask[x]
            #print('b:  ', b) 
        if 'X' in b:
            r = []
            
            # count all the 'X's
            c = b.count('X') 
            #create a binary string template with the length of X-count
            formatstr = '{0:0' + str(c) + 'b}' 
            binmap = [formatstr.format(int(i)) for i in range(2 ** c)] # fill with 2^X-count 
            
            #print(binmap) # for evey X in the string we have all both options as a replacement from the binmap
            for bm in binmap:
                tmp = b[:]
                for x in range(len(bm)):
                    #replace 1 'X' by one value from binmap(0 or 1)
                    tmp = tmp.replace('X', bm[x], 1)
                #print('t', tmp, bit2int(tmp))
                r.append(bit2int(tmp))
            print('r:', r)
            b = r
    #print('b:', b)
    return b

# bitmask to int
def bit2int(b):
    return int(b,2)

if __name__ == '__main__':
    f = read_input("input")
    
    
    mask = ''       # current mask
    mem = dict()    # memory


    for line in f:
        if line[0] == 'mask':
            mask = line[1]
            #print(line)
        elif line[0][0:3] == 'mem':
            addr = []
            #print(line[0][4:-1])
            x = line[0][4:-1]
            addr = findalladdr(x, mask)
            for a in addr:
                # write the value in all addresses we got back from findalladdr
                mem.update({a: line[1]})

    # check all mem entries and sum them up
    total = 0
    for i, j in mem.items():
        total += int(j)
    print(total)

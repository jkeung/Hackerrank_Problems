#!/bin/python

import sys

t = int(raw_input().strip())

def scan_matrix(G, P):
    # iterate through the grid
    for i, row in enumerate(G):
        # scan each character in the row
        for index in range(len(row)-len(P[0])+1):
            # check to see if the first row of the pattern is in current index
            if P[0]==row[index:index+len(P[0])]:
                lines_matched = 0
                for j, subrow in enumerate(P):
                    if G[i+j][index:index+len(P[0])] == P[j]:
                        lines_matched+=1
                # if all number of lines match return 'YES' 
                if lines_matched==len(P):
                    return 'YES'
    return 'NO'
                  
    
for a0 in xrange(t):
    # define large array
    R,C = map(int, raw_input().strip().split(' '))
    G = []
    for _ in xrange(R):
        row = str(raw_input().strip())
        G.append(row)
    # define search pattern
    r,c = map(int, raw_input().strip().split(' '))
    P = []
    for _ in xrange(r):
        subrow = str(raw_input().strip())
        P.append(subrow)
        
    print scan_matrix(G,P)

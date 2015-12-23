#!/bin/python

import sys


time = raw_input().strip()

am_or_pm = time[-2:]

if am_or_pm == 'PM':
    hour = str(int(time[:2]) + 12)
    minute = time[3:5]
    second = time[6:8]
    
    if hour == '24':
        hour = '12'
    
elif am_or_pm == 'AM':
    hour = str(time[:2])
    minute = time[3:5]
    second = time[6:8]
    
    if hour == '12':
        hour = '00'
        
print hour + ':' + minute + ':' + second

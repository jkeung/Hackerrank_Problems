#!/bin/python

import sys


h = int(raw_input().strip())
m = int(raw_input().strip())

numbers = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 
            8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 
            15:'quarter', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 
            21:'twenty one', 22:'twenty two', 23:'twenty three', 24:'twenty four', 25:'twenty five', 
            26:'twenty six', 27:'twenty seven', 28:'twenty eight', 29:'twenty nine', 30:'half'}

def time_in_words(h,m):
    if h < 12:
        if m<=30:
            hours = numbers[h]
        else:
            if h > 12:
                hours = numbers[1]
            else:
                hours = numbers[h+1]

    if m==0:
        return hours + " o' clock "
    elif m==1:
        return numbers[m] + ' minute past' + hours
    elif m==15 or m==30:
        return numbers[m] + ' past ' + hours
    elif m<30:
        return numbers[m] + ' minutes past ' + hours
    elif m>30 and (60-m==15):
        return numbers[60-m] + ' to ' + hours
    else:
        return numbers[60-m] + ' minutes to ' + hours
    

print time_in_words(h,m)

# Enter your code here. Read input from STDIN. Print output to STDOUT
import string
letter_dict = dict(zip(string.lowercase, range(1,27)))
t = int(raw_input())

def funny(word):
    for i in range(len(word)/2+1):
        if abs(letter_dict[word[i+1]] - letter_dict[word[i]]) == abs(letter_dict[word[-i-2]] - letter_dict[word[-i-1]]):
            pass
        else:
            return 'Not Funny'
    return 'Funny'

for i in range(t):
    word = raw_input()
    print funny(word)

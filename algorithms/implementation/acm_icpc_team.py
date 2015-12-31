#!/bin/python

import sys

n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
topic = []
topic_i = 0
for topic_i in xrange(n):
    topic_t = str(raw_input().strip())
    topic.append(int(topic_t,2))

# get number of max topics by doing bitwise or statement over all topics
max_topics = 0
for i in range(len(topic)):
    for j in range(i+1, len(topic)):
        max_topics = max(max_topics, bin(topic[i]|topic[j]).count("1"))

# get number of two person combinations that can achieve max topics
num_max_topics = 0
for i in range(len(topic)):
    for j in range(i+1, len(topic)):
        if bin(topic[i]|topic[j]).count("1") == max_topics:
            num_max_topics += 1

print max_topics
print num_max_topics

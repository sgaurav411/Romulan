import matplotlib.pyplot as plt
import sys
import operator
import argparse
import requests
import time
import urllib
from bs4 import BeautifulSoup


def func(k):
    validLetters = "abcdefghijklmnopqrstuvwxyz"
    s=""
    for char in k:
        if char in validLetters:
            s+=char
    return s

start_time = time.time()
address="http://www.gutenberg.org/files/2701/2701-0.txt"
content=urllib.request.urlopen(address)

doc={}
last="rn"
#aise_hi=[]
for line in content:
    x=str(line)
    x=x[1:]
    #@x=' '+x
    words=x.split(' ')
    for entry in words:
        k=str(entry)
        k.strip()
        k.lower()
        func(k)
        if(len(k)>2):
            rn=k[-2:]
            if(rn==last):
                k=k[:-2]
        #aise_hi.append(k)
        #whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        #k = ''.join(filter(whitelist.__contains__, k))
        #k=func(k)        
        k=k.lower()
        if(k!=' ' and k!=''):
            if (doc.__contains__(k)):
                doc[k] = int(doc.get(k)) + 1
            else:
               doc[k] = 1
sort_orders = sorted(doc.items(), key=lambda x: x[1], reverse=True)
#print(sort_orders)
just_the_rank=[]
just_the_occur=[]
c=1
for x,y in sort_orders:
    #print(x,"::",y)
    just_the_occur.append(c)
    just_the_rank.append(y)
    c+=1


plt.ylabel("Total Number of Occurrences")
plt.xlabel("Rank of word")
plt.loglog(just_the_rank, just_the_occur, base=10)

#print(aise_hi)
plt.show()

print("--- %s seconds ---" % (time.time() - start_time))
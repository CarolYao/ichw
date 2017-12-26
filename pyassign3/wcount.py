
# coding: utf-8

# In[ ]:


#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Zhangsan"
__pkuid__  = "1600012345"
__email__  = "zhangsan@pku.edu.cn"
"""

import sys
from urllib.request import urlopen


def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """

    words=lines.split()
    wordlist=[]
    wordcount=[]
    for i in words:
        if i in wordlist:
            wordcount[wordlist.index(i)]+=1
        else:
            wordlist.append(i)
            wordcount.append(1)
    
    value=[]
    for i in len(wordlist):
        value.append((wordcount[i],wordlist[i]))
    
    value.sort(reverse=True)
    top=value[:topn]
    
    for (number,word) in top:
        print(word,'\t',number)
    # your code goes here
    pass

if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines   = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)


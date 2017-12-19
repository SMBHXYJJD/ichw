#!/usr/bin/env python3

"""wcount.py: .

__author__ = "Weixuyan"
__pkuid__  = "1700011733"
__email__  = "weixuyan@pku.edu.cn"
"""

import sys
import re
from urllib.request import urlopen
from string import punctuation

def cutoff(text):
    '''cut the article into single words
    '''

    text2 = re.sub(r'[{}]+'.format(punctuation),'',text)
    text2 = re.sub('\n',' ',text2)
    text2 = re.sub('\r',' ',text2)
    text2 = text2.lower()
    j = text2.split(' ')
    while '' in j:
        j.remove('')
    
    return j

def conum(list1):
    '''count how many times does a word appears
    '''
    dict1={}
    for i in list1:
        if i not in dict1 :
            dict1[i] = 1
        else:
            dict1[i] += 1

    return dict1


def totuple(dict1):
    '''transfer a dict into a list of tuple'''
    
    list2=[]

    list2 =list(dict1.items()) #fouzechuxian<built-in method items of dict object at>
    return list2



def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
    b=cutoff(lines)
    
    c=conum(b)
    
    d=totuple(c)
          
    e= sorted(d,key=lambda tupl: tupl[1] ,reverse=True)

    try:
        for i in range(0 , topn):
            k = e[i]
            
            space = 15-len(str(k[0]))-len(str(k[1]))
            print (k[0],' ' * space, k[1])
        
    except Exception as err:
            print(err)
    
    
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


import re
from collections import Counter

def check(wordlb):
    pattern = r'_[a-z]+'
    len_w_b = len(wordlb.split('_'))
    labellist = []
    lines = ''
    if len_w_b == 2:
        word, lb = wordlb.split('_')
        #print(word, lb)
    elif len_w_b < 2:
        lines += "无标签或没有词：" + wordlb + '\n'
        word, lb = 'NULL', 'NULL'
        #lines += word + ' ' + lb
        wordlb = 'NULL' + '_' + 'NULL'
    else:
        lines += "缺少空格：" + wordlb + '\n'
        labellist += re.findall(pattern, wordlb)
        for i in range(len(labellist)-1):
            wordlb = ''.join(wordlb.split(labellist[i], 1)[0] + labellist[i] + \
                 ' ' + wordlb.split(labellist[i], 1)[1])
            #print(wordlb)
        for ll in wordlb.split(' '):
            if len(ll.split('_')) % 2 == 0: 
                word, lb = ll.split('_')
                #lines += word + ' ' + lb + '\n'
                
            else:
                word, lb = 'NULL','NULL'
                wordlb = 'NULL' + '_' + 'NULL'

    return lines, wordlb



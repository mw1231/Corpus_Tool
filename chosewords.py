#coding:utf-8
import re


# cut off the word's _
def quxhx(word):
    if word is not None:
        words = word.strip().split("_")
        newword = words[0]
        return newword


# useless
def back_vi(w):
    if re.match(r'.+nr', w) is not None:
        #print(w)
        return w

    else:
        return 'Not_vi'


# take out the punctuation
def tp(line):
    line1 = []
    for a in line.strip().split(' '):
        if a[-2:] == 'ww':
            continue
        else:
            line1.append(a)
    return line1


# take the left words of the l_word
def lwst(line, word):
    if line:
        l_line = line.split(word)
        # print(len(l_line))
        # if len(l_line) >= 2:  #if the word is the end of the sentence
        return l_line[0]
        # else:
        #    return '0'


# take the right words of the r_word
def rwst(line, word):
    if line:
        l_line = line.split(word)
        # print(len(l_line))
        # if len(l_line) >= 2:          #if the word is the end of the sentence
        return l_line[1]
        # else:
        # return '0'


def choseTword(file, wtype='_bo', outfile='out_test.txt'):
    out_l = []
    out_v = []
    out_r = []
    fo = open(outfile, 'w', encoding='utf-8')
    with open(file, 'r', encoding='utf-8') as ft:
        nb = 0  # the number of word's line
        #print(nb)
        while True:
            line_i = ft.readline()
            nb = nb + 1  
            # open the file line
            #print(nb)
            if line_i:
                line = tp(line_i)
                for i in line:
                    # process every token
                    m = re.findall(r"(.+" + wtype + ')', i)
                    #print(m)
                    # find the center words in the
                    if m is not None:
                        for mc in m:
                            #print(mc)
                            index = line.index(mc)
                            l_word = quxhx(line[index - 1])  # find the left word
                            v_word = quxhx(line[index])  # the center word
                            if index < len(line) - 1:  # if there has a right word
                                r_word = quxhx(line[index + 1])
                                rs = rwst(line_i, r_word)
                            else:
                                r_word = '0'  # if there is no right word,show 0
                            ls = lwst(line_i, l_word)
                            out_l.append(l_word)
                            out_v.append(v_word)
                            out_r.append(r_word)
                            #outline = (str(nb) + '.' + '|' + l_word + '--' + v_word + '--' + r_word + '|' + '\n')
                            #fo.write(
                            #    str(nb) + '.' + ls + '|' + l_word + '--' + v_word + '--' + r_word + '|' + rs + '\n')
                            #print(outline)

                            
                            a =   ("<tr>\
                            <td><font color='black' size='10'>%s.</font></td>\
                            <td><font color='black' size='10'>%s</font></td>\
                            <td><font color='green' size='10'>%s</font>\
                                <font color='red' size='10'>%s</font> \
                                <font color='blue' size='10'>%s</font></td> \
                            <td><font color='black' size='10'>%s</font></td>\
                                </tr><br>" \
                                 % (str(nb), ls, l_word, v_word, r_word, rs)) 
                            fo.write(a)
            else:
                break

    #fstr = 'The number is: ' + str(len(out_l))

    
    fo.close()
    return out_l, out_v, out_r
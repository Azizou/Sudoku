import os,sys

class CustomString(str):

    def __init__(self,string):
       self.str = str(string)


    def __cmp(self,dec1,dec2):
        if dec1<dec2: return -1
        elif dec1==dec2: return 0
        else: return 1
    def __cmp__(self,cstring):
        if not isinstance(cstring,CustomString):
            cstring = CustomString(cstring)
        l1 = len(self.str)
        l2 = len(cstring.str)
        str1,str2,l1,l2,reordered = (self.str, cstring.str, l1, l2,False) if l1 <= l2 else (cstring.str, self.str, l2, l1, True)
        dec1 = dec2 = ''
        cont = False
        for i in range(l1):
            if (not ( cont or str1[i].isdecimal() or str2[i].isdecimal())) and str1[i] != str2[i]:
                return self.__cmp(str1,str2) if not reordered else self.__cmp(str2,str1)
            if str1[i].isdecimal() and str2[i].isdecimal():#Both decimal, read more to decide
                #read to end of dec
                cont = True
                dec1 += str1[i]
                dec2 += str2[i]
            elif cont:#Not both are decs
                if str1[i].isdecimal():
                    dec1 += str1[i]
                elif str2[i].isdecimal():
                    dec2 += str2[i]
                else: #final decision
                    dec1,dec2 = eval(dec1),eval(dec2)
                    return self.__cmp(dec1,dec2) if not reordered else self.__cmp(str2,str1)
        else:
            if l1 < l2 and str2[l1].isdecimal():
                dec2 += str2[l1]
            if dec1 == '':
                dec1 = '0'
            if dec2 == '':
                dec2 = '0'
            dec1,dec2 = eval(dec1),eval(dec2)
            return self.__cmp(dec1,dec2) if not reordered else self.__cmp(str2,str1)

    def __lt__(self,value):
        return self.__cmp__(value)== -1

##    def __eq__(self, value):
##        return self.__cmp__(value)==0
##
##    def __gt__(self,value):
##        return self.__cmp__(value)==1
##
##    def __ge__(self,value):
##        return self.__cmp__(value)>=0
##
##    def __le__(self,value):
##        return self.__cmp__(value)<=0
##        
def find_prefix(word1, word2):
    l1 = len(word1)
    l2 = len(word2)
   # word1,word2,l1,l2 =  (word1,word2,l1,l2) if l1 > l2 else (word2,word1,l2,l1)
    if l1 < l2 :
        word1, word2 = word2, word1
        l1,l2 = l2,l1
    #print(word1,word2)
    for i in range(l1):
        if i< l2:
            if word1[i] != word2[i]:
                return word1[:i]
        else:
            return word1[:i]
    else: return word1

def find_prefix3(word1,word2,word3):
    w1 = find_prefix(word1,word2)
    w2 = find_prefix(w1,word3)
    return w2 #find_prefix(w1,w2)

def find_prefix_list(words):
    res = ''
    if len(words) == 0:
        return ''
    if len(words)<2:
        return words[0]
    res = find_prefix(words[0],words[1])
    for i in words[2:]:
        res = find_prefix(res,i)
    return res


def extract_decimal(prefix,word):
    l = len(prefix)
    lw = len(word)
    if lw<=l or not word[l].isdecimal():
        return -1
    #r = len(word[l:])
    res = ''
    for i in range(l,lw):
        if word[i].isdecimal() or word[i]=='.':
            res += word[i]
        else: break
    return eval(res)
def extract_all_decimal(words):
    prefix = find_prefix_list(words)
    res = []
    for word in words:
        res.append(extract_decimal(prefix,word))
    return res

def print_ordered(words):
    decs = extract_all_decimal(words)
    mapp = dict(zip(decs,words))
    decs.sort()
    for i in decs:
        print(mapp[i])

def main2():
    w = "Dragon ball episode "
    w1 = "Dragon ball episode 1"
    w2 = "Dragon ball episode 2"
    w10 = "Dragon ball episode 10"
    w100 = "Dragon ball episode 100"
    w11 = "Dragon ball episode 11"
    words = [w100,w10,w11,w1,w2,w]
   
    decs = extract_all_decimal(words)
    mapp = dict(zip(decs,words))
    decs.sort()
    for i in decs:
        print(mapp[i]) 

    wordss = []
    for word in words:
        wordss.append(CustomString(word))
    wordss.sort()

    for word in wordss: print(word)

def main():
    path = 'C:\\Users\\Claude\\dwhelper\\Guilty Chrown'
#    path = sys.argv[1]
    os.chdir(path)
    files = os.listdir()
    titles = [CustomString(name) for name in files]
    titles.sort()
    for name in titles: print(name)


if __name__ == '__main__':
    main()

import vigenerecipher
import re,itertools
import enchant
from math import gcd
from functools import partial
MAX_KEY_LENGTH = 30



def find_patterns(len_key):
    all_patterns = {}
    with open('ciphertext.txt','r') as f:
        data = f.read()
        data = re.sub(r"\W", "", data)  #strip  \n \t and spaces
        data = ''.join(e for e in data if e.isalpha())
        f.close()
        for i,c in enumerate(data):
            pattern = data[i:i+len_key]   #Work in progress
            if pattern not in all_patterns:
                if len(pattern) == len_key:
                    k=0
                    for m in re.finditer(pattern, data):
                        if k == 0:
                            all_patterns[pattern] = []
                        else:
                            all_patterns[pattern].append(m.start()-i)
                        k += 1
                else:
                    continue
            else:
                continue
        return all_patterns

def find_key_length(patterns):

    for key, value in iter(patterns.items()):
        if(len(value) > 2):
            num1 = value[0]
            num2 = value[1]
            test = gcd(num1, num2)
            for i,val in enumerate(value):
                if i >= 2:    #to skip the first two that were done previously
                    test = gcd(test,value[i])
                else:
                    continue
            patterns[key] = test
        else:
            patterns[key] = 0
            continue

    for key,value in iter(patterns.items()):
        print("%s : %d" % (key, value))

    return
    #return key_length  Work in progress




def main():
    patterns=[]
    for i in range(3, (MAX_KEY_LENGTH+1)):
        patterns =  find_patterns(i)
        find_key_length(patterns)
        #testkey = find_key_length(patterns) Work in progress



if __name__ == '__main__':
	main()

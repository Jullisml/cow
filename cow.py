import numpy as np
import re

file = open('hello.cow', 'r')
rd = file.read()
a = re.sub(r'\n', r' ', rd)
a = a.split(' ')

stek = []
dctnr = {}
ixx = 0

result = np.zeros(1000)

for item in a:
    if item == 'MOO':
        stek.append(ixx)
    if item == 'moo':
        dctnr[ixx]=stek[len(stek)-1]
        dctnr[stek.pop()] = ixx
    ixx += 1
    
K = 0
i = 0

while(i != len(a)):
    if a[i] == 'MoO':
        result[K] += 1
    if a[i] == 'MOo':
        result[K] -= 1
    if a[i] == 'moO':
        K += 1
    if a[i] == 'mOo':
        K -= 1
    if a[i] == 'OOM':
        print(chr(int(result[K])))
    if a[i] == 'Moo':
        if a[K] != 0:
            print(chr(int(result[K])))
    if a[i] == 'OOO':
        a[K] = 0
    if a[i] == 'moo':
        i = dctnr[i]-1
    if a[i] == 'MOO':
        if result[K] == 0:
            i = dctnr[i]
    if a[i] == '':
        pass
    else:
        i += 1
        continue
    i += 1

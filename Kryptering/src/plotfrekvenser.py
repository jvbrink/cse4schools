# -*- coding: utf-8 -*-

import string
import numpy as np
from matplotlib.pyplot import *

freq_no = [6.24, 2.04, 0.19, 3.56, 14.64, 2.16, 3.82, 1.27, 5.98, 1.15, 3.69, 
           5.86, 3.18, 7.13, 5.22, 1.53, 0.10, 8.02, 7.38, 8.27, 1.65, 2.42, 
           0.10, 0.10, 0.51, 0.10, 0.25, 0.89, 2.55]

freq_en = [8.04, 1.48, 3.34, 3.82, 12.49, 2.40, 1.87, 5.05, 7.57, 0.16, 0.54,
           4.07, 2.51, 7.23, 7.64, 2.14, 0.12, 6.28, 6.51, 9.28, 2.73, 1.05,
           1.68, 0.23, 1.66, 0.09, 0.00, 0.00, 0.00]

ind = np.arange(29.)
width = 0.35
adj = ind.copy(); adj[26:] += width/2.0


fig, ax = subplots()
rects1 = ax.bar(adj, freq_no, width, color='r')
rects2 = ax.bar(ind+width, freq_en, width, color='b')

ax.set_xticks(ind+width)
alphabet = [char for char in string.ascii_uppercase]
alphabet.append(r'$\bf \rm \AE$')
alphabet.append(r'$\bf \rm \O$')
alphabet.append(r'$\bf \rm \AA$')

ax.set_yticklabels(range(0, 18, 2), fontsize=22)
ax.set_ylabel('%', fontsize=22)
ax.set_xticklabels(alphabet, fontsize=22)

ax.set_title('Frekvens av hvor ofte bokstaver blir brukt', fontsize=22)
ax.legend(['Norsk', 'Engelsk'], fontsize=22)

show()













test = np.array([4.9,
        1.6,
        0.15,
        2.8,
        11.5,
        1.7,
        3.0,
        1.0,
        4.7,
        0.9,
        2.9,
        4.6,
        2.5,
        5.6,
        4.1,
        1.2,
        0.0,
        6.3,
        5.8,
        6.5,
        1.3,
        1.9,
        0.0,
        0.0,
        0.4,
        0.0,
        0.2,
        0.7,
        2.0])


test /= np.sum(test)/99.6

test[test==0.0] = 0.1
print "freq_no = ["
for i in test:
    print "%.2f," % i,
print "]"
print np.sum(test)
 



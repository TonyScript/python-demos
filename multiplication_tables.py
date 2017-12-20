#/usr/local/bin/python3
# -*- coding: utf-8 -*-
# form __feature__ import print_function

for i in range(9, 0, -1):
    for j in range(i, 0, -1):
        print (str(i) + '*' + str(j) + '=' + str(i*j), end='')
    print('')


for i in range(1, 10, 1):
    for j in range(i, 10, 1):
        print (str(i) + '*' + str(j) + '=' + str(i * j), end=' ')
    print('')
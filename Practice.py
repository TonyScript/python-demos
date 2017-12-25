#/usr/local/bin/python3
# -*- coding: utf-8 -*-

"""一个数如果恰好等于它的因子之和，这个数就称为”完数”。
例如6=1＋2＋3.编程找出1000以内的所有完数。
"""
from sys import stdout

for j in range(2, 1000):
    k = []
    n = -1
    s = j
    for i in range(1, j):
        if j % i == 0:
            n += 1
            s -= i
            k.append(i)
    if s == 0:
        print(j)
        for i in range(n):
            stdout.write(str(k[i]))
            stdout.write(' ')
        print(k[n])

"""猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，
还不过瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又
多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。到
第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
"""
FINAL_COUNT = 1
for day in range(9, 0, -1):
    Initinal_Count = (FINAL_COUNT + 1) * 2
    FINAL_COUNT = Initinal_Count
print(Initinal_Count)

"""从键盘接收一个5位数，判断它是不是回文数。
即12321是回文数，个位与万位相同，十位与千位相同。
"""
a = input()
x = str(a)
flag = True

for i in range(len(x) / 2):
    if x[i] != x[-i - 1]:
        flag = False
        break
if flag:
    print("{} 是一个回文数".format(a))
else:
    print("{} 不是一个回文数".format(a))

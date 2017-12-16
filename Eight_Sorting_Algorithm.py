#/usr/local/bin/python3
# -*- coding: utf-8 -*-

arglist = [1, 1, 2, 5, 3, 90, 555, 123]

"""1.插入排序
    基本操作就是将一个数据插入到已经排好序的有序数据中，
    从而得到一个新的、个数加一的有序数据，算法适用于少量数据的排序，
    时间复杂度为O(n^2)。是稳定的排序方法。
    插入算法把要排序的数组分成两部分：第一部分包含了这个数组的所有元素，
    但将最后一个元素除外（让数组多一个空间才有插入的位置），而第二部分
    就只包含这一个元素（即待插入元素）。在第一部分排序完成后，
    再将这个最后元素插入到已排好序的第一部分中。
"""
def insert_sorting(lists):
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
            j -= 1
    return lists

"""2.希尔排序
希尔排序(Shell Sort)是插入排序的一种。也称缩小增量排序，
是直接插入排序算法的一种更高效的改进版本。希尔排序是非稳定排序算法。
该方法因DL．Shell于1959年提出而得名。 希尔排序是把记录按下标的一
定增量分组，对每组使用直接插入排序算法排序；随着增量逐渐减少，每组
包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止。
"""
def shell_sorting(lists):
    count = len(lists)
    step = 2
    group = count / step
    while group > 0:
        for i in range(0, group):
            j = i + group
            while j < count:
                k = j - group
                key = lists[j]
                while k >= 0:
                    if lists[k] > key:
                        lists[k + group] = lists[k]
                        lists[k] = key
                    k -= group
                j += group
        group /= step
    return lists

shell_sorting(arglist)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

arglist = [1,1,2,5,3,90,555,123]

# 1. 插入排序
def insert_sorting(lists):
	count = len(lists)
	for i in range(1, count):
		key = lists[i]
		j = i - 1
		while j>= 0:
			if lists[j] > key:
				lists[j+1] >lists[j]
				lists[j] = key
			j -= 1
	return lists

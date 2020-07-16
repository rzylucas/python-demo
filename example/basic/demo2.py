#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
# 题目二：
# 查找列表中元素，移除每个元素的空格，并查找以 a或A开头 并且以 c 结尾的所有元素。
"""


li = ["alec", " aric", "Alex", "Tony", "rain"]
tu = ("alec", " aric", "Alex", "Tony", "rain")
dic = {'k1': "alex", 'k2': ' aric', "k3": "Alex", "k4": "Tony"}

tump = []
temp_tu = list(tu)
for i in range(0, len(li)):
    # 去除元素空格
    li[i] = li[i].strip()
    # 以a或A开头,且以c结尾的所有元素
    if li[i].endswith('c') and li[i].capitalize().startswith('A'):
        tump.append(li[i])

for i in range(0, len(temp_tu)):
    # 以a或A开头,且以c结尾的所有元素
    temp_tu[i] = temp_tu[i].strip()
    if temp_tu[i].endswith('c') and temp_tu[i].capitalize().startswith('A'):
        tump.append(temp_tu[i])

for item in dic.keys():
    # 去除元素空格
    dic[item] = dic[item].strip()
    # 以a或A开头,且以c结尾的所有元素
    if dic[item].endswith('c') and dic[item].capitalize().startswith('A'):
        tump.append(dic[item])

for i in range(0, len(tump)):
    tump[i].strip()

tu = tuple(temp_tu)
print("移除每个元素的空格:")
print("list:",li)
print("tuple:",tu)
print("dict:",dic)
print("以a或A开头,且以c结尾的所有元素:")
for i in tump:
    print(i)


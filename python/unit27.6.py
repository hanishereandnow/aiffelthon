# 27.6 심사문제: 특정 문자가 들어있는 단어 찾기

import string

with open('words.txt', 'r') as file:
    s = file.read()
    s = s.split()
    list =[]
    for i in range(len(s)):
        if 'c' in s[i]:
            list.append(s[i])
    for i in list:
        i = i.strip(',.')
        print(i)
# 25.8 심사문제: 딕셔너리에서 특정 값 삭제하기

keys = input().split()
values = map(int, input().split())

x = dict(zip(keys, values))
x = {key: value for key, value in x.items() if key != 'delta'}
x = {key: value for key, value in x.items() if value != 30}

print(x)
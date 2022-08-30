# 24.6 심사문제: 높은 가격순으로 출력하기

price = list(map(int, input().split(';')))
price.sort(reverse=True)    # 오름차순으로 정렬

for i in range(len(price)):
    print('{0:>9,}'.format(price[i]))
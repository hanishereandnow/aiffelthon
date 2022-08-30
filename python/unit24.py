# 코딩도장 24.5
# 표준 입력으로 문자열이 입력됩니다. 입력된 문자열에서 'the'의 개수를 출력하는 프로그램을 만드세요
# (input에서 안내 문자열은 출력하지 않아야 합니다).
# 단, 모든 문자가 소문자인 'the'만 찾으면 되며 'them', 'there', 'their' 등은 포함하지 않아야 합니다.

'''input 값: the grown-ups' response, this time, was to advise me to lay aside my drawings of boa constrictors,
whether from the inside or the outside, and devote myself instead to geography, history, arithmetic, and grammar.
That is why, at the, age of six, I gave up what might have been a magnificent career as a painter.
I had been disheartened by the failure of my Drawing Number One and my Drawing Number Two.
Grown-ups never understand anything by themselves, and it is tiresome for children to be always and forever explaining things to the.'''

text = input().split()

count = 0
for i in text:
    if i.strip(',.') == 'the':
        count += 1
print(count)
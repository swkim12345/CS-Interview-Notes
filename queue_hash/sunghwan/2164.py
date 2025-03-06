'''
카드 2
push, pop만 이용해 푸는 문제
단순히 deque를 이용하자.
'''

from collections import deque

N = int(input())
# 리스트 생성하기 -> 컴프리헨션
arr = [i for i in range(1, N + 1)]

deq = deque(arr)

while len(deq) != 1:
    # 1. pop
    deq.popleft()
    # 2. pop한 것을 다시 push
    tmp = deq.popleft()
    deq.append(tmp)

print(deq.pop())
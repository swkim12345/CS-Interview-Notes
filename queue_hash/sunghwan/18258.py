'''
큐 2
deque를 이용한 방법, queue를 이용하는 방법, 리스트가 있다.
리스트는 역시 리턴으로 인한 오버헤드가 켜서 deque로 바꾸었다.
각각의 명령은 함수로 분리해 쉽게 사용할 수 있게 하자.
시간초과가 sys 라이브러리를 안써서.. input에서 시간 초과가 나서 바꾸어주었다.
'''

import sys
from collections import deque

def push(queue, X):
    queue.append(X)

def pop(queue):
    if len(queue):
        print(queue.popleft())
    else:
        print(-1)

def size(queue):
    print(len(queue))

def empty(queue):
    if len(queue):
        print(0)
    else :
        print(1)

def front(queue):
    if len(queue):
        print(queue[0])
    else:
        print(-1)

def back(queue):
    if len(queue):
        print(queue[-1])
    else:
        print(-1)

N = int(input())
queue = deque()

dictionary = {"push" : push, "pop" : pop, "size" : size, "empty" : empty, "front" : front, "back": back}

for _ in range(N):
    tmp = sys.stdin.readline().split()
    func = dictionary.get(tmp[0])
    # 좀 더 우아하게 구조분해 할당을 할 수 있을까..
    if len(tmp) == 2:
        func(queue, tmp[-1])
    else:
        func(queue)
        

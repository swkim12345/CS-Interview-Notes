'''
싸이버개강총회

학회원 - 시간으로 딕셔너리를 만들어서 찾아야 함.
'''

import sys

def time(t):
    return t.split(":")

S, E, Q = input().split()
S = time(S)
E = time(E)
Q = time(Q)

chatting = dict()
answer = 0

while True:
    line = sys.stdin.readline()
    if not line:
        break
    t, nickname = line.split()
    t = time(t)
    if t[0] < S[0] or (t[0] == S[0] and t[1] <= S[1]):
        chatting[nickname] = t[0]
    elif (t[0] > E[0] or (t[0] == E[0] and t[1] >= E[1])) and (t[0] < Q[0] or (t[0] == Q[0] and t[1] <= Q[1])):
        if chatting.get(nickname):
            answer += 1
            chatting.pop(nickname)

print(answer)

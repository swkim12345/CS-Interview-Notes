'''
걸그룹 마스터 준석이

양방향 해시같은 게 없으니깐 딕셔너리로 구현하자. 1:N(걸그룹 - 사람), 1:1(사람 - 걸그룹)
1:N의 경우 사전순으로 정렬되어야 하니깐 삽입 전 sort 하고 삽입 필수
'''

import sys

def inp():
    return input()

# map으로 반환된 iterator로 구조분해할당
N, M = map(int, inp().split())

group_to_member = dict()
member_to_group = dict()

for _ in range(N):
    group = inp()
    size = int(inp())

    member = []
    for __ in range(size):
        member.append(inp())
    
    member.sort()
    group_to_member[group] = member
    for m in member:
        member_to_group[m] = group    

for _ in range(M):
    question = inp()
    type = int(inp())
    if type == 1:
        print(member_to_group.get(question))
    else:
        member = group_to_member.get(question)
        for m in member:
            print(m)
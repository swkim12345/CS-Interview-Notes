'''
제로
돈을 잘못 부른다 -> 직전 지우기 -> 스택
'''

K = int(input())
stack = []
for i in range(K):
    tmp = int(input())
    if tmp == 0:
        stack.pop()
    else:
        stack.append(tmp)
print(sum(stack))
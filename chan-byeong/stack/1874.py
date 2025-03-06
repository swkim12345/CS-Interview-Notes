from collections import deque

n = int(input())

stack = []
ans = []
q = deque()

for i in range(1, n+1):
  q.append(i)

for _ in range(n):
  k = int(input())
  if not stack or stack[-1] < k:
    while q[0] != k:
      stack.append(q.popleft())
      ans.append('+')
    ans.append('+')
    ans.append('-')
    q.popleft()
  elif stack[-1] == k:
    ans.append('-')
    stack.pop()
  # else:
  #   break

if not stack:
  for i in ans:
    print(i)
else:
  print('NO')
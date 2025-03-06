n = int(input())

stack = []
ans = 0
arr = []

for _ in range(n):
  h = int(input())
  arr.append(h)

for h in reversed(arr):
  v = 0
  while stack and stack[-1][0] < h:
    v += stack.pop()[1] + 1
  ans += v
  stack.append((h, v))
print(ans)
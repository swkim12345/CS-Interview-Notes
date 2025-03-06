n = int(input())

arr = input().split()
arr = list(map(int, arr))

ans = [0]*n
stack = []

for i, h in enumerate(reversed(arr)):
  while stack and stack[-1][1] < h:
    ans[stack.pop()[0]] = n-i
  stack.append((n-i-1, h))

print(" ".join(map(str, ans)))


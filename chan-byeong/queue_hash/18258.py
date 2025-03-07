import sys
from collections import deque

input = sys.stdin.readline

n = int(input().rstrip())

queue = deque()

for _ in range(n):
  val = input().rstrip()
  vals = val.split(" ")

  match vals[0]:
    case "push": queue.append(int(vals[1]))
    case "pop" : print(queue.popleft() if queue else -1)
    case "size": print(len(queue))
    case "empty": print(0 if queue else 1)
    case "front": print(queue[0] if queue else -1)
    case "back": print(queue[-1] if queue else -1)


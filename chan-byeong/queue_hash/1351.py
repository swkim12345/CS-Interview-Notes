# 무한 수열
# An = Ai/p + Ai/q 재귀적으로 풀 수 있겠다라고 생각

# 순수하게 재귀로 풀었을 경우 시간 초과 발생
# 이를 해결하기 위해 Ai값을 저장하여 재활용하기로

import math

def solution():
  n, p, q = map(int, input().split(" "))

  check = {}

  check[0] = 1
  check[1] = 2

  def recur(n,p,q):
    if n in check: return check[n]
    check[n] = recur(math.floor(n/p),p,q) + recur(math.floor(n/q),p,q)
    return check[n]
  
  print(recur(n,p,q))

solution()
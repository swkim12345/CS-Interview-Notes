# 입력의 개수가 정해지지 않아서 어떻게 해야할지 고민이 된다.
# -> 스트리밍 종료 시간 이후의 채팅이 들어오면 while 문을 종료한다.
# -> 하지만 스트리밍 종료 시간 이후의 채팅이 들어오지 않으면 문제가 발생한다.

# -> 모든 채팅 입력을 한번에 받아서 처리한다.
# -> 그냥 무한 입력 받으면 됐음.

# 입력 개수 10**5
# 시간 복잡도 O(n)으로 해결해야 한다.

import sys
def solution():
  def time_compare(time1, time2, flag = True):
    time1 = list(map(int,time1.split(":")))
    time2 = list(map(int,time2.split(":")))

    if time1[0] < time2[0]: return True if flag else False
    elif time1[0] == time2[0]:
      if time1[1] < time2[1]: return True if flag else False
      elif time1[1] == time2[1]: return True
      else: return False if flag else True
    else: return False if flag else True
  
  st, ed, stream_ed = input().split(" ")

  check = {}
  ans = 0

  # chat_logs = [sys.stdin.readline().strip() for _ in range(100000)]
  

  # while(True):
  #   chat_log = sys.stdin.readline().strip()
  #   if not chat_log: break
  #   chat_logs.append(chat_log)

  # print(chat_logs)

  for chat_log in sys.stdin:
    time, nickname = chat_log.strip().split(" ")
    
    if time_compare(time, st): 
      check[nickname] = 1
      continue

    if time_compare(time, ed, False) and time_compare(time, stream_ed):
      if nickname in check and check[nickname] == 1: 
        ans += 1
        check[nickname] = 0

    if time_compare(time, stream_ed, False): break

  print(ans)


solution()
# 옥상 정원 꾸미기
# 2493번과 비슷하지만 다름. 역방향은 동일함, 번수가 아닌 몇 개를 볼 수 있는 지
# nlogn에 풀어야 함.
# 1. 그냥 다 확인하는 법 -> N**2
# 2. 하나마다 정렬 후 탐색 -> n * nlogn * logn(이분탐색)
# 3. 일단 역방향
# 스택을 이용해 하나씩 삽입, 만약 스택값보다 작다면 스택 사이즈만큼 가져옴.
# 아니면 (앞 > 스택) -> pop, (앞 <= 스택) 까지 가져옴. 다 가져오면 다시 push
# tuple로 (idx, value)


# N = int(input())
# arr = []
# for _ in range(N):
#     arr.append(int(input()))
# answer = 0
# stack = []

# for i in range(N - 1, -1, -1):
#     sec_stack = []
#     while True:
#         # 앞 > 뒤 -> pop
#         if len(stack) != 0 and arr[i] > stack[-1][1]:
#             answer += 1
#             sec_stack.append(stack.pop())
#         else:
#             break
#     for j in reversed(sec_stack):
#         stack.append(j)
#     stack.append((i, arr[i]))

# print(answer)

# 결국 풀이 봄.
'''
결론적으론 스택을 이용해 내림차순으로 스택 내부를 채우고, len - 1만큼 answer에 더해주는 방식이더라.
'''
N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
answer = 0
stack = []

for i in range(N):
    while True:
        # 만약 스택(앞) > arr(뒤) -> 볼 수 있음 -> 스택에 삽입
        if len(stack) == 0 or stack[-1] > arr[i]:
            stack.append(arr[i])
            break
        # 스택(앞) <= arr(뒤) -> 볼 수 없음 -> 볼 수 있을 때 까지 pop
        else:
            stack.pop()
    answer += len(stack) - 1

print(answer)


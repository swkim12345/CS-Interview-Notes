# 500,000이므로 nlogn까지 가능한 문제
# 어느 탑에서 수신? - 쿼리?
# 단순히 왼쪽으로 가면서 확인-> 시간이 너무 오래 걸림. n**2
# 스택 하나를 탑(arr)를 왼쪽으로 가며 확인해가며 top과 비교, top과 비교했을 때 작으면 인덱스 저장, 아니면 stack에 push
# 스택은 뒤의 값이 들어가게 됨, 앞의 값과 비교해서 pop을 한 다음 index를 삽입하면 끝.

stack = []
N = int(input())
answer = [0] * N

arr = list(map(int, input().split()))

for i in range(N - 1, -1, -1):
    while True:
        # 뒤에서부터 체크,만약 크다면 -> 앞 < 뒤, 답 아님, 그냥 stack에 추가
        if len(stack) == 0 or stack[-1][1] > arr[i]:
            tup = (i, arr[i])
            stack.append(tup)
            break
        # 만약 스택(뒤의 값)보다 arr값(앞의 값)이 작다면 -> 앞 >= 뒤, 답임. -> answer에 추가.
        else:
            # 체크한 인덱스 + 1값이 답이 됨.
            answer[stack[-1][0]] = i + 1
            stack.pop()

for i in answer:
    print(i, end=" ")
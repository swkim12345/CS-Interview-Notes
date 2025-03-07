# 답이 하나만 나오는 문제 -> pop을 하면 수열로 고정됨.
# answer와 비교해 숫자가 크면 pop, 작게 되면 만들 수 없게 됨 -> NO 출력

if __name__ == '__main__':
    stack = []
    arr = []
    answer = []
    n = int(input())
    for i in range(n) :
        arr.append(int(input()))
        
    arr_idx = 0
    for i in range(1, n + 1):
        # 만약 안에 없으면 push
        if len(stack) == 0:
            stack.append(i)
            answer.append("+")
        # 있으면 answer와 비교하면서 while
        else:
            while True:
                # 만약 i가 더 작으면? -> 뒤에 값이 있으므로 push
                if i <= arr[arr_idx]:
                    stack.append(i)
                    answer.append("+")
                    break
                # 만약 i가 더 크거나 같으면? -> pop 후 숫자와 비교, 적절한 숫자가 아니면 NO
                cmp = stack.pop()
                if cmp == arr[arr_idx]:
                    answer.append("-")
                    arr_idx += 1
                else:
                    print("NO")
                    exit()
    while len(stack):
        # 만약 i가 더 크거나 같으면? -> pop 후 숫자와 비교, 적절한 숫자가 아니면 NO
        cmp = stack.pop()
        if cmp == arr[arr_idx]:
            answer.append("-")
            arr_idx += 1
        else:
            print("NO")
            exit()

    for i in answer:
        print(i)
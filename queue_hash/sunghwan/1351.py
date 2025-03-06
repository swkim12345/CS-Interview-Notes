'''
무한 수열
..이게 왜 해시가 필요하지?
단순한 dp 문제로 보임. 10**12는 그냥 dp로 풀면 아마 터질 가능성이 높아 보임.
공간 복잡도상 단순한 배열, dp로는 못 품
따라서, dictionary를 통해 주어진 값에서 역으로 푸는 방법이 좋을 거 같음
Ai는 두개로 분해가 되고, 이는 dictionary에 필요한 값을 추가할 수 있다.
두개의 dictionary로 풀자.
하나는 idx - 가격, 하나는 before idx - next idx
두번째 dictionary로 값을 분해하고, keys만 가져와서 정렬한 다음 정렬한 순서대로 첫번째 dictionary에 삽입해 문제를 해결하자.
'''

N, P, Q = map(int, input().split())
idx_value = dict()

def dp(idx):
    if (idx == 0):
        return 1
    if idx_value.get(idx):
        return idx_value.get(idx)
    idx_P = dp(idx // P)
    idx_value[idx // P] = idx_P
    idx_Q = dp(idx // Q)
    idx_value[idx // Q] = idx_Q
    return idx_P + idx_Q

print(dp(N))

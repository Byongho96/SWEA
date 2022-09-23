import sys
sys.stdin = open('input.txt', 'r', encoding='UTF-8')

d1 = [-1, 1, 1, -1]
d2 = [1, 1, -1., -1]

def check():
    pass

def brute_force(i, j, n, dessert):
    global result

    if n == 4:
        result = max(result, dessert)
        return

    if n == 0 or n == 1:
        di, dj = d1[n], d2[n]
        for dist in range(1, N):
            ni = int(i + di * dist)
            nj = int(i + dj * dist)
            if 0 <= ni < N and 0 <= nj < N:
                if not eaten[arr[ni][nj]]:
                    eaten[arr[ni][nj]] = 1
                    pre_dist[n] = dist
                    brute_force(ni, nj, n + 1, dessert+dist)
                else:
                    return
            else:
                return
    if n == 2 or n == 3:
        di, dj = d1[n], d2[n]
        record_dist = pre_dist[n-2]
        ni, nj = i, j
        for dist in range(1, record_dist + 1):
            ni = int(i + di * dist)
            nj = int(i + dj * dist)
            if not (0 <= ni < N and 0 <= nj < N):
                break
            if eaten[arr[ni][nj]]:
                break
        else:
            brute_force(ni, nj, n + 1, dessert + record_dist)
            return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    pre_dist = [0, 0]
    for i in range(1, N):
        for j in range(N-1):
            eaten = [0] * 101
            brute_force(i, j, 0, 0)

    print(f'#{tc} { result}')
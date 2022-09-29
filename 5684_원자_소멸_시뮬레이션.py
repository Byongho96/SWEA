import sys
sys.stdin = open('input.txt', 'r', encoding='UTF-8')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    for _ in range(N):
        j, i, d, e = map(int, input().split())

    print(f'#{tc} {energy}')
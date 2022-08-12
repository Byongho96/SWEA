for t in range(1, 11):
    T = int(input())
    ldr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)] # 0으로 좌우 감싼 2차원 배열 100*102
    shortst = 100*100   # 최단경로 비교
    start = 0   # 시작 x좌표 저장

    for j in range(1, 101): # 1~100번 탐색
        i = 99
        dis = 0

        if ldr[i][j] == 0: # 1인 지점만 찾아서 반복문 진행
            continue

        for _ in range(99): # 99번 올라가면 출바지점 도착
            if not (ldr[i][j-1] or ldr[i][j+1]): # 양쪽이 모두 막혔을 경우
                i -= 1 # 위로
            elif ldr[i][j-1]:   # 왼쪽이 뚫렸을 경우
                while ldr[i][j-1]:  # 갈 수 있을 때까지 이동
                    dis += 1
                    j -= 1
                i -= 1  # 왼쪽으로 더 이상 못가면, 위로 이동
            else:   # 오른쪽이 뚫렸을 경우
                while ldr[i][j+1]:  # 갈 수 있을 때까지 이동
                    dis += 1
                    j += 1
                i -= 1  # 오른족으로 더 이상 못가면, 위로 이동
            dis += 1    # 위로 올라갈 때마다 카운트(어차피 모두 99번 올라가서 없어도 됨)

        if dis <= shortst:  # 이동 거리가 가장 짧을 때마다, 관려변수 업데이트
            shortst = dis
            start = j-1

    print(f'#{t} {start}')
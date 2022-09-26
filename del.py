def solution(N):
    def d_sum(number, len_num):
        nm = str(number)
        # s_sum = number
        for i in range(len_num):
            number += int(nm[i])
        return number


    # N = input()
    ans = 0
    min = 999999
    e = int(N)
    l = len(N)
    s = e - (9*l)
    if s < 1:
        s = 1

    # 수의 범위에 대한 분해합 검정
    for num in range(s, e):
        s_um = d_sum(num, len(str(num)))
        if s_um == e and num <= min:
            min = num

    if min != 999999:
        ans = min
    print(ans)

for idx in range(1, 1000001):
    solution(str(idx))
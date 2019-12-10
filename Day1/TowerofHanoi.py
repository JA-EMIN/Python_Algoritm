# 하노이 탑
# 1(처음)     2(중간)      3(끝)
# 1(처음) 기둥에 꽂혀있는 n개의 원반을 3(끝)으로 옮기는 문제
# 한번에 한개만 움직일 수 있고, 큰 원반을 작은 원반 위에 얹을 수 없다.
# 알고리즘
#   1(처음)에서 n개의 원반을 2(중간)를 이용하여 3(끝)으로 옮기는 알고리즘  Hanoi(n, start, by, dest)
# 1. 1(처음)에서 n-1개의 원반을 3(끝)을 이용하여 2(중간)으로 옮긴다.      Hanoi(n-1, start, dest, by)
# 2. 1(처음)에서 1개의 원반을 3(끝)으로 옮긴다.
# 3. 2(중간)에서 n-1개의 원반을 1(처음)을 이용하여 3(끝)으로 옮긴다.      Hanoi(n-1, by, start, dest)

def move(start, dest):
    print('시작: ', start,'에서 ', '목적지:', dest, '로 이동')

def Hanoi(n, start, by, dest):  # n: 원반갯수, start : 시작기둥, by : 이동에 이용될 기둥, dest : 목적기둥
    if n == 1:
        move(start, dest)       # 실제로 이동
        return
    else:
        Hanoi(n-1, start, dest, by)                 # n-1개의 원반이 1(start)에서 2(by)로 3(dest)기둥을 이용하여 이동해야한다.
        move(start, dest)                           # 1(start)에서 1개의 원반을 3(dest)로 옮긴다.
        Hanoi(n-1, by, start, dest)                 # 현재 2번기둥에 n-1개의 원반이 위치해 있다
                                                    # 이제 n-1개의 원반이 2(by)에서 3(dest)로 2(start)기둥을 이용하여 이동해야한다.


Hanoi(5, 1, 2, 3)

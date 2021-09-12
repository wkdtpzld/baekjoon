n = 0  # 숫자 1, 2, 3, ...
step = 1  # 증가/감소 크기: 1, -1
y = 0  # 줄 위치
x = -1  # 칸 위치 (배열 선두보다 한칸 앞)
size = 5  # 배열 크기 (5*5 배열)
arr = [[0] * size for i in range(size)]  # 2차원 배열 구조

while True:
    for _ in range(size):  # 몇 칸 진행할까
        n += 1
        x += step
        arr[y][x] = n
    size -= 1
    if size < 1:  # 출력할 게 없으면 종료
        break
    for _ in range(size):  # 몇 줄 진행할까
        n += 1
        y += step
        arr[y][x] = n
    step = -step  # 증감 방향을 반대로

# 2차원 리스트 출력하기
for line in arr:
    for n in line:
        print('%3d' % n, end='')
    print()
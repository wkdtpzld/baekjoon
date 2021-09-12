num=int(input())
n=1
n_sum=0

while True:
    n_sum += n
    if n_sum >= num:
        break
    else:
        n += 1
n_result = n_sum - num
son=1
if n % 2 != 0:
    print(f'{son+n_result}/{n - n_result}')
else:
    print(f'{n - n_result}/{son+n_result}')
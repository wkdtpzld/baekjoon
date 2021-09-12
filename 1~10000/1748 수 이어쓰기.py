n=int(input())
n_len=len(str(n))
cnt=0

for i in range(n_len-1):
    cnt += 9 * 10 ** i * (i + 1)
print(cnt + (n - 10**(n_len-1)+1)*n_len)
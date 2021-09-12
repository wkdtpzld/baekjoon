month,d,y,t=input().split()
d=int(d[:-1])
y=int(y)
h,m=map(int,t.split(':'))
month_li=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
day_li=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if y % 400 == 0 or (y % 100 != 0 and y % 4 == 0):
    day_li[1] += 1
total_time=sum(day_li)*24*60

month_sum=month_li.index(month)
result=(sum(day_li[:month_sum])+d-1)*24*60 + h*60 +m
result_true=result/total_time
print(result_true*100)
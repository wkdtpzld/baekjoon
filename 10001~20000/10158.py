w,h=map(int,input().split())
x,y=map(int,input().split())
time=int(input())
cnt=0
if ((x+time)%w) != 0 and ((x+time)//w)%2 != 0:
    x= w-(x+time)%w
elif ((x+time)%w) != 0 and ((x+time)//w)%2 == 0:
    x= (x+time)%w
elif ((x+time)%w) == 0 and ((x+time)//w)%2 != 0:
    x = w
elif ((x+time)%w) ==0 and ((x+time)//w)%2 == 0:
    x= 0
if ((y+time)%h) != 0 and ((y+time)//h)%2 != 0:
    y = h-(y+time)%h
elif ((y+time)%h) != 0 and ((y+time)//h)%2 == 0:
    y= (y+time)%h
elif ((y+time)%h) == 0 and ((y+time)//h)%2 != 0:
    y = h
elif ((y+time)%h) == 0 and ((y+time)//h)%2 == 0:
    y = 0
print(x,y)
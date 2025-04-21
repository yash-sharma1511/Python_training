def time_increment(h:int,m:int)->tuple[int,int]:
    m+=1
    if m==60:
        m=0
        h=(h+1)%24
    return h,m
print(time_increment(23,59))
print(time_increment(13,29))
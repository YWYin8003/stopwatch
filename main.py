from time import sleep

second=0
minute=0
hour=0
day=0
year=0
i=0

while True:
    print ((str(year))+"year"+":"+(str(day).zfill(3))+"day"+":"+(str(hour).zfill(2))+"hour"+":"+(str(minute).zfill(2))+"minute"+":"+(str(second).zfill(2))+"second")
    if second>=59:
        second=-1
        e=minute+1
        minute=e
    if minute>=60:
        minute=0
        e=hour+1
        hour=e
    if hour>=24:
        hour=0
        e=day+1
        day=e
    
    if i<=3:

        if day>=365:
            day=0
            e=year+1
            year=e
            u=i+1
            i=u

    if i>=4:

        if day>=366:
            day=0
            e=year+1
            year=e
            i=1


    
        

    e=second+1
    second=e
    sleep (1)
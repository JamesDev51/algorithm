import math
def combine(n, stations, w):
    online=[]
    i=0
    while i<len(stations):
        station=stations[i]
        l,r=max(1,station-w),min(n,station+w)
        while i+1<len(stations) and stations[i+1]-w<=r:
            r=min(n,stations[i+1]+w)
            i+=1
        online.append((l,r))
        i+=1
    return online

def get_offline(n,online):
    offline=[]
    lt=1
    for on_l,on_r in online:
        if lt<on_l:offline.append((lt,on_l-1))
        lt=on_r+1
    if lt<=n:offline.append((lt,n))
    return offline
            
def solution(n, stations, w):
    answer = 0
    online=combine(n, stations, w)
    size=2*w+1
    lt=1
    offline=get_offline(n,online)
    for off_l,off_r in offline:
        offline_size=off_r-off_l+1
        if offline_size<size:answer+=1
        else:answer+=math.ceil(offline_size/size)
    
    
    return answer
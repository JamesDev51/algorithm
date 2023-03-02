import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

name_set=set()
place_idx=dict()
idx_place=dict()

place_time=[[0]*50002 for _ in range(10)]
idx=0
if __name__=="__main__":
    n=int(input())
    for _ in range(n):
        name,place,s,e=input().split()
        if name not in name_set:name_set.add(name)
        else:continue
        if place not in place_idx:
            place_idx[place]=idx;
            idx_place[idx]=place
            idx+=1
        for t in range(int(s),int(e)):
            place_time[place_idx[place]][t]+=1

    crowd=list()
    most_crowd=float('-inf')
    for i in range(idx):
        name=idx_place[i]
        lt,rt=1,1
        now=place_time[i][lt]
        while lt<=rt and rt<=50000:
            while rt<=50000 and now==place_time[i][rt]:rt+=1
            if now==most_crowd:
                crowd.append((name,lt,rt))
            elif now>most_crowd:
                crowd.clear()
                crowd.append((name,lt,rt))
                most_crowd=now
            lt=rt
            now=place_time[i][lt]
    crowd.sort(key=lambda x:(x[0],x[1]))
    print(*crowd[0])
        
        
            
        
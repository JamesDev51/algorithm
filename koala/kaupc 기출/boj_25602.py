import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def find(day,total_satisfaction):
    if day==k: return total_satisfaction

    ret=0
    for i in range(n):
        if a[i]==0:continue #선택 불가능한 상태
        a[i]-=1
        for j in range(n):
            if a[j]==0:continue #선택 불가능한 상태
            a[j]-=1
            today_satisfaction=r[day][i]+m[day][j]
            ret=max(ret,find(day+1,total_satisfaction+today_satisfaction))
            a[j]+=1
        a[i]+=1
    return ret
        

if __name__=="__main__":
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    r=[list(map(int,input().split())) for _ in range(k)]
    m=[list(map(int,input().split())) for _ in range(k)]
    print(find(0,0))
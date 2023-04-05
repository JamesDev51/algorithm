import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    acc=[0];h=dict();h[0]=1
    for num in arr:acc.append(acc[-1]+num)
    res=0
    for num in acc[1:]: 
        gap=num-k
        if gap in h:res+=h[gap]
        if num in h:h[num]+=1
        else:h[num]=1
    print(res)
    
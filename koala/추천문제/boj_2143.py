import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    t=int(input())
    n=int(input())
    a=list(map(int,input().split()))
    for i in range(1,n):a[i]+=a[i-1]
    m=int(input())
    b=list(map(int,input().split()))
    for i in range(1,m):b[i]+=b[i-1]
    a_hash=dict(); b_hash=dict()
    
    for  i in range(n):
        num=a[i]
        if num in a_hash:a_hash[num]+=1
        else:a_hash[num]=1
        for j in range(i):
            gap=a[i]-a[j]
            if gap in a_hash:a_hash[gap]+=1
            else:a_hash[gap]=1
            
    for  i in range(m):
        num=b[i]
        if num in b_hash:b_hash[num]+=1
        else:b_hash[num]=1
        for j in range(i):
            gap=b[i]-b[j]
            if gap in b_hash:b_hash[gap]+=1
            else:b_hash[gap]=1
    cnt=0
    for key,value in a_hash.items():
        b_key=t-key
        if  b_key in b_hash:cnt+=value*b_hash[b_key]
    print(cnt)
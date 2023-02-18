import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

if __name__=="__main__":
    while True:
        n,A,B=map(int,input().split())
        if not n and not A and not B:break
        arr=[]
        for _ in range(n):
            k,a,b=map(int,input().split())
            arr.append((abs(a-b),a,b,k))
        arr.sort(key=lambda x:(-x[0]))
        res=0
        for _,a,b,k in arr:
            if a<b:
                if k<=A:
                    res+=k*a
                    A-=k
                else:
                    res+=A*a
                    k-=A
                    A=0
                    res+=k*b
                    B-=k
            else:
                if k<=B:
                    res+=k*b
                    B-=k
                else:
                    res+=B*b
                    k-=B
                    B=0
                    res+=k*a
                    A-=k
        print(res)                

import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        arr=list(map(int,input().split()))
        full=0
        extra=0
        half=0
        for div in arr:
            if div==1: #구매
                if extra>0:extra-=1
                half+=1
            else: #의사
                org_half=half
                male,female=1,half-1
                moved_full=(male//2+female//2)
                full+=moved_full
                half=(male%2+female%2)
                extra+=(org_half-half-moved_full)
        print(full+half+extra)
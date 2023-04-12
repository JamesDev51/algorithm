import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

from bisect import bisect

if __name__=="__main__":
    for _ in range(int(input())):
        k,n=map(int,input().split())
        ab_set=set()
        ans=[1e9,1e9,1e9]
        ab=[list(map(int,input().split())) for _ in range(2)]
        for a in ab[0]:
            for b in ab[1]:
                ab_set.add(a+b)
        ab=sorted(list(ab_set))
        cd=[list(map(int,input().split())) for _ in range(2)]
        for c in cd[0]:
            for d in cd[1]:
                cd_sum=c+d
                need=k-cd_sum
                idx=bisect(ab,need)
                if idx<len(ab):
                    ab_sum=ab[idx]
                    tmp=[abs(k-ab_sum-cd_sum),ab_sum+cd_sum-k,ab_sum+cd_sum]
                    if tmp<ans:ans=tmp
                if 0<=idx-1:
                    ab_sum=ab[idx-1]
                    tmp=[abs(k-ab_sum-cd_sum),ab_sum+cd_sum-k,ab_sum+cd_sum]
                    if tmp<ans:ans=tmp
                if idx+1<len(ab):
                    ab_sum=ab[idx+1]
                    tmp=[abs(k-ab_sum-cd_sum),ab_sum+cd_sum-k,ab_sum+cd_sum]
                    if tmp<ans:ans=tmp
        print(ans[2])
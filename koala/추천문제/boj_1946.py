import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        scores=[list(map(int,input().split())) for _ in range(n)]
        scores.sort()
        smallest=1e9
        cnt=0
        for _,score in scores:
            if smallest>score:
                smallest=score
                cnt+=1
        print(cnt)
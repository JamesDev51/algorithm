import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
from itertools import combinations

if __name__=="__main__":
    n=int(input())
    ability=[list(map(int,input().split())) for _ in range(n)]
    res=float('inf')
    for comb in combinations(list(range(n)),n//2):
        team1,team2=0,0
        for i in range(n):
            for j in range(i+1,n):
                if i==j:continue
                if i in comb and j in comb:
                    team1+=ability[i][j]
                    team1+=ability[j][i]
                elif i not in comb and j not in comb:
                    team2+=ability[i][j]
                    team2+=ability[j][i]
                else:continue
        res=min(res,abs(team1-team2))
    print(res)
                    
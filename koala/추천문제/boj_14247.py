import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    n=int(input())
    h=list(map(int,input().split()))
    a=list(map(int,input().split()))
    trees=[]
    for i in range(n):
        trees.append((h[i],a[i]))
    trees.sort(key=lambda x:(x[1]))
    res=0
    for day in range(n):
        res+=(trees[day][0]+trees[day][1]*day)
    print(res)
import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

n, m = map(int, input().split())    # 잎 개수, day
a, b, c = map(int, input().split()) #독 한계, 해독, 현재 독
arr = []    #독, 행복도
for _ in range(n):
    arr.append(list(map(int, input().split())))

happy = 0

def dfs(day, h, poison, idx):
    global happy
    
    if poison > a: return
    if day != 0:
        # 최대 행복도 갱신
        happy = max(happy, h)
        
        # 첫날 아니면 해독
        poison -= b
        if poison < 0: poison = 0
        
    if day == m - 1: return
    
    for i in range(idx, n): 
        # 현재 독 + 먹을 잎의 독소가 한계보다 작다면
        if poison + arr[i][0] <= a:
            dfs(day + 1, h + arr[i][1], poison + arr[i][0], idx + 1)
    

dfs(0, 0, c, 0)
print(happy)
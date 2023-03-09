import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
sys.setrecursionlimit(100000000000)

# def backtracking(l,first,second):
#     global smallest_gap
#     if l==n:
#         smallest_gap=min(smallest_gap,abs(first-second))
#         return
#     a,b=prices[l]
#     backtracking(l+1, max(first,a), second)
#     backtracking(l+1, first, max(second,b))
    
# if __name__=="__main__":
#     for i in range(int(input())):
#         n=int(input())
#         prices=[list(map(int,input().split())) for _ in range(n)]
#         smallest_gap=float('inf')
#         backtracking(0,0,0)
#         print(smallest_gap)

t = II()
for _ in range(t):
    n = II()
    nums1 = []
    nums2 = []
    tot = []
    for i in range(n):
        x, y = MII()
        nums1.append(x)
        nums2.append(y)
        tot.append([x, 0, i])
        tot.append([y, 1, i])
    tot.sort(key=lambda x: x[0])
    vis1, vis2 = [0] * n, [0] * n
    cnt = 0
    ans = inf
    m1, last_m1, m2, last_m2 = -inf, -inf, -inf, -inf
    f1 = f2 = 0
    pt = 0
    for v_, group_, idx_ in tot:
        while pt < n * 2 and tot[pt][0] <= v_:
            v, group, idx = tot[pt]
            if group == 0:
                if vis2[idx] == 0: cnt += 1
                vis1[idx] = 1
                f1 = 1
                if v == m1: last_m1 = m1
                elif v > m1: m1, last_m1 = v, m1
            else:
                if vis1[idx] == 0: cnt += 1
                vis2[idx] = 1
                f2 = 1
                if v == m2: last_m2 = m2
                elif v > m2: m2, last_m2 = v, m2
            pt += 1
        if cnt == n and f1 and f2:
            if group_ == 0:
                if nums2[idx_] == m2: ans = min(ans, v_ - last_m2)
                else: ans = min(ans, v_ - m2)
            else:
                if nums1[idx_] == m1: ans = min(ans, v_ - last_m1)
                else: ans = min(ans, v_ - m1)
    print(ans)
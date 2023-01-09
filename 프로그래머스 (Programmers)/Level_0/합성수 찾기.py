def solution(n):
    answer=0
    a=[0]*(n+1)
    for i in range(1,n+1):
        for j in range(i,n+1,i):
            a[j]+=1
    for i in range(1,n+1):
        if a[i]>2:answer+=1
    return answer
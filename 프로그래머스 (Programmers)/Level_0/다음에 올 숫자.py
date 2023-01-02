def solution(common):
    n=len(common)
    isDungbi=False
    for i in range(-1000,2001):
        if i==0:continue
        if all(common[j]==common[j-1]*i for j in range(1,n)):
            isDungbi=True
            return common[-1]*i
    return common[-1]+(common[-1]-common[-2])
        
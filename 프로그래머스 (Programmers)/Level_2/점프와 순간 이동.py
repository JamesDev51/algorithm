def solution(n):
    ans=0
    while n:
        if n%2==0: n//=2
        else:n-=1;ans+=1
    return ans
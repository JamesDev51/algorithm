def solution(k, ranges):
    answer = []
    coords=dict();coords[0]=k
    x=1
    while k!=1:
        if k%2==0: #짝수
            y=k//2
        else: #홀수
            y=k*3+1
        coords[x]=y
        x+=1;k=y
    n=len(coords)-1
    
    jungjukbun=[0]*(n+1)
    for x in range(1,n+1):
        jungjukbun[x]=jungjukbun[x-1]+(coords[x]+coords[x-1])/2
        
    for a,b in ranges:
        if a==b==0:answer.append(jungjukbun[-1])
        elif a<=n+b :answer.append(jungjukbun[n+b]-jungjukbun[a])
        else:answer.append(-1)
    
    return answer
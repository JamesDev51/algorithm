def solution(n):
    pyramid = []
    for i in range(1,n+1):
        row=[0]*i;pyramid.append(row)
    d=0;cnt=0;num=1
    row,col=0,0
    while n:
        pyramid[row][col]=num
        num+=1
        cnt+=1
        if cnt==n:
            d=(d+1)%3
            cnt=0
            n-=1
        if d==0:row+=1
        elif d==1:col+=1
        elif d==2:row-=1;col-=1
    answer=[]
    for row in pyramid:
        answer.extend(row)
    return answer
from math import sqrt
def find(y,x_square,d_square):
    lt,rt=0,len(y)-1
    ret=-1
    while lt<=rt:
        mid=(lt+rt)//2
        if x_square+pow(y[mid],2)<=d_square:
            ret=max(ret,mid)
            lt=mid+1
        else:
            rt=mid-1
    return ret+1

    return 0
def solution(k, d):
    answer = 0
    y=list(range(0,d+1,k))
    d_square=pow(d,2)
    for x in range(0,d+1,k):
        x_square=pow(x,2)
        answer+=find(y,x_square,d_square)
    return answer
def getNum(n):
    idx=0
    while True:
        flag=False
        if "3" in str(idx) or idx%3==0:
            idx+=1
        else:
            idx+=1
            n-=1
            flag=True
        if not n and flag:break
    return idx-1


def solution(n):
    return getNum(n)
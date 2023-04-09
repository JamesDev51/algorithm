import sys
sys.stdin=open("input.text","rt")

def test():
    for x in range(w):
        div=-1;cnt=0
        flag=False
        for y in range(d):
            if ch[y]!=-1:
                if div==ch[y]:cnt+=1
                else:div=ch[y];cnt=1
            else:
                if div==films[y][x]:cnt+=1
                else:div=films[y][x];cnt=1
            
            if cnt==k:flag=True;break
        if not flag:return False
    return True
            
def insert(level,now_cnt,tot_cnt):
    if now_cnt==tot_cnt:return test()
    if level==d:return False
    ret=False
    for div in range(-1,2):
        if div==-1:
            ret |=insert(level+1,now_cnt,tot_cnt)
        else:
            ch[level]=div; #시약 투입
            ret |= insert(level+1,now_cnt+1,tot_cnt)
            ch[level]=-1
    return ret
    

def go():
    if test():return 0
    for tot_cnt in range(1,d+1):
        if insert(0,0,tot_cnt):
            return tot_cnt
    

for t in range(1,int(input())+1):
    d,w,k=map(int,input().split())
    films=[list(map(int,input().split())) for _ in range(d)]
    ch=[-1]*d
    print(f"#{t} {go()}")
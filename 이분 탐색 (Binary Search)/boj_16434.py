import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def check(h_max):
    global h_atk
    h_atk_cur=h_atk; h_hp_cur=h_max
    for t,a,h in rooms:
        if t==1: #몬스터
            if h%h_atk_cur==0: val=h//h_atk_cur-1
            else:val=h//h_atk_cur
            if h_hp_cur-a*val<=0: return False #용사 사망 조건
            h_hp_cur-=a*val
        else: #포션
            h_atk_cur+=a
            if h_hp_cur+h>=h_max: h_hp_cur=h_max
            else: h_hp_cur+=h
    return True

def solve():
    global m_sum
    lt,rt=1,10**30 #rt를 10**15로 해서 틀렸음 범위가 생각보다 넓음
    res=float('inf')
    while lt<=rt:
        mid=(lt+rt)//2
        if check(mid):res=min(res,mid);rt=mid-1
        else: lt=mid+1
    return res
            

if __name__=="__main__":
    n,h_atk=map(int,input().split())
    m_sum=0
    rooms=list()
    for _ in range(n):
        t,a,h=map(int,input().split())
        if t==1:m_sum+=a
        rooms.append((t,a,h))
    print(solve())
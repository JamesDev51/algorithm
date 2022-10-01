import sys
sys.stdin = open("input.text",  "rt")
import sys
from collections import deque
input=sys.stdin.readline

def solve():
    limit=9999; mod=10000
    ch=[0]*(limit+1)
    ch[a]=1
    que=deque()
    que.append((a,''))
    
    while que:
        num,com=que.popleft()
        if num==b: return com
        if 0<=num*2<=limit:
            if not ch[num*2]: ch[num*2]=1; que.append((num*2,com+'D'))
        else:
            if not ch[(num*2)%mod]: ch[(num*2)%mod]=1; que.append(((num*2)%mod,com+'D'))
            
        if 0<num<=limit:
            if not ch[num-1]: ch[num-1]=1; que.append((num-1,com+'S'))
        elif num==0:
            if not ch[9999]: ch[9999]=1; que.append((9999,com+'S'))
        
        str_num=str(num)
        while len(str_num)<=3:str_num='0'+str_num
        
        l_num=int(str_num[1:]+str_num[0])
        if not ch[l_num]: ch[l_num]=1; que.append((l_num,com+'L'))
        
        r_num=int(str_num[3]+str_num[:3])
        if not ch[r_num]: ch[r_num]=1; que.append((r_num,com+'R'))
        
    
if __name__=="__main__":
    for _ in range(int(input())):
        a,b=map(int, input().split())
        print(solve())
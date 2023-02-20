import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
from collections import deque

if __name__=="__main__":
    n=int(input())
    now=list(map(int,input().split()))
    future=list(map(int,input().split()))
    gap=[future[i]-now[i] for i in range(n)]
    total_move=sum(map(abs,gap)) #앞이든 뒤든 움직여야 하는 거리
    que=deque()
    res=0
    while total_move: #작업이 끝나는 조건
        rt=0
        while rt<n and gap[rt]==0:rt+=1
        flag=True if gap[rt]>0 else False #양수 음수 플래그
        lt=rt;work=gap[rt]
        while lt<=rt and rt<=n:
            if rt==n:
                que.append((lt,rt,work))
                break
            if gap[rt]==0:
                que.append((lt,rt,work))
                while rt<n and gap[rt]==0:rt+=1
                if rt==n:break
                lt=rt;work=gap[rt]
                flag=True if gap[rt]>0 else False #양수 음수 플래그
            elif flag==True and gap[rt]<0:
                que.append((lt,rt,work))
                lt=rt;work=gap[lt];flag=False
            elif flag==False and gap[rt]>0:
                que.append((lt,rt,work))
                lt=rt;work=gap[lt];flag=True
            else:
                if flag:
                    work=min(work,gap[rt])
                else:
                    work=max(work,gap[rt])
                rt+=1
        while que:
            lt,rt,work=que.popleft()
            total_move-=((rt-lt)*abs(work))
            for idx in range(lt,rt):
                gap[idx]-=work
            res+=abs(work)
    print(res)   
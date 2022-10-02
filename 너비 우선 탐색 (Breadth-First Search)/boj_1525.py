import sys
sys.stdin = open("input.text",  "rt")
import sys
from collections import deque
from copy import deepcopy
input=sys.stdin.readline

def solution(mat):
    answer=-1
    expected="123456780"
    str_mat=''.join(''.join(mat[i][j] for j in range(3)) for i in range(3))
    que=deque()
    que.append((str_mat,0))
    ch=set()
    ch.add(str_mat)
    
    while que:
        now_str_mat,cnt=que.popleft()
        if now_str_mat==expected: answer=cnt; break
        zero_idx=now_str_mat.index('0')
        y,x=zero_idx//3, zero_idx%3
        for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
            ny,nx=y+dy,x+dx
            if 0<=ny<3 and 0<=nx<3:
                new_idx=ny*3+nx
                list_now_str_mat=list(now_str_mat)
                list_now_str_mat[zero_idx],list_now_str_mat[new_idx]=list_now_str_mat[new_idx],list_now_str_mat[zero_idx]
                new_str_mat=''.join(list_now_str_mat)
                
                if new_str_mat not in ch:
                    ch.add(new_str_mat)
                    que.append((new_str_mat,cnt+1))
            
        


    return answer

if __name__=="__main__": 
    mat=[list(input().split()) for _ in range(3)]
    print(solution(mat))
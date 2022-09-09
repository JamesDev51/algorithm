import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve():
    res=float('-inf')
    stack=[]
    for now_idx in range(n):
        height=heights[now_idx]
        if not stack or stack[-1][0]<height: stack.append((height,now_idx))
        else:
            while stack and stack[-1][0]>=height:
                p_height,p_idx=stack.pop()
                if stack:res=max(res,p_height*(now_idx-stack[-1][1]-1))
                else:res=max(res,p_height*now_idx)
            stack.append((height,now_idx))
    now_idx=n
    while stack:
        p_height,p_idx=stack.pop()
        if stack:res=max(res,p_height*(now_idx-stack[-1][1]-1))
        else: res=max(res,p_height*now_idx)
    return res        
                    
    
    
if __name__=="__main__":
    n=int(input())
    heights=[int(input()) for _ in range(n)]
    print(solve())
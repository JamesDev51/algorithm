def make_new_u(u):
        strip_u=u[1:-1]
        new_u=''
        for ch in strip_u:
            if ch=='(':new_u+=')'
            else:new_u+='('
        return new_u
    
def check(p):
    if not p:return '' #1번: 빈 문자열
    left,right=0,0
    stack=[]
    for idx in range(len(p)):
        ch=p[idx]
        if ch=='(':left+=1;stack.append(ch)
        else:
            right+=1
            if stack and stack[-1]=='(':stack.pop()
            else:stack.append(ch)
        if left>0 and right>0 and left==right:break
    div_idx=left+right
    u,v=p[:div_idx],p[div_idx:]
    if not stack: #3번: u가 올바른 괄호 문자열
        return u+check(v)
    else: #4번: u가 올바른 괄호 문자열이 x
        return '('+check(v)+')'+make_new_u(u)

def solution(p):
    answer=check(p)
        
    return answer
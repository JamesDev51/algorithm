def check(s):
    stack=[]
    for ch in s:
        if ch in "({[":stack.append(ch)
        else:
            if not stack: return False
            if stack and (ch==")" and stack[-1]=="(") or (ch=="]" and stack[-1]=="[") or (ch=="}" and stack[-1]=="{"):
                stack.pop()
    if not stack:return True

def solution(s):
    answer = 0
    
    for i in range(len(s)):
        new_s=s[i:]+s[:i]
        if check(new_s):answer+=1
    
    return answer
def solution(ingredient):
    answer = 0
    stack=[]
    for i in ingredient:
        if len(stack)>=3:
            if i==1 and stack[-1]==3 and stack[-2]==2 and stack[-3]==1:
                for _ in range(3):stack.pop()
                answer+=1
            else: stack.append(i)
        else:stack.append(i)
        
        
    return answer
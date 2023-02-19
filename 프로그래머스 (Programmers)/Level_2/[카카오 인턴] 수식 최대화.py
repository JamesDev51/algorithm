from itertools import permutations
def init(expressions):
    exp_set=set()
    for ch in expressions:
        if not ch.isdigit():
            exp_set.add(ch)
    return exp_set


def solution(expression):
    answer = 0
    ex_set=list(init(expression))
    
    num=0;stack=[];op_stack=[]
    for perm in permutations(ex_set,len(ex_set)):
        perm_prior=dict()
        for idx in range(len(ex_set)):
            perm_prior[perm[idx]]=idx
        
        for ch in expression:
            if ch.isdigit():
                num=num*10+int(ch)
            else:
                stack.append(num)
                num=0
                while op_stack and perm_prior[op_stack[-1]]>=perm_prior[ch]:
                    operator=op_stack.pop()
                    num2,num1=stack.pop(),stack.pop()
                    if operator=="+":stack.append(num1+num2)
                    elif operator=="-":stack.append(num1-num2)
                    elif operator=="*":stack.append(num1*num2)
                op_stack.append(ch)
        stack.append(num)
        num=0
        while op_stack:
            operator=op_stack.pop()
            num2,num1=stack.pop(),stack.pop()
            if operator=="+":stack.append(num1+num2)
            elif operator=="-":stack.append(num1-num2)
            elif operator=="*":stack.append(num1*num2)
        res=stack.pop()
        answer=max(answer,abs(res))
    return answer
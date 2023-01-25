def solution(n):
    answer = 0
    lt,rt=0,0
    sub_sum=0
    while lt<=rt and rt<=n:
        if n<=sub_sum:
            if sub_sum==n and lt!=0: answer+=1
            sub_sum-=lt
            lt+=1
        else:
            rt+=1
            sub_sum+=rt
            
    return answer
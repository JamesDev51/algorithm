from collections import deque
def solution(queue1, queue2):
    que1,que2=deque(queue1),deque(queue2)
    que1_sum,que2_sum=sum(que1),sum(que2)
    total_sum=que1_sum+que2_sum
    max_try=len(queue1)+len(queue2)
    if total_sum%2:return -1 #전체합이 홀수면 절대 불가능
    goal=total_sum//2
    now_try=0
    answer = -1
    
    while now_try<=600001:
        if que1_sum==que2_sum:
            answer=now_try
            break
        elif que1_sum>que2_sum:
            poped=que1.popleft()
            que2.append(poped)
            que1_sum-=poped; que2_sum+=poped
        else:
            poped=que2.popleft()
            que1.append(poped)
            que2_sum-=poped; que1_sum+=poped    
        now_try+=1
    return answer
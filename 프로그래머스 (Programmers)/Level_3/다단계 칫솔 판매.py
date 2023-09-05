import heapq

def solution(enroll, referral, seller, amount):
    n=len(enroll)
    m=len(seller)
    step=dict()
    profits=dict()
    answer = [0]*n
    
    reverse_tree=dict()
    for i in range(n):
        enroll_person=enroll[i]
        profits[enroll_person]=0
        referral_person=referral[i]
        if referral_person=='-': #추천인이 없는 경우
            reverse_tree[enroll_person]=None
            step[enroll_person]=1
        else:
            reverse_tree[enroll_person]=referral_person
            step[enroll_person]=step[referral_person]+1
    heap=[]
    
    for i in range(m):
        seller_person=seller[i]
        sold_cnt=amount[i]
        seller_person_step=step[seller_person]
        heapq.heappush(heap,(-seller_person_step,seller_person,sold_cnt*100))
    while heap:
        _,person,profit=heapq.heappop(heap)
        while person!=None:
            parents_person=reverse_tree[person]
            parents_profit=int(profit*0.1)
            
            if parents_profit==0:
                profits[person]+=profit
                break
            else:
                calculated_profit=profit-parents_profit
                profits[person]+=calculated_profit
                
            
            profit=parents_profit
            person=parents_person
    
    for i in range(n):
        enroll_person=enroll[i]
        answer[i]=profits[enroll_person]
    
    return answer
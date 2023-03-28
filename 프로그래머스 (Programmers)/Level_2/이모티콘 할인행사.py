import heapq
heap=[(0,0)]
def calculate(users, emoticons,discounts):
    
    membership=0; benefit=0
    for min_rate,threshold in users:
        total_price=0
        for i in range(len(emoticons)):
            if min_rate<=discounts[i]: #비율 이상의 할인이 이루어진다.
                total_price+=(emoticons[i]*(100-discounts[i])/100)
        if threshold<=total_price:membership+=1
        else:benefit+=total_price
    heapq.heappush(heap,(-membership,-benefit))
        
        
    
def go(users, emoticons,depth,discounts):
    if depth==len(emoticons):
        calculate(users,emoticons,discounts)
    else:
        for rate in range(10,41,10):
            discounts[depth]=rate
            go(users,emoticons,depth+1,discounts)
def solution(users, emoticons):
    go(users,emoticons,0,[0]*len(emoticons))
    answer = [-heap[0][0],-heap[0][1]]
    return answer

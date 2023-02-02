def solution(prices):
    length=len(prices)
    answer = list(range(length-1,-1,-1))
    stack=[]
    for idx in range(length):
        price=prices[idx]
        while stack and stack[-1][1]>price:
            p_idx, p_price=stack.pop()
            answer[p_idx]=idx-p_idx
        stack.append((idx,price))
        
            
            
    return answer
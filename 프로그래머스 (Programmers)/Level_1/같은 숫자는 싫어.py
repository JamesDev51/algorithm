def solution(arr):
    prev=-1
    answer = []
    for num in arr:
        if num!=prev:
            answer.append(num)
            prev=num
        
    
    
    return answer
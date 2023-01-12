def solution(numbers):
    answer = 0
    hash_table=[0]*10
    for i in range(len(numbers)):hash_table[numbers[i]]=1 
    for i in range(10): 
        if not hash_table[i]:answer+=i
    return answer
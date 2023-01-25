def solution(n):
    answer = 0
    bin_n=bin(n)
    cnt_1_n=bin_n.count('1')
    for i in range(n+1,1000000):
        if bin(i).count('1')==cnt_1_n:answer=i;break
        
    return answer
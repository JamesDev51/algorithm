def solution(a):
    answer = 0
    idx_num=list()
    for idx,num in enumerate(a):
        idx_num.append((num,idx))
    idx_num.sort()
    ch=[0]*len(a)
    smallest_idx=float('inf')
    for i in range(len(a)):
        now_idx=idx_num[i][1]
        if now_idx<smallest_idx:
            smallest_idx=now_idx
        else:
            ch[i]+=1

    largest_idx=float('-inf')
    for i in range(len(a)):
        now_idx=idx_num[i][1]
        if largest_idx<now_idx:
            largest_idx=now_idx
        else:
            ch[i]+=1
    answer=len(ch)-ch.count(2)
    
    return answer
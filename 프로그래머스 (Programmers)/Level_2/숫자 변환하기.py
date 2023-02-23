from collections import deque

def solution(x, y, n):
    que=deque(); que.append(x)
    num_hash=dict(); num_hash[x]=0
    while que:
        num=que.popleft()
        if num==y:return num_hash[y]
        new_num=num+n
        if new_num<=1_000_000:
            if new_num not in num_hash:num_hash[new_num]=num_hash[num]+1;que.append(new_num)
            elif num_hash[num]+1<num_hash[new_num]:
                num_hash[new_num]=num_hash[num]+1
                que.append(new_num)
        new_num=num*2
        if new_num<=1_000_000:
            if new_num not in num_hash:num_hash[new_num]=num_hash[num]+1;que.append(new_num)
            elif num_hash[num]+1<num_hash[new_num]:
                num_hash[new_num]=num_hash[num]+1
                que.append(new_num)
        new_num=num*3
        if new_num<=1_000_000:
            if new_num not in num_hash:num_hash[new_num]=num_hash[num]+1;que.append(new_num)
            elif num_hash[num]+1<num_hash[new_num]:
                num_hash[new_num]=num_hash[num]+1
                que.append(new_num)
    return -1
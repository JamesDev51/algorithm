def solution(s):
    answer = 1
    same,n_same=1,0
    x=s[0]; start_idx=0;idx=1
    while idx<len(s):
        if s[idx]==x:same+=1
        else: n_same+=1
        if same==n_same:
            same,n_same=1,0
            idx+=1
            start_idx=idx
            if start_idx<len(s): x=s[idx];answer+=1
        idx+=1
    return answer
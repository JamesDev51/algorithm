def solution(s):
    last_idx=[-1]*26
    answer=[0]*len(s)
    for i in range(len(s)):
        alpha=s[i]
        alpha_idx=ord(alpha)-97
        answer[i]=i-last_idx[alpha_idx] if last_idx[alpha_idx]!=-1 else -1
        last_idx[alpha_idx]=i
    return answer
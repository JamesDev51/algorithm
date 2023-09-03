def solution(s):
    answer = 1
    n=len(s)
    for mid in range(n-1):
        lt,rt=mid-1,mid+1
        cnt=1
        while 0<=lt<rt<n and s[lt]==s[rt]:
            lt-=1;rt+=1;cnt+=2
        answer=max(answer,cnt)
        
        if s[mid]==s[mid+1]:
            lt,rt=mid-1,mid+2
            cnt=2
            while 0<=lt<rt<n and s[lt]==s[rt]:
                lt-=1;rt+=1;cnt+=2
            answer=max(answer,cnt)
    return answer
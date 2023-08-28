def solution(stones, k):
    answer = 0
    lt,rt=1,max(stones)
    while lt<=rt:
        mid=(lt+rt)//2
        count=0
        for stone in stones:
            if count<k:
                if stone-mid<0:count+=1
                else:count=0
            else:
                break
        if count<k:
            answer=max(answer,mid)
            lt=mid+1
        else:
            rt=mid-1
    return answer
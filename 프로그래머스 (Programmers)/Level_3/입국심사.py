def solution(n, times):
    answer = 0
    longest=max(times)
    lt,rt=1,longest*n
    while lt<=rt:
        mid=(lt+rt)//2
        possible=0
        for time in times:possible+=(mid//time)
        if n<=possible:
            answer=mid
            rt=mid-1
        else:lt=mid+1
    return answer
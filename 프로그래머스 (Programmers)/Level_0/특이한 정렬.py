from bisect import bisect_left

def solution(numlist, n):
    answer = []
    numlist.sort()
    mid=bisect_left(numlist,n)

    
    if n in numlist:
        answer.append(n)
        lt,rt=mid-1,mid+1
    else:
        lt,rt=mid,mid+1
    while 0<=lt and rt<len(numlist) and 0<=mid<len(numlist):
        if (n-numlist[lt])<(numlist[rt]-n):
            answer.append(numlist[lt])
            lt-=1
        elif (n-numlist[lt])>(numlist[rt]-n):
            answer.append(numlist[rt])
            rt+=1
        else:
            if numlist[lt]<numlist[rt]:
                answer.append(numlist[rt])
                rt+=1
    if 0<=lt: answer.extend(reversed(numlist[:lt+1]))
    if rt<len(numlist): answer.extend(numlist[rt:])
    
    return answer
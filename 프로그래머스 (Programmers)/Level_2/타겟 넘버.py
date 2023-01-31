def back_tracking(numbers,target,step, num):
    if step==len(numbers):
        if num==target: return 1
        return 0
    ret=back_tracking(numbers,target,step+1,num+numbers[step])+back_tracking(numbers,target,step+1,num-numbers[step])
    return ret

def solution(numbers, target):
    answer = back_tracking(numbers,target,0,0)
    return answer
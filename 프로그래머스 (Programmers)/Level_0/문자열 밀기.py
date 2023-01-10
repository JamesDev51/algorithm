def solution(A, B):
    answer = -1
    for i in range(len(A)):
        tmp_str=A[-i:]+A[:-i]
        if tmp_str==B: answer=i;break
    return answer
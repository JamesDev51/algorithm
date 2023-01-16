def solution(n, arr1, arr2):
    answer=[]
    mat=[0]*n
    for i in range(n):
        mat[i]|=arr1[i]
        mat[i]|=arr2[i]
    for i in range(n):
        row=''
        for j in range(n):
            if mat[i]&(1<<j):row+='#'
            else:row+=' '
        answer.append(row[::-1])

    return answer
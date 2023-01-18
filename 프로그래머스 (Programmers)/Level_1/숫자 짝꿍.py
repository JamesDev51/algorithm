def solution(X, Y):
    answer = ''
    hash_x=[0]*10; hash_y=[0]*10
    for x in X:hash_x[int(x)]+=1
    for y in Y:hash_y[int(y)]+=1

    flag=False
    for i in range(9,-1,-1):
        jjak=min(hash_x[i],hash_y[i])
        if jjak>0:
            flag=True
            if i==0 and len(answer)==0:
                answer+='0'
            else:
                answer+=jjak*str(i)
    if not flag:answer='-1'
    return answer
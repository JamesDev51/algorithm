horizon=[0]*13
vertical=[0]*13
left_to_right=[0]*30 #n-row+col-1 
right_to_left=[0]*30 #row+col

def back_tracking(n,cnt,sy):
    if n==cnt:return 1
    ret=0
    y=sy+1
    for x in range(n):
        if not horizon[y] and not vertical[x] and not left_to_right[n-y+x-1] and not right_to_left[y+x]:
            horizon[y]=vertical[x]=left_to_right[n-y+x-1]=right_to_left[y+x]=1
            ret+=back_tracking(n,cnt+1,y)
            horizon[y]=vertical[x]=left_to_right[n-y+x-1]=right_to_left[y+x]=0
    return ret

def solution(n):
    answer = back_tracking(n,0,-1)
    return answer 
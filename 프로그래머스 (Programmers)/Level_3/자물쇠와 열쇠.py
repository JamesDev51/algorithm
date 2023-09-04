from copy import deepcopy

def check(n,m,lock_mat):
    cnt=0
    for y in range(n):
        for x in range(n):
            if lock_mat[y+m][x+m]==1:cnt+=1
    return cnt==n*n

def turn_right(m,key):
    turned_right_key=[[[0]*m for _ in range(m)] for _ in range(4)]
    
    for y in range(m):
        for x in range(m):
            turned_right_key[0][y][x]=key[y][x]
    
    for idx in range(1,4):
        for y in range(m):
            for x in range(m):
                turned_right_key[idx][x][m-y-1]=turned_right_key[idx-1][y][x]
    return turned_right_key

def solution(key, lock):
    answer = False
    n,m=len(lock),len(key)
    t=2*m+n
    lock_mat=[[0]*t for _ in range(t)]
    
    for y in range(n):
        for x in range(n):
            lock_mat[y+m][x+m]=lock[y][x]
    
    turned_right_key=turn_right(m,key)

    for y in range(t-m):
        for x in range(t-m):
            for idx in range(4):
                cp_lock_mat=deepcopy(lock_mat)
                for i in range(m):
                    for j in range(m):
                        cp_lock_mat[y+i][x+j]+=turned_right_key[idx][i][j]
                if check(n,m,cp_lock_mat):
                    answer=True
                
    return answer
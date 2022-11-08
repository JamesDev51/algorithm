import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    mat=[[0]*1001 for _ in range(1001)]
    n=int(input())
    coords=[]
    for _ in range(n):
        y,x=map(int,input().split())
        coords.append((y,x))
    coords.sort()
    y_set=set(); x_set=set()
    
    for i in range(n):
        y_set.add(coords[i][0])
        x_set.add(coords[i][1])
    y_list=list(y_set); x_list=list(x_set)
    y_list.sort()
    x_list.sort()
    
    y_idx=dict(); x_idx=dict()
    for i in range(1,len(y_list)+1):
        y_idx[y_list[i-1]]=i
    for i in range(1,len(x_list)+1):
        x_idx[x_list[i-1]]=i
    
    for i in range(n):
        mat[y_idx[coords[i][0]]][x_idx[coords[i][1]]]+=1   

    p_sum=[[0]*1001 for _ in range(1001)]

    for y in range(1,1001):
        for x in range(1,1001):
            p_sum[y][x]=p_sum[y][x-1]+p_sum[y-1][x]-p_sum[y-1][x-1]+mat[y][x]

    
    res=float('inf')
    for y in range(2,1001):
        for x in range(2,1001):
            cnt_1=p_sum[y][x]
            cnt_2=p_sum[y][1000]-cnt_1
            cnt_3=p_sum[1000][x]-cnt_1
            cnt_4=p_sum[1000][1000]-cnt_1-cnt_2-cnt_3
            res=min(res,max(cnt_1,cnt_2,cnt_3,cnt_4))
    print(res)
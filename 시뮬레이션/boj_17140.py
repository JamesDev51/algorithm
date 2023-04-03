import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def go():
    global row,col,mat
    new_mat=[[0]*100 for _ in range(100)]
    if row>=col:
        max_col=float('-inf')
        for y in range(row):
            num_hash=dict()
            for x in range(col):
                num=mat[y][x]
                if num==0:continue
                elif num not in num_hash:num_hash[num]=1
                else:num_hash[num]+=1
            max_col=min(100,max(max_col,len(num_hash)*2))
            
            idx=0
            for key,value in sorted(num_hash.items(),key=lambda x:(x[1],x[0])):
                new_mat[y][idx]=key;idx+=1
                new_mat[y][idx]=value;idx+=1
                if idx==100:break
        col=max_col
        mat=new_mat
    else:
        max_row=float('-inf')
        for x in range(col):
            num_hash=dict()
            for y in range(row):
                num=mat[y][x]
                if num==0:continue
                elif num not in num_hash:num_hash[num]=1
                else:num_hash[num]+=1
            max_row=min(100,max(max_row,len(num_hash)*2))
            
            idx=0
            for key,value in sorted(num_hash.items(),key=lambda x:(x[1],x[0])):
                new_mat[idx][x]=key;idx+=1
                new_mat[idx][x]=value;idx+=1
                if idx==100:break
        row=max_row
        mat=new_mat
        
def check():
    return mat[r-1][c-1]==k

if __name__=="__main__":
    r,c,k=map(int,input().split())
    mat=[[0]*100 for _ in range(100)]
    for i in range(3):
        arr=map(int,input().split())
        for j in range(3):mat[i][j]=next(arr)
    row,col=3,3
    for time in range(101):
        if check():
            print(time)
            exit(0)
        go()
    print(-1)
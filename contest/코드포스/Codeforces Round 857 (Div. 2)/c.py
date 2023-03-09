import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

if __name__=="__main__":
    for i in range(int(input())):
        n,m=map(int,input().split())
        mat=[[0]*m for _ in range(n)]
        num=548
        n_offset=n//2
        m_offset=m//2
        if n%2==1:n_offset+=1    
        if m%2==1:m_offset+=1
    
    
        for sy in range(n_offset):
            for sx in range(m_offset):
                for y in range(sy *2,sy*2+2):
                    for x in range(sx*2,sx*2+2):
                        if not 0<=y<n or not 0<=x<m:num+=1;continue
                        mat[y][x]=num;num+=1
            print(n*m)
            for q in mat:print(*q)

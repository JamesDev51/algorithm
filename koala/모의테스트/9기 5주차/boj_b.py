import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def init():
    for num in range(10):
        for i in range(7):
            if flags[num][i]:
                if i%3==0:
                    for x in range(1,s+1):
                        mat[num][(i//3)*(s+1)][x]='-'
                else:
                    if i==1:
                        for y in range(1,s+1):mat[num][y][0]='|'
                    elif i==2:
                        for y in range(1,s+1):mat[num][y][s+1]='|'
                    elif i==4:
                        for y in range(s+2,2*s+2):mat[num][y][0]='|'
                    elif i==5:
                        for y in range(s+2,2*s+2):mat[num][y][s+1]='|'
                    
                        

if __name__=="__main__":
    s,n=map(int,input().split())
    flags=[
        [1,1,1,0,1,1,1],
        [0,0,1,0,0,1,0],
        [1,0,1,1,1,0,1],
        [1,0,1,1,0,1,1],
        [0,1,1,1,0,1,0],
        [1,1,0,1,0,1,1],
        [1,1,0,1,1,1,1],
        [1,0,1,0,0,1,0],
        [1,1,1,1,1,1,1],
        [1,1,1,1,0,1,1]]
    mat=[[[' ']*(s+2) for _ in range(2*s+3)] for _ in range(10)]
    init()
    str_n=str(n)
    res=[[' ']*((s+3)*(len(str_n))) for _ in range(2*s+3)]
    for i in range(len(str_n)):
        offset=i*(s+3)
        num=int(str_n[i])
        for y in range(2*s+3):
            for x in range(s+2):
                res[y][offset+x]=mat[num][y][x]
    for q in res:
        print(''.join(q[:-1]))
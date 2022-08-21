import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve():
    b_time_taken=0; 
    score=0
    for i in range(n):
        x,c=info[i]
        b_time=b_time_taken+rb*x #현재 x에서 베시 시간
        f_time=rf*x
        taste_time=f_time-b_time
        if taste_time>0:
            score+=taste_time*c
            b_time_taken+=taste_time
    print(score)
        
    
if __name__=="__main__":
    l,n,rf,rb=map(int,input().split())
    info=[list(map(int,input().split())) for _ in range(n)]
    info.sort(key=lambda x:(-x[1],x[0]))
    solve()
    
    '''
    베시
    0 3 6 9 12 15 18 21 24 27 30
                     28 31 
    농부
    0 4 8 12 16 20 24 28 32 36 40
    '''
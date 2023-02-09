import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def get_distance(prev_y,prev_x,now_y,now_x):
    return abs(prev_y-now_y)+abs(prev_x-now_x)

def get_middle(prev_y,prev_x,now_y,now_x):
    return (abs(prev_y+now_y)/2,abs(prev_x+now_x)/2)
    

def solve():
    ch[patterns[0]]=1
    for i in range(1,len(patterns)):
        prev,now=patterns[i-1],patterns[i]
        prev_y,prev_x=prev//3,prev%3
        now_y,now_x=now//3,now%3
        dist=get_distance(prev_y,prev_x,now_y,now_x)
        
        if ch[now]:return False
        if dist==1:ch[now]=1;continue
        else:
            middle=get_middle(prev_y,prev_x,now_y,now_x)            
            if 0<middle[0]<1 or 0<middle[1]<1 or 1<middle[0]<2 or 1<middle[1]<2:ch[now]=1;continue
            if ch[int(middle[0]*3+middle[1])]: ch[now]=1;continue
            return False
    return True

if __name__=="__main__":
    n=int(input())
    patterns=list(map(int,input().split()))
    for i in range(len(patterns)):patterns[i]-=1
    ch=[0]*9
    print("YES" if solve() else "NO")
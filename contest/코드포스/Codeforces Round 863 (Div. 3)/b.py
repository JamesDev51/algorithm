import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

if __name__=="__main__":
    for _ in range(int(input())):
        n,x1,y1,x2,y2=map(int,input().split())
        lm,rm=n//2,n//2+1
        c1,c2=-1e9,-1e9
        if x1<=lm:c1=max(c1,lm-x1+1)            
        else:c1=max(c1,x1-rm+1)
        if y1<=lm:c1=max(c1,lm-y1+1)            
        else:c1=max(c1,y1-rm+1)

        if x2<=lm:c2=max(c2,lm-x2+1)            
        else:c2=max(c2,x2-rm+1)
        if y2<=lm:c2=max(c2,lm-y2+1)            
        else:c2=max(c2,y2-rm+1)
        print(abs(c1-c2))
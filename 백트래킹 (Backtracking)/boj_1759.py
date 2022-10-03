import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def dfs(idx,c_cnt,v_cnt,secret):
    if len(secret)==l : 
        if c_cnt>=2 and v_cnt>=1: print(secret)
        return
    if idx==c: return
    
    alpha=arr[idx]    
    if alpha in vowel:v_cnt+=1        
    else: c_cnt+=1
    dfs(idx+1,c_cnt,v_cnt,secret+alpha)

    if alpha in vowel:v_cnt-=1        
    else: c_cnt-=1
    dfs(idx+1,c_cnt,v_cnt,secret)
        

if __name__=="__main__":
    l,c=map(int,input().split())
    arr=list(input().strip().split())
    vowel="aeiou"
    arr.sort()
    dfs(0,0,0,"")

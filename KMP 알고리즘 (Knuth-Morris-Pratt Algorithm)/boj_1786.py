import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def getFail():
    fail=[0]*len(p)
    j=0
    for i in range(1,len(p)):
        while j and p[i]!=p[j]:j=fail[j-1]
        if p[i]==p[j]: j+=1; fail[i]=j
    return fail

def kmp():
    fail=getFail()
    res=[]
    
    j=0
    for i in range(len(t)):
        while j and t[i]!=p[j]: j=fail[j-1]    
        if t[i]==p[j]:
            if j==len(p)-1: #끝까지 온 경우 
                res.append(i-len(p)+2) #답을 찾음
                j=fail[j] #찾지 못한 것처럼 다시 실패함수쪽으로 이동시킴
            else: j+=1 #끝이 아니면 한칸 앞으로 이동
    print(len(res))
    print(*res)

if __name__=="__main__":
    t=input().rstrip()
    p=input().rstrip()
    kmp()

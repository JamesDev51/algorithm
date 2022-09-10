import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    stacks=[[] for _ in range(7)]
    res=0
    n,p=map(int,input().split())
    for _ in range(n):
        line,pret=map(int,input().split())
        if not stacks[line]:
            stacks[line].append(pret);res+=1
        else:
            while stacks[line] and stacks[line][-1]>pret:
                stacks[line].pop()
                res+=1
            if stacks[line] and stacks[line][-1]==pret: continue
            else: stacks[line].append(pret); res+=1
    print(res)
            
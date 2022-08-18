import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    case=1
    while True:
        l,p,v=map(int,input().split())
        if not l and not p and not v:break
        print(f"Case {case}: {(v//p)*l+min(v%p,l)}")
        case+=1
        
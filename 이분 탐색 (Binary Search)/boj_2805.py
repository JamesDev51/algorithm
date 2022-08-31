import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def check_amount(height):
    amount_sum=0
    for i in range(n):amount_sum+=(trees[i]-height if trees[i]>height else 0)
    return amount_sum


def solve():
    res=-1e9
    lt,rt=0,max(trees)
    while lt<=rt:
        mid=(lt+rt)//2
        amount=check_amount(mid)
        if m<=amount:
            res=max(res,mid)
            lt=mid+1
        else: rt=mid-1
    return res

if __name__=="__main__":
    n,m=map(int, input().split())
    trees=list(map(int,input().split()))
    print(solve())
import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def calculate(num1,num2,operator):
    if operator=="+":return num1+num2
    elif operator=="-":return num1-num2
    elif operator=="*":return num1*num2
    
def solve():
    max_dp[0]=operands[0]
    min_dp[0]=operands[0]
    max_dp[1]=calculate(max_dp[0],operands[1],operators[0])
    min_dp[1]=calculate(min_dp[0],operands[1],operators[0])
    for i in range(1,len(operators)):
        max_dp[i+1]=max(calculate(max_dp[i],operands[i+1],operators[i]),calculate(max_dp[i-1],calculate(operands[i],operands[i+1],operators[i]),operators[i-1]),calculate(min_dp[i],operands[i+1],operators[i]))
        min_dp[i+1]=min(calculate(min_dp[i],operands[i+1],operators[i]),calculate(min_dp[i-1],calculate(operands[i],operands[i+1],operators[i]),operators[i-1]))
    return max_dp[-1]
        

if __name__=="__main__":
    n=int(input())
    op=list(input().strip())
    operands=list()
    operators=list()
    for i in range(n):
        if i%2==0:operands.append(int(op[i]))
        else:operators.append(op[i])
    max_dp=[0]*(len(operators)+1)
    min_dp=[0]*(len(operators)+1)
    print(solve())
    print(max_dp)
    print(min_dp)
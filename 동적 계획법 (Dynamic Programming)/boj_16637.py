import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def calc(num1,num2,operator):
    if operator=="+":return num1+num2
    elif operator=="-":return num1-num2
    elif operator=="*":return num1*num2
    
def solve():
    if len(operands)==1:return operands[0]
    max_dp[0]=operands[0]
    min_dp[0]=operands[0]
    max_dp[1]=calc(max_dp[0],operands[1],operators[1])
    min_dp[1]=calc(min_dp[0],operands[1],operators[1])
    for i in range(2,len(operators)):
        min_dp[i]=min(calc(min_dp[i-1],operands[i],operators[i]),calc(min_dp[i-2],calc(operands[i-1],operands[i],operators[i]),operators[i-1]), calc(max_dp[i-1],operands[i],operators[i]), calc(max_dp[i-2],calc(operands[i-1],operands[i],operators[i]),operators[i-1]))
        max_dp[i]=max(calc(max_dp[i-1],operands[i],operators[i]),calc(max_dp[i-2],calc(operands[i-1],operands[i],operators[i]),operators[i-1]),calc(min_dp[i-1],operands[i],operators[i]), calc(min_dp[i-2],calc(operands[i-1],operands[i],operators[i]),operators[i-1]))
    return max_dp[-1]


if __name__=="__main__":
    n=1+int(input())
    op=['+']+list(input().strip())
    operands=list()
    operators=list()
    for i in range(n):
        if i%2==1:operands.append(int(op[i]))
        else:operators.append(op[i])
    max_dp=[0]*len(operators)
    min_dp=[0]*len(operators)
    print(solve())
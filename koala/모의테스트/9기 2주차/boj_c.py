import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve():
    remove_count=0;stack=[]
    for each_num in num:
        while stack and remove_count<k and int(stack[-1])<int(each_num):
            stack.pop(); remove_count+=1
        stack.append(each_num)
    
    while len(stack)>n-k:stack.pop()
    
    return ''.join(stack)
        
if __name__=="__main__":
    n,k=map(int,input().split())
    num=input().strip()
    print(solve())
import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def check(start):
    ch=[0]*(n+1)
    node=start
    while not ch[node]:
        tmp_answer.append(node)
        ch[node]=1
        node=graph[node]
        if node==start:return True
    return False
        

def solve():
    global answer
    ch=[0]*(n+1)
    for node in range(1,n+1):
        tmp_answer.clear()
        if not ch[node] and check(node): answer.extend(tmp_answer)
    answer=list(set(answer))

if __name__=="__main__":
    n=int(input())
    graph=[0]*(n+1)
    for node in range(1,n+1):
        next_node=int(input())
        graph[node]=next_node
    tmp_answer=[]
    answer=[]
    solve()
    answer.sort()
    print(len(answer))
    for ans in answer:print(ans)
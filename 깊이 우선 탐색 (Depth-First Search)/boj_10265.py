import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def dfs(node):
    global flag, cycle_size
    visited[node]=1
    ret=0
    for next_node in graph[node]:
        if not visited[next_node]:
            ret+=dfs(next_node)
        else:
            if not finished[next_node]:
                flag=True
                cycle_size+=1
                tmp_node=node
                while tmp_node!=next_node:
                    cycle_size+=1
                    tmp_node=graph_org[tmp_node][0]
    finished[node]=1
    return ret+1

if __name__=="__main__":
    n,k=map(int,input().split())
    likes=map(int,input().split())
    graph_org=[[] for _ in range(n+1)]
    graph=[[] for _ in range(n+1)]
    for out_person in range(1,n+1):
        in_person=next(likes)
        graph_org[out_person].append(in_person)
        graph[in_person].append(out_person)
    
    info=[]
    visited=[0]*(n+1); finished=[0]*(n+1)
    flag=False
    
    for node in range(1,n+1):
        flag=False
        if not visited[node]:
            cycle_size=0
            tot_size=dfs(node)
            if not flag:
                for i in range(1,n+1): visited[i]=0; finished[i]=0
            else:
                if cycle_size<=k:info.append((cycle_size,tot_size))
    
    dp=[[0]*(k+1) for _ in range(len(info)+1)]
    for i in range(1,len(info)+1):
        c,nc=info[i-1]
        for j in range(1,k+1):
            if j<c:dp[i][j]=dp[i-1][j]
            else:dp[i][j]=min(k,max(dp[i-1][j],dp[i-1][j-c]+nc))
    result=max(dp[len(info)])
    print(result)
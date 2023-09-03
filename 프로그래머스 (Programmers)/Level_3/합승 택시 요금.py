def floyd_warshall(n,s,a,b,fares):
    fare_map=[[float('inf')]*(n+1) for _ in range(n+1)]
    for node in range(n+1):fare_map[node][node]=0
    for n1,n2,fare in fares:
        fare_map[n1][n2]=fare
        fare_map[n2][n1]=fare
    
    
    for mid in range(1,n+1):
        for start in range(1,n+1):
            for end in range(1,n+1):
                if fare_map[start][mid]+fare_map[mid][end]<fare_map[start][end]:
                    fare_map[start][end]=fare_map[start][mid]+fare_map[mid][end]
    answer=min(fare_map[s][a]+fare_map[a][b],fare_map[s][b]+fare_map[b][a],fare_map[s][a]+fare_map[s][b])
    for mid in range(1,n+1):
        answer=min(answer,fare_map[s][mid]+fare_map[mid][a]+fare_map[mid][b])
    
    return answer


def solution(n, s, a, b, fares):
    answer=floyd_warshall(n,s,a,b,fares)
    return answer
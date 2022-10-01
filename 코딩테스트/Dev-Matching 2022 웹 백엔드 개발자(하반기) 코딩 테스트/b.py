import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


from collections import deque


def bfs(maps,ch,que,sy,sx,n,m):
    country_dict=dict()
    ch[sy][sx]=1
    country_dict[maps[sy][sx]]=1
    que.append((sy,sx))
    while que:
        y,x=que.popleft()
        for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
            ny,nx=y+dy,x+dx
            if 0<=ny<n and 0<=nx<m and maps[ny][nx]!='.' and not ch[ny][nx]:
                country=maps[ny][nx]
                if country in country_dict:country_dict[country]+=1  
                else: country_dict[country]=1
                ch[ny][nx]=1
                que.append((ny,nx))
    items=list(country_dict.items())
    items.sort(key=lambda x:(x[1],x[0]))
    dom_name, dom_num=items[-1]
    new_country_dict=dict()
    new_country_dict[dom_name]=dom_num

    for sub_name,sub_num in items:
        if sub_name==dom_name:continue
        if sub_num<dom_num:new_country_dict[dom_name]+=sub_num
        else:new_country_dict[sub_name]=sub_num
    return new_country_dict           
    
    

                                


def solution(maps):
    answer = 0
    n,m=len(maps), len(maps[0])
    ch=[[0]*m for _ in range(n)]
    que=deque()
    result_dict=dict()
    for y in range(n):
        for x in range(m):
            if maps[y][x]!='.' and not ch[y][x]:
                ret_dict=bfs(maps,ch,que,y,x,n,m)            

                for country,num in ret_dict.items():
                    if country in result_dict: result_dict[country]+=num
                    else: result_dict[country]=num
    result_items=list(result_dict.items())
    result_items.sort(key=lambda x:(x[1],x[0]))
    return result_items[-1][1]
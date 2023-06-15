import heapq

def solution(plans):
    answer = []
    
    stack=[]
    task_heap=[]
    for name,start,playtime in plans:
        h,m=map(int,start.split(":"))
        heapq.heappush(task_heap,[h*60+m,int(playtime),name])
        
    for t in range(1000000):
        if stack:stack[-1][1]-=1
        if stack and stack[-1][1]==0:answer.append(stack.pop()[2])
        
        if task_heap and task_heap[0][0]==t:
            stack.append(heapq.heappop(task_heap))
        
        
        
    
    return answer
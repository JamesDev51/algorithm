import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
from collections import deque

if __name__=="__main__":
    s=input().strip()
    t=input().strip()
    answer=0
    used=set()
    que=deque(); que.append(s)
    while que:
        string=que.popleft()
        if string in used: continue
        else: used.add(string)
        if string==t:answer=1;break
        if string in t and len(string)<len(t):
            que.append(string+'A')
            que.append('B'+string[::-1])
        if string[::-1] in t and len(string)<len(t):
            que.append(string+'A')
            que.append('B'+string[::-1])
    print(answer)
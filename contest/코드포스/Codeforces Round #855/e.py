import sys
sys.stdin = open("input.text",  "rt")
import sys
from collections import deque
input=sys.stdin.readline

if __name__=="__main__":
    for _ in range(int(input())):
        n,k=map(int,input().split())
        s=input().strip()
        t=input().strip()
        used=set();used.add(s)
        que=deque();que.append(s)
        flag=False
        while que:
            word=que.popleft()
            if word==t:
                flag=True;break
            for i in range(n-3):
                new_word=word[:i]+word[i+3]+word[i+1:i+3]+word[i]+word[i+3:]
                if new_word not in used:
                    used.add(new_word)
                    que.append(new_word)
                if i+4<n:
                    new_word=word[:i]+word[i+4]+word[i+1:i+4]+word[i]+word[i+4:]
                    if new_word not in used:
                        used.add(new_word)
                        que.append(new_word)
    print("YES" if flag else "NO")
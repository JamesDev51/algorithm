import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def check(s):
    if len(s)<4:return False
    s=s.lower()
    word="meow";idx=0
    for i in range(n):
        ch=s[i]
        if ch not in word:return False
        if word[idx]==ch:continue
        else:
            idx+=1
            if idx==4:return False
            if word[idx]==ch:continue
            else:return False
    if idx<3:return False
    return True
        

if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        s=input().strip()
        print("YES" if check(s) else "NO")
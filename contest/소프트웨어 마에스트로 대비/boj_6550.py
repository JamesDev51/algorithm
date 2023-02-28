import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def check(s,t):
    idx=0
    for ch in t:
        if s[idx]==ch:idx+=1
        if idx==len(s):return True
    return False

if __name__=="__main__":
    while True:
        try:
            s,t=input().split(" ")
            print("Yes" if check(s,t)else "No")
        except ValueError:
            break
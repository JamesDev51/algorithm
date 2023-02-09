import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

if __name__=="__main__":
    find=input().strip()
    answer=0
    for _ in range(int(input())):
        sent=input().strip()
        sent=sent+sent[:len(find)-1]
        if find in sent:answer+=1
    print(answer)
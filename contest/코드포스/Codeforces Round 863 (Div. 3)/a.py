import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

if __name__=="__main__":
    for _ in range(int(input())):
        n,d=input().split()
        num=input().strip()
        for i in range(int(n)):
            if num[i]<d:
                print(num[:i]+d+num[i:])
                break
        else:
            print(num+d)
        
            
        
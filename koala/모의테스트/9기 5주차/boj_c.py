import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

if __name__=="__main__":
    phrase=input().strip()
    exploded_phrase=input().strip()
    stack=[]; idx=0
    for ch in phrase:
        stack.append(ch)
        if len(stack)>=len(exploded_phrase) and stack[-1]==exploded_phrase[-1]:
            if ''.join(stack[-len(exploded_phrase):])==exploded_phrase:
                for _ in range(len(exploded_phrase)):stack.pop()
    print("FRULA" if not stack else ''.join(stack))
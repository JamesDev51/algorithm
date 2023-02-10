import sys
sys.setrecursionlimit(10000000)

cnt=0
ans=-1
def find(find_word,now,level):
    global cnt,ans
    if find_word==now:ans=cnt
    if level<5:
        for ch in "AEIOU":
            cnt+=1
            find(find_word,now+ch,level+1)

def solution(word):
    find(word,'',0)
    return ans
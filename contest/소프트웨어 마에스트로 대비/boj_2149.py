import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    key=input().strip()
    cipher=input().strip()
    col=len(key);row=len(cipher)//col
    
    sorted_key=list()
    for idx, ch in enumerate(list(key)):sorted_key.append((ch,idx))
    sorted_key.sort()
    mat=[['']*col for _ in range(row)]
    idx=0
    for key_idx in range(col):
        x=sorted_key[key_idx][1]
        for y in range(row):
            mat[y][x]=cipher[idx];idx+=1
    answer=''
    for q in mat:answer+=''.join(q)
    print(answer)
            
                
    
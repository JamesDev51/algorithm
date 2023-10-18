import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    pizza=int(input())
    m,n=map(int,input().split())
    m_parts=list(int(input()) for _ in range(m))
    n_parts=list(int(input()) for _ in range(n))
    m_hash,n_hash=[0]*(pizza+1),[0]*(pizza+1)
    m_hash[0]=1;n_hash[0]=1
    
    m_parts_acc=[0]*(m+1)
    n_parts_acc=[0]*(n+1)
    
    for i in range(m):
        m_parts_acc[i+1]=m_parts_acc[i]+m_parts[i]
    for i in range(1,m+1):
        for j in range(i-1,-1,-1):
            diff=m_parts_acc[i]-m_parts_acc[j]
            if diff<=pizza:m_hash[diff]+=1
            else:break
    rear_acc=0
    for i in range(m-1,-1,-1):
        rear_acc+=m_parts[i]
        if pizza<=rear_acc:break
        front_acc=0
        for j in range(i-1):
            front_acc+=m_parts[j]
            if rear_acc+front_acc<=pizza:m_hash[rear_acc+front_acc]+=1
            else:break
            
    for i in range(n):
        n_parts_acc[i+1]=n_parts_acc[i]+n_parts[i]
    for i in range(1,n+1):
        for j in range(i-1,-1,-1):
            diff=n_parts_acc[i]-n_parts_acc[j]
            if diff<=pizza:n_hash[diff]+=1
            else:break
            
    rear_acc=0
    for i in range(n-1,-1,-1):
        rear_acc+=n_parts[i]
        if pizza<=rear_acc:break
        front_acc=0
        for j in range(i-1):
            front_acc+=n_parts[j]
            if rear_acc+front_acc<=pizza:n_hash[rear_acc+front_acc]+=1
            else:break
    answer=0
    for i in range(pizza+1):
        answer+=m_hash[i]*n_hash[pizza-i]
    print(answer)
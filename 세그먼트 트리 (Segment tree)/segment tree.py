#start: 시작 인덱스,  end: 끝 인덱스 (구간 나눠짐)
#node: 노드 번호
def init(start, end, node):
    if start==end: #리프 노드에 도달한 경우
        tree[node]=arr[start]  #리프 노드에 해당 인덱스 값을 넣고
        return tree[node] #값을 리턴
    mid=(start+end)//2 #구간 쪼개기
    tree[node]=init(start,mid,node*2)+init(mid+1,end,node*2+1) #재귀적으로 자식 노드들의 합을 노드에 할당
    return tree[node] #부모에게 값 리턴

#start: 시작 인덱스, end: 끝 인덱스 (구간 나눠짐)
#node: 노드 번호
#left, right: 구간 합을 구하고자 하는 인덱스 범위
def sub_sum(start, end, node, left, right):
    if end<left or right<start: return 0 #구간에 포함되지 않는 경우에는 0을 리턴(합에는 영향을 주지 않음)
    if left<=start<=end<=right: return tree[node] #구간에 전부 포함되는 경우에는 바로 그 노드 값을 리턴
    mid=(start+end)//2
    return sub_sum(start,mid,node*2,left,right) + sub_sum(mid+1, end, node*2+1, left, right) #재귀적으로 자식 노드들의 합을 구하기 

def update(start,end, node,index, new_value):
    if index<start or end<index: return tree[node] #범위를 벗어난 경우에는 변화가 없는 구간이므로 노드 값 리턴
    if start==end: #끝까지 내려갔으면 
        tree[node]=new_value #리프노드 밸류 갱신
        return tree[node] #리프노드 리턴
    mid=(start+end)//2
    tree[node]=update(start,mid,node*2,index,new_value)+update(mid+1,end,node*2+1, index,new_value) #리프노드부터 부모까지 재귀적으로 업데이트됨
    return tree[node]

if __name__ =="__main__":
    n=9
    arr=[1,2,3,4,5,6,7,8,9]
    tree=[0]*(4*n) #트리는 최대 4n 정도 크기를 미리 할당해놓기
    init(0,n-1,1)
    print(sub_sum(0, n-1, 1, 0, 9))
    update(0,n-1,1,3,14)
    print(sub_sum(0, n-1, 1, 0, 9))
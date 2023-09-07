import heapq
import sys
sys.setrecursionlimit(100000)

answer = [[],[]]
tree=[[None]*2 for _ in range(10002)]

def make_tree(heap_nodes):
    if len(heap_nodes)==0:
        return None
    elif len(heap_nodes)==1:
        return heap_nodes[0][2]
    
    left_heap,right_heap=[],[]
    _,px,p_idx=heapq.heappop(heap_nodes)
    
    for y,x,idx in heap_nodes:
        if x<px:heapq.heappush(left_heap,[y,x,idx])
        else:heapq.heappush(right_heap,[y,x,idx])
    
    tree[p_idx][0]=make_tree(left_heap)
    tree[p_idx][1]=make_tree(right_heap)
    return p_idx

def preorder(node):
    answer[0].append(node)
    left_node,right_node=tree[node]
    if left_node!=None:preorder(left_node)
    if right_node!=None:preorder(right_node)
    
def postorder(node):
    left_node,right_node=tree[node]
    if left_node!=None:postorder(left_node)
    if right_node!=None:postorder(right_node)
    answer[1].append(node)
    
        
    
def solution(nodeinfo):
    heap=[]
    for idx,val in enumerate(nodeinfo):
        x,y=val
        heapq.heappush(heap,[-y,x,idx+1])
    root=heap[0][2]
    make_tree(heap)
    
    preorder(root)
    postorder(root)
    
    return answer
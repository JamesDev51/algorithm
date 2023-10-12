import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def tracking_tree(node):
    if not tree[node]:return 0
    
    
    ret_list=[]
    for child_node in tree[node]:
        ret_list.append(tracking_tree(child_node))
    ret_list.sort()
    
    for i in range(len(ret_list)):
        ret_list[i]+=(len(ret_list)-i)
    ret_list.sort()
    return ret_list[-1]
        
        
        
if __name__=="__main__":
    n=int(input())
    tree_info=list(map(int,input().split()))
    tree=[[] for _ in range(n+1)]
    for now_node,parents_node in enumerate(tree_info):
        if parents_node==-1:continue
        tree[parents_node].append(now_node)
    print(tracking_tree(0))
            
        
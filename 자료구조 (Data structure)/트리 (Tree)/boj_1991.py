import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def preorder(node):
    print(node,end="")
    if tree[node][0]!=".":preorder(tree[node][0])
    if tree[node][1]!=".":preorder(tree[node][1])

def inorder(node):
    if tree[node][0]!=".":inorder(tree[node][0])
    print(node,end="")
    if tree[node][1]!=".":inorder(tree[node][1])
    

def postorder(node):
    if tree[node][0]!=".":postorder(tree[node][0])
    if tree[node][1]!=".":postorder(tree[node][1])
    print(node,end="")

if __name__=="__main__":
    n=int(input())
    tree=dict()
    for _ in range(n):
        node,left,right=input().split()
        tree[node]=[left,right]
        
    root='A'
    preorder(root)
    print()
    inorder(root)
    print()
    postorder(root)
    
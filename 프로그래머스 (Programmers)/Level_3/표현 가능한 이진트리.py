from collections import deque

def convert_bin(number):
    return bin(number)[2:]

def add_zero(bin_number):
    tot=0
    idx=0
    while tot<len(bin_number):
        tot+=pow(2,idx)
        idx+=1
    bin_number='0'*(tot-len(bin_number))+bin_number
    return bin_number

def inorder(now,full_bin_number):
    global tree,idx
    if now>len(full_bin_number):return
    inorder(now*2,full_bin_number)
    tree[now]=int(full_bin_number[idx]);idx+=1
    inorder(now*2+1,full_bin_number)
    

tree=[];idx=1
def make_tree(full_bin_number):
    global tree,idx
    tree=[0]*(len(full_bin_number)+1)
    idx=0
    inorder(1,full_bin_number)

def check(limit):
    for i in range(1,limit+1):
        if i*2+1>=limit+1:continue
        if not tree[i] and (tree[i*2] or tree[i*2+1]):return False
    return True
    

def solution(numbers):
    answer = []
    for number in numbers:
        bin_number=convert_bin(number)
        full_bin_number=add_zero(bin_number)
        make_tree(full_bin_number)
        if check(len(full_bin_number)):answer.append(1)
        else:answer.append(0)
    return answer
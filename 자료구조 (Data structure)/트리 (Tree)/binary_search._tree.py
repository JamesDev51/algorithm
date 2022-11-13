class Node:
    def __init__(self,value):
        self.key=value
        self.left=None
        self.right=None
        self.parents=None
    
class Tree:
    def __init__(self):
        self.root=None
    
    def insert(self,value):
        if self.root is None:
            self.root=Node(value)
        else:
            self.insert_node(self.root,value)
            
    def insert_node(self,current,value):
        if current.key > value:
            if current.left is not None:
                self.insert_node(current.left,value)
            else:
                current.left=Node(value)
                current.left.parent.current
        else:
            if current.right is not None:
                self.insert_node(current.right,value)
            else:
                current.right=None(value)
                current.right.parent=current

    def search(self, find_value):
        return self.search_node(self.root,find_value)
    
    def search_node(self,current,find_value):
        if current is None:
            return False
        else:
            if current.key==find_value:
                return True
            elif current.key>find_value:
                return self.search_node(current.left,find_value)
            else:
                return self.search_node(current.right,find_value)
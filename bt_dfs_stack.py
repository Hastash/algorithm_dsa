class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

def dfs_traversal(node):
    if node is None: return
    
    stack=[]
    stack.append(node)
    
    while stack:
        curNode = stack.pop()
        print(curNode.value, end=" ")
        # Since we want to traverse left before right, 
        # we push right child first
        if curNode.right:
            stack.append(curNode.right)
        if curNode.left:
            stack.append(curNode.left)

# Example binary tree
#       1
#      / \
#     2   3
#    / \
#   4   5
#  /
# 6
example_tree = Node(1)
example_tree.left = Node(2)
example_tree.right = Node(3)
example_tree.left.left = Node(4)
example_tree.left.right = Node(5)
example_tree.left.left.left = Node(6)
         
print("DFS Traversal:")
dfs_traversal(example_tree)             
    
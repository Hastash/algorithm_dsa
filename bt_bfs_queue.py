from collections import deque
class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

def bfs_traversal(node):
    if node is None: return
    
    queue=deque()
    queue.append(node)
    
    while queue:
        curNode = queue.popleft()
        print(curNode.value, end=" ")
        # Since we want to traverse left before right, 
        # we push left child first
        if curNode.left:
            queue.append(curNode.left)
        if curNode.right:
            queue.append(curNode.right)

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
bfs_traversal(example_tree)             
    
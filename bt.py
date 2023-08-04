class BinaryTree:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def count_levels(node):
    if node is None: return 0
    else:
        leftLevels = count_levels(node.left)
        rightLevels = count_levels(node.right)
        return 1 + max(leftLevels, rightLevels)

#Test Cases
# Empty tree
empty_tree = None
print(count_levels(empty_tree))

#Single Node Tree
single_node_tree = BinaryTree(3)
print(count_levels(single_node_tree))


#Example Tree
#       1
#      / \
#     2   3
#    / \
#   4   5
#  /
# 6

example_tree = BinaryTree(1)
example_tree.left = BinaryTree(2)
example_tree.right = BinaryTree(3)
example_tree.left.left = BinaryTree(4)
example_tree.left.right = BinaryTree(5)
example_tree.left.left.left = BinaryTree(6)
example_tree.left.left.left.left = BinaryTree(7)


print(count_levels(example_tree))
    
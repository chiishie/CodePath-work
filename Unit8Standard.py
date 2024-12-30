from collections import deque

# Tree Node class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)
    
root = TreeNode("Trunk")
   
root.left = TreeNode("Mcintosh")
root.right = TreeNode("GrannySmith")

# Root's Grandchildren
root.left.left = TreeNode("Fuji")
root.left.right = TreeNode("Opal")
root.right.left = TreeNode("Crab")
root.right.right = TreeNode("Gala")
                



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


root = TreeNode("Poseidon")
root.left = TreeNode("Atlantis")
root.right = TreeNode("Oceania")
root.left.left = TreeNode("Coral")
root.left.right = TreeNode("Pearl")
root.right.left = TreeNode("Kelp")
root.right.right = TreeNode("Reef")

print_tree(root)

def mertwins(root):
    if root is None:
        return False
    
    elif root.right is None or root.left is None:
        return False
    
    else:
        if root.left.val == root.right.val:
            return True
        else:
            return False

    
root1 = TreeNode("Mermother", TreeNode("Coral"), TreeNode("Coral"))

"""
      Merpapa
       /    \
   Calypso  Coral
"""
root2 = TreeNode("Merpapa", TreeNode("Calypso"), TreeNode("Coral"))

"""
      Merenby
           \    
         Calypso  
"""
root3 = TreeNode("Merenby", None, TreeNode("Calypso"))

print(mertwins(root1))
print(mertwins(root2))
print(mertwins(root3))


def get_decision(root):
    if root is None:
        return False
    
    elif root.left is None or root.right is None:
        return False
    
    if root.val == "AND":
        return root.left.val and root.right.val
    elif root.val == "OR":
        return root.left.val or root.right.val

expression1 = TreeNode("OR", TreeNode(True), TreeNode(False))

"""
       False
"""
expression2 = TreeNode(False)

print(get_decision(expression1))
print(get_decision(expression2))

def leftmost_path(root):
    
    if root is None:
        return []
    
    else:
        return [root.val] + leftmost_path(root.left)
    

system_a = TreeNode("CaveA", 
                  TreeNode("CaveB", TreeNode("CaveD"), TreeNode("CaveE")), 
                          TreeNode("CaveC", None, TreeNode("CaveF")))

system_b = TreeNode("CaveA", None, TreeNode("CaveB", None, TreeNode("CaveC")))

print(leftmost_path(system_a))
print(leftmost_path(system_b))

def explore_reef(root):
    
    if root is None:
        return []
    
    left = explore_reef(root.left)
    right = explore_reef(root.right)
    
    return [root.val] + left + right
                        
reef = TreeNode("CoralA", 
                TreeNode("CoralB", TreeNode("CoralD"), TreeNode("CoralE")), 
                          TreeNode("CoralC"))

print(explore_reef(reef))

def count_coral(root):
    
    if root is None:
        return 0
    
    elif root.left is None and root.right is None:
        return 1
    
    return 1 + count_coral(root.left) + count_coral(root.right)

reef1 = TreeNode("Staghorn", 
                TreeNode("Sea Fan", TreeNode("Bubble", TreeNode("Fire")), TreeNode("Table")),
                        TreeNode("Sea Whip", TreeNode("Star")))

reef2 = TreeNode("Fire", 
                TreeNode("Black"), 
                        TreeNode("Star", 
                                  TreeNode("Lettuce", None, TreeNode("Sea Whip"))))

print(count_coral(reef1))
print(count_coral(reef2))

def ocean_depth(root):
    count = 0
    if root is None:
        return 0
    
    elif root.left is None and root.right is None:
        return 1
        
    left_depth = ocean_depth(root.left)
    right_depth = ocean_depth(root.right)
    
    # The depth of the tree rooted at the current node
    return 1 + max(left_depth, right_depth)
            
ocean = TreeNode("Sunlight", 
                TreeNode("Twilight", 
                        TreeNode("Abyss", 
                                TreeNode("Trenches")), TreeNode("Anglerfish")),
                                        TreeNode("Squid", TreeNode("Giant Squid")))

tidal_zones = TreeNode("Spray Zone", 
                      TreeNode("Beach"), 
                              TreeNode("High Tide", 
                                      TreeNode("Middle Tide", None, TreeNode("Low Tide"))))

print(ocean_depth(ocean))
print(ocean_depth(tidal_zones))
    
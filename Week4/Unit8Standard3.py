from collections import deque 

# Tree Node class
class TreeNode:
  def __init__(self, value, key=None, left=None, right=None):
      self.key = key
      self.val = value
      self.left = left
      self.right = right

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root

def count_odd_splits(root):
    sum = 0
    
    if root is None:
        return 0
   
    left = count_odd_splits(root.left)
    right = count_odd_splits(root.right)
     
    if (root.val % 2) != 0:
        return 1 + left + right
    else:
        return left + right
    
    
values = [2, 3, 5, 6, 7, None, 12]
monstera = build_tree(values)

values1 = [2, 3, 5, 6, 7, None, 12, 13, 15, 17]
monstera1 = build_tree(values)

print(count_odd_splits(monstera))
print(count_odd_splits(monstera1))
print(count_odd_splits(None))
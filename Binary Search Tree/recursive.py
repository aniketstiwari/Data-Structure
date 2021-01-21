import pdb

class BST:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value


def insert(root, key):
  if root is None:
    return BST(key)
  else:
    if root.value == key:
      return root
    elif key < root.value:
      root.left = insert(root.left, key)
    else:
      root.right = insert(root.right, key)

  return root

def search(root, key):
  if root is None or root.value == key:
    return root

  if key < root.value:
    return search(root.left, key)

  return search(root.right, key)

def inorder(root):
  if root is not None:
    inorder(root.left)
    print(root.value)
    inorder(root.right)

binary_search_tree = BST(50)
binary_search_tree = insert(binary_search_tree, 30)
binary_search_tree = insert(binary_search_tree, 20)
binary_search_tree = insert(binary_search_tree, 40)
binary_search_tree = insert(binary_search_tree, 70)
binary_search_tree = insert(binary_search_tree, 60)
binary_search_tree = insert(binary_search_tree, 80)

print(search(binary_search_tree, 30))

inorder(binary_search_tree)
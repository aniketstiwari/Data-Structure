class BST:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value

  # Average O(Log(n)) time | space O(1)
  # Worst O(n) time | space O(1)
  def insert(self, value):
    currentNode = self
    while True:
      if value < currentNode.value:
        if currentNode.left is None:
          currentNode.left = BST(value)
          break
        else:
          currentNode = currentNode.left
      else:
        if currentNode.right is None:
          currentNode.right = BST(value)
          break
        else:
          currentNode = currentNode.right

    ## Adding self in the end make the chaining of methods
    ## For example we can do something like this
    ### testbst.insert(1).insert(2).insert(3)
    return self

  # Average O(Log(n)) time | space O(1)
  # Worst O(n) time | space O(1)
  def contains(self, value):
    currentNode = self
    while currentNode is not None:
      if value < currentNode.value
        currentNode = currentNode.left
      elif value > currentNode.value
        currentNode = currentNode.right
      else
        return True
    return False


  def remove(self, value, parentNode = None):
    pass
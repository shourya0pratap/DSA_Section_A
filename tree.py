class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def insert(root,newNode):
    q = []
    q.append(root)
    while q:
        topNode = q.pop(0)
        if topNode.left is None:
            topNode.left = newNode
            return
        else:
            q.append(topNode.left)
        if topNode.right is None:
            topNode.right = newNode
            return
        else:
            q.append(topNode.right)

def preOrderTraversal(root):
    print(root.data)
    if root.left is not None:
        preOrderTraversal(root.left)
    if root.right is not None:
        preOrderTraversal(root.right)
        
def printLevelOrder(root):
    if not root:
        return

    q = [root]
    
    while q:
        # 1. Determine how many nodes are at the current level
        level_size = len(q)
        
        # 2. Process all nodes belonging to this specific level
        for _ in range(level_size):
            currentNode = q.pop(0)
            
            # Print the node on the same line
            print(currentNode.data, end=" ")
            
            # Add children to the queue for the next level
            if currentNode.left:
                q.append(currentNode.left)
            if currentNode.right:
                q.append(currentNode.right)
        
        # 3. Once the inner loop finishes, the level is done
        print() # Print a newline

root = TreeNode(0)
n = int(input("Enter size of tree: "))
for i in range(1 , n):
    newNode = TreeNode(i)
    insert(root,newNode)
printLevelOrder(root)
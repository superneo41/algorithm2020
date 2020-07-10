# 106. Construct Binary Tree from Inorder and Postorder Traversal
def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
	def helper(in_left, in_right):
		if in_left > in_right:
			return None

		val = postorder.pop()

		root = TreeNode(val)

		index = index_map[val]

		# construct right first
		root.right = helper(index+1, in_right)
		root.left = helper(in_left, index-1)
		return root
	index_map = {val:index for index, val in enumerate(inorder)}
	return helper(0, len(postorder)-1)

# 105. Construct Binary Tree from Preorder and Inorder Traversal
def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
	def helper(in_left, in_right):
		if in_left > in_right:
			return None

		val = preorder.pop(0)
		index = index_map[val]
		root = TreeNode(val)

		root.left = helper(in_left, index-1)
		root.right = helper(index+1, in_right)
		return root

	index_map = {val:index for index, val in enumerate(inorder)}
	return helper(0,len(inorder)-1)

# 116. Populating Next Right Pointers in Each Node
def connect(self, root: 'Node') -> 'Node':
    def dfs(root):
        if not root:
            return
        if root.left:
            root.left.next = root.right
        if root.right and root.next:
            root.right.next = root.next.left
        dfs(root.left)
        dfs(root.right)
    dfs(root)
    return root

# bfs
# level order traverse, then connect the node

# 236. Lowest Common Ancestor of a Binary Tree
# postorder traverse
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
	def dfs(root)
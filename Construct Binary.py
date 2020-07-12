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
# dfs
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
	# use left, mid, right boolean,
	# if left + mid + right >= 2, return the root as ans

	def dfs(root):
		if not root:
			return False

		left = dfs(root.left)
		right = dfs(root.right)

		mid = (root == p or root == q)
		if left + right + mid >= 2:
			ans.self = root
		return left or right or mid

	self.ans = None
	dfs(root)
	return self.ans

# bfs
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
	# construct a parent dictionary for each node
	# construct a ancestor set for p
	# traverse q and q's ancestor find common node in p's ancestor set
	if not root:
		return None

	stack = [root]
	parent ={root: None}
	while stack:
		node = stack.pop()
		if node.left:
			parent[node.left] = node
			stack.append(node.left)
		if node.right:
			parent[node.right] = node
			stack.append(node.right)

	ancestor = set()
	while p:
		ancestor.add(p)
		p = parent[p]
	while q:
		if q in ancestor:
			return q
		else:
			q = parent[q]
	return None


#297. Serialize and Deserialize Binary Tree
# dfs
	# 	1
	# 2		 3
	# 		4  5

def serialize(self, root):
	self.ans = []
	def dfs(root):
		if not root:
			self.ans.append("null")
			return 
		self.ans.append(root.val)
		dfs(root.left)
		dfs(root.right)

	dfs(root)
	return ",".join(str(i) for i in self.ans)

def deserialize(self, data):
	def helper(l):
		if l[0] == "null":
			l.pop(0)
			return None
		root = TreeNode(l.pop(0))
		root.left = helper(l)
		root.right = helper(l)
		return root
	l = data.split(",")
	return helper(l)

# bfs
def serailize(root):
	if not root:
		return None
	ans = []
	q = [root]
	while q:
		ans.extend(q)
		next_q = []
		for node in q:
			if not node:
				continue
			next_q.extend([node.left, node.right])
		q = next_q
	while ans and ans[-1] == None:
		ans.pop()
	return ",".join([str(node.val) if node else 'null' for node in ans])

def deserialize(data):
	if not data:
		return None
	l = data.split(",")
	root = TreeNode(l.pop(0))
	q = [root]
	while l:
		next_q = []
		for node in q:
			if not node:
				continue
			if not l:
				break
			left = l.pop(0)
			node.left = TreeNode(left) if left != 'null' else None
			next_q.append(node.left)
			if not l:
				break
			right = l.pop(0)
			node.right = TreeNode(right) if right != 'null' else None
			next_q.append(node.right)
		q = next_q
	return root


# 4 types of tree traverse in both DFS and BFS

'''
	   1
	2      3
  4   5

(a) Inorder (Left, Root, Right) : 4 2 5 1 3
(b) Preorder (Root, Left, Right) : 1 2 4 5 3
(c) Postorder (Left, Right, Root) : 4 5 2 3 1
(d) levelOrder: [[1], [2,3],[4,5]]
'''

# Inorder
# dfs
def InorderTraverse(self, root):
	def dfs(root):
		if root == None:
			return
		dfs(root.left)
		ans.append(root.val)
		dfs(root.right)

	ans = []
	dfs(root)
	return ans

# bfs
def InorderTraverseBFS(self, root):
	stack = []
	ans = []
	cur = root
	while stack or cur != None:
		while cur != None:
			stack.append(cur)
			cur = cur.left
		cur = stack.pop()
		ans.append(cur.val)
		cur = cur.right
	return ans


# preorder
# dfs
def preorderTraverse(self, root):
	def dfs(root):
		if not root:
			return
		ans.append(root.val)
		dfs(root.left)
		dfs(root.right)
	ans = []
	dfs(root)
	return ans

# bfs
def preorderTraverseBFS(self, root):
	stack = []
	ans = []
	cur = root
	while cur or stack:
		while cur:
			ans.append(cur.val)
			stack.append(cur)
			cur = cur.left
		cur = stack.pop()
		cur = cur.right
	return ans


# postorder
# dfs
def postorderTraverse(self, root):
	def dfs(root):
		if not root:
			return
		dfs(root.left)
		dfs(root.right)
		ans.append(root.val)
	ans = []
	dfs(root)
	return ans

# bfs
# do reverse right preorder, 13254 => 45231
def postorderTraverseBFS(self,root):
	stack = []
	ans = []
	cur = root
	while cur or stack:
		while cur:
			ans.append(cur.val)
			stack.append(cur)
			cur = cur.right
		cur = stack.pop()
		cur = cur.left
	return ans[::-1]
# cutting the leaves
def postorderTraverseBFS2(self, root):

	ans = []
	cur = root
	stack = [cur]
	while stack:
		node = stack[-1]
		if not node.left and not node.right:
			ans.append(node.val)
			stack.pop()
		else:
			if node.right:
				stack.append(node.right)
				node.right = None
			if node.left:
				stack.append(node.left)
				node.left = None
	return ans

# level order traverse
# dfs
def levelOrder(self, root):
	def dfs(root,level):
		if not root:
			return
		if level not in levels:
			levels[level] = [root.val]
		else:
			levels[level].append(root.val)
		dfs(root.left, level+1)
		dfs(root.right, level+1)

	levels = {}
	dfs(root, 0)
	ans = []
	for i in range(len(levels)):
		ans.append(levels[i])
	return ans

# bfs
def levelOrderBFS(self, root):
	if not root:
		return []

	queue = [root]
	levels = []
	while queue:
		level = []
		for i in range(len(queue)):
			node = queue.pop(0)
			level.append(node.val)
			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)
		levels.append(level)
	return levels

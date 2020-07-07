# Tree problems

# 104. Maximum Depth of Binary Tree
# dfs
def maxDepth(self, root: TreeNode) -> int:
	if not root:
		return 0

	ans = 1
	def dfs(root, level):
		if not root:
			return
		
		nonlocal ans
		ans = max(ans, level)
		dfs(root.left, level+1)
		dfs(root.right, level+1)
	dfs(root,1)
	return ans

# bfs
def maxDepth(self, root: TreeNode) -> int:
	if not root:
		return 0
	levels = [(1, root)]
	ans = 1
	while levels:
		pair = levels.pop()
		level = pair[0]
		node = pair[1]
		ans = max(ans, level)
		if node.left:
			levels.append((level+1,node.left))
		if node.right:
			levels.append((level+1,node.right))
	return ans



# 101. Symmetric Tree
# dfs
def isSymmetric(self, root):
	def helper(left,right):
		if not left and not right:
			return True
		if not left or not right:
			return False
		return (left.val == right.val) and helper(left.left,right.right) and helper(left.right,right.left)

	if not root:
		return True
	return helper(root.left,root.right)

# bfs
# preorder traverse left and right, see if equals
def isSymmetric(self, root):
	left = [root]
	right = [root]
	while left and right:
		l = left.pop()
		r = right.pop()
		if not l and not r:
			continue
		if not l or not r:
			return False
		if l.val != r.val:
			return False
		left.append(l.left)
		right.append(r.right)
		left.append(l.right)
		right.append(r.left)
	return True


# 112. Path Sum
# dfs
def hasPathSum(self, root, sum):
	if not root:
		return False

	if not root.left and not root.right:
		return sum == root.val
	return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)
# bfs
# stack store (node, value remaining)
def hasPathSum(self, root, sum):

	if not root:
		return False
	stack = [(root,sum-root.val)]
	while stack:
		item = stack.pop()
		node = item[0]
		val = item[1]
		if node.left:
			stack.append((node.left, val-node.left.val))
		if node.right:
			stack.append((node.right, val-node.right.val))
		if not node.left and not node.right and val == 0:
			return True
	return False

# 250. Count Univalue Subtrees
# 1 n2
def countUnivalSubtrees(self, root):
	def isUniSubtree(root):
		if not root:
			return True
		if root.left and root.left.val != root.val:
			return False
		if root.right and root.right.val != root.val:
			return True
		return isUniSubtree(root.left) and isUniSubtree(root.right)

	def dfs(root):
		if not root:
			return
		if isUniSubtree(root):
			self.count += 1
		dfs(root.left)
		dfs(root.right)
	self.count = 0
	dfs(root)
	return self.count

# 2 count the number during isUniSubtree
def countUnivalSubtrees(self, root):
	def isUniSubtree(root):
		if not root.left and not root.right:
			self.count += 1
			return True

		isUni = True
		if root.left:
			isUni = isUniSubtree(root.left) and isUni and root.val == root.left.val
		if root.right:
			isUni = isUniSubtree(root.right) and isUni and root.val == root.right.val

		self.count += isUni
		return isUni 
	self count = 0
	if not root:
		return 0
	isUniSubtree(root)
	return self.count


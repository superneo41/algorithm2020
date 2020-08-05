# TOP 100
# 5. Longest Palindromic Substring
# brute force
def longestPalindrome(self, s: str) -> str:
    def isPalindromic(sub: str):
        sub_reversed = sub[::-1]
        return sub_reversed == sub
    
    ans = ""
    max_length = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if j-i > max_length and isPalindromic(s[i:j]):
                max_length = j - i
                ans = s[i:j]
    return ans

# expand from center
def longestPalindrome(self, s: str) -> str:
    def P(s,l,r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
    
    ans = ""
    for i in range(len(s)):
        temp = P(s,i,i)
        if len(temp) > len(ans):
            ans = temp
        temp = P(s,i,i+1)
        if len(temp) > len(ans):
            ans = temp
    return ans


# 15. 3Sum
def threeSum(self, nums: List[int]) -> List[List[int]]:
    # sort array
    nums.sort()
    
    # two pointer
    n = len(nums)
    ans = []
    for i in range(n):
        l = i + 1
        r = n - 1
        if i > 0 and nums[i] == nums[i-1]:
            continue
        while l < r:
            if nums[l] + nums[r] + nums[i] == 0:
                ans.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                while nums[l] == nums[l-1] and l < r:
                    l += 1
                
            elif nums[l] + nums[r] + nums[i] < 0:
                l += 1
            else:
                r -= 1
    return ans


# 17. Letter Combinations of a Phone Number
def letterCombinations(self, digits: str) -> List[str]:
	phone = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
	digits_str = []
	for i in digits:
		digits_str.append(phone[i])

	ans = []
	def helper(component, digits_str):
		if not digits_str:
			ans.append(component)
		else:
			for i in digits_str[0]:
				helper(component+i, digits_str[1:])

	helper("", digits_str)
	return ans



# 19. Remove Nth Node From End of List
# 2 pass
def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
	# get size
	cur = head
	size = 0
	while cur:
		size += 1
		cur = cur.next

	# iter to i-1 th node
	ith = size - n
	# if ith == 0, remove first node
	if ith == 0:
		return head

	cur = head
	for i in range(ith-1):
		cur = cur.next

	cur.next = cur.next.next
	return head


# one pass
def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    # one pass
    dic = {}
    cur = head
    i = 0
    while cur:
        dic[i] = cur
        i += 1
        cur = cur.next
    
    ith = len(dic) - n
    if ith == 0:
        return head.next
    dic[ith-1].next = dic[ith-1].next.next
    return head


# 20. Valid Parentheses
def isValid(self, s: str) -> bool:
    Parentheses = {"(":")","[":"]","{":"}"}
    stack = []
    for p in s:
        if p in {"(","[","{"}:
            stack.append(p)
        else:
            if not stack:
                return False
            if p != Parentheses[stack.pop()]:
                return False
    return len(stack) == 0


# 139. Word Break
# recursion with memo
def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    memo = {}
    def word_break(s,wordDict,start):
        if start == len(s):
            return True
        if start in memo:
            return memo[start]
        for end in range(start+1,len(s)+1):
            if s[start:end] in wordDict and word_break(s,wordDict,end):
                memo[start] = True
                return memo[start]
        memo[start] = False
        return memo[start]
    return word_break(s, set(wordDict), 0)

# bfs
def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    q = [s]
    seen = set()
    while q:
        s = q.pop(0)
        for i in wordDict:
            if s.startswith(i):
                new_s = s[len(i):]
                if new_s == "":
                    return True
                if new_s not in seen:
                    q.append(new_s)
                    seen.add(new_s)
    return False

# dp
def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    dp = [False] * (len(s)+1)
    dp[0] = True
    wordDict = set(wordDict)
    for r in range(1, len(s)+1):
        for l in range(0,r):
            if dp[l] and s[l:r] in wordDict:
                dp[r] = True
                break
    return dp[len(s)]
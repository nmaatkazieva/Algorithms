#https://leetcode.com/problems/evaluate-boolean-binary-tree/editorial/?source=submission-ac

import time
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def evaluate_recursion(self, root: Optional[TreeNode]) -> bool:
        result = False

        if root.val == 0:
            pass
        elif root.val == 1:
            result = True
        if root.val == 2:
            result = self.evaluate_recursion(root.left) or self.evaluate_recursion(root.right)
        elif root.val == 3:
            result = self.evaluate_recursion(root.left) and self.evaluate_recursion(root.right)

        return result 
    
    def evaluate_iterative(self, root: Optional[TreeNode]) -> bool:
        stack = [root]
        # key - TreeNode, value - boolean
        evaluated = {}

        while stack:
            top_node = stack[-1]
            if top_node.val in [0,1]:
                stack.pop()
                evaluated[top_node] = top_node.val == 1
                continue

            if top_node.left in evaluated and top_node.right in evaluated:
                stack.pop()
                if top_node.val == 2:
                    evaluated[top_node] = evaluated[top_node.left] or evaluated[top_node.right]
                elif top_node.val == 3:
                    evaluated[top_node] = evaluated[top_node.left] and evaluated[top_node.right]
            else:
                stack.append(top_node.left)
                stack.append(top_node.right)

        

        return evaluated[root] 

#root = TreeNode(1)
root = TreeNode(2,TreeNode(1),TreeNode(3,TreeNode(0),TreeNode(1)))
solution = Solution()
start_time = time.time()
result = solution.evaluate_iterative(root)
end_time = time.time()
print(result)
execution_time = (end_time - start_time)*1000
print(execution_time)


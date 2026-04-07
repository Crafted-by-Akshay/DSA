from typing import List

class SegmentNode:
    def __init__(self, total, L, R):
        self.sum = total
        self.L = L
        self.R = R
        self.left_child = None
        self.right_child = None

class SegmentTree:
    
    def __init__(self, nums: List[int]):
        self.root = self.build(nums, 0, len(nums) - 1)

    def build(self, nums, L, R):
        if L == R:
            return SegmentNode(nums[L], L, R)
        M = (L + R) // 2
        root = SegmentNode(0, L, R)
        root.left_child = self.build(nums, L, M)
        root.right_child = self.build(nums, M + 1, R)
        root.sum = root.left_child.sum + root.right_child.sum
        return root
    
    def update(self, index: int, val: int) -> None:
        self.update_helper(self.root, index, val)
    
    def update_helper(self, root, index: int, val: int) -> SegmentNode:
        if root.L == root.R:
            root.sum = val
            return root
        
        M = (root.L + root.R) // 2
        if index > M:
            root.right_child = self.update_helper(root.right_child, index, val)
        else:
            root.left_child = self.update_helper(root.left_child, index, val)
        root.sum = root.left_child.sum + root.right_child.sum
        return root
    
    def query(self, L: int, R: int) -> int:
        return self.query_helper(self.root, L, R)

    def query_helper(self, node, L: int, R: int) -> int:
        if node.L == L and node.R == R:
            return node.sum
        M = (node.L + node.R) // 2
        if L > M:
            return self.query_helper(node.right_child, L, R)
        elif R <= M:
            return self.query_helper(node.left_child, L, R)
        else:
            return (self.query_helper(node.left_child, L, M) + self.query_helper(node.right_child, M + 1, R))





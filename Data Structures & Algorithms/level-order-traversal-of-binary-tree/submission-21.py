# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        queue = [root]
        li = []

        i = 0
    
        while len(queue) != 0:
            temp_list = []
            add_to_queue = []
            for i in range(len(queue)):
                node = queue.pop(0)

                temp_list.append(node.val)
                
                if node.left:
                    add_to_queue.append(node.left)
                
                if node.right:
                    add_to_queue.append(node.right)
            
            li.append(temp_list)

            queue = add_to_queue
            
        return li



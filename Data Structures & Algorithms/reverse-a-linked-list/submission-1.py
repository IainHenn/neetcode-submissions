# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        temp = head
        values = []
        while temp is not None:
            values.append(temp.val)
            temp = temp.next

        # Reverse the array
        values = values[::-1]

        curr = None
        newHead = ListNode()
        for i in range(len(values)):
            if i == 0:
                newHead.val = values[i]
                newHead.next = None
                curr = newHead

            # Not the start
            else:
                newNode = ListNode()
                curr.next = newNode
                newNode.val = values[i]
                newNode.next = None
                curr = newNode
                
        
        return newHead
            


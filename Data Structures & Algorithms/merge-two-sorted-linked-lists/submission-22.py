# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    

        def link_list_to_list(linked_list):
            curr = linked_list
            arr = []

            while curr is not None:
                arr.append(curr.val)

                curr = curr.next
            
            return arr

        def generate_linked_list(arr):

            if len(arr) == 0 or arr is None:
                return None
            
            head = ListNode(arr[0])
            curr = head

            for i in range(1, len(arr)):
                curr.next = ListNode(arr[i])
                curr = curr.next
            
            return head
                    

        l1_arr = link_list_to_list(list1)
        l2_arr = link_list_to_list(list2)


        l_merged = l1_arr + l2_arr

        return generate_linked_list(sorted(l_merged))



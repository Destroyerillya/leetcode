from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result_list = ListNode()
        node = result_list

        while list1 or list2:
            node.next = ListNode()
            node = node.next
            if list1 and list2:
                if list1.val <= list2.val:
                    node.val = list1.val
                    list1 = list1.next
                else:
                    node.val = list2.val
                    list2 = list2.next
            elif not list1 and list2:
                node.val = list2.val
                list2 = list2.next
            elif list1 and not list2:
                node.val = list1.val
                list1 = list1.next
        result_list = result_list.next
        return result_list


class Solution2:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2

        if list1 or list2:
            cur.next = list1 if list1 else list2

        return dummy.next


list1 = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=4, next=None)))
list2 = ListNode(val=1, next=ListNode(val=3, next=ListNode(val=4, next=None)))
Solution2().mergeTwoLists(list1, list2)
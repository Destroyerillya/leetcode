from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    while head and head.next:
        if head.val == head.next.val:
            head = head.next
        else:
            head.next = deleteDuplicates(head.next)
            break
    return head


test_data = ListNode(1, ListNode(1, ListNode(2, ListNode(2, ListNode(3)))))

deleteDuplicates(test_data)
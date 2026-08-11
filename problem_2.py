from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list(arr):
    dummy = ListNode()
    curr = dummy
    for x in arr:
        curr.next = ListNode(x)
        curr = curr.next
    return dummy.next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = []
        carry = 0
        while (l1.next if l1 else None) or (l2.next if l2 else None):
            d1, d2 = l1.val if l1 else 0, l2.val if l2 else 0
            ans.append((d1 + d2 + carry) % 10)
            carry = (d1 + d2 + carry) // 10
            l1, l2 = l1.next if l1 else None, l2.next if l2 else None

        d1, d2 = l1.val if l1 else 0, l2.val if l2 else 0
        ans.append((d1 + d2 + carry) % 10)
        carry = (d1 + d2 + carry) // 10
        l1, l2 = l1.next if l1 else None, l2.next if l2 else None

        if carry:
            ans.append(carry)
        
        print(ans)
        return build_linked_list(ans)

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


if __name__ == "__main__":
    sol = Solution()

    l1 = build_linked_list([2, 4, 3])
    l2 = build_linked_list([5, 6, 4, 1])

    ans = sol.addTwoNumbers(l1, l2)

    assert linked_list_to_list(ans) == [7, 0, 8, 1]

    assert linked_list_to_list(sol.addTwoNumbers(
        build_linked_list([0]),
        build_linked_list([0])
    )) == [0]

    assert linked_list_to_list(sol.addTwoNumbers(
        build_linked_list([9,9,9,9,9,9,9]),
        build_linked_list([9,9,9,9])
    )) == [8,9,9,9,0,0,0,1]

    print("All tests passed!")
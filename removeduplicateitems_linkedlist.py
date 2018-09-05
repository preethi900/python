#Remove duplicate items

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head:
            current = head
            while current.next:
                if current.next.val == current.val:
                    current.next = current.next.next
                else:
                    current = current.next
        return head

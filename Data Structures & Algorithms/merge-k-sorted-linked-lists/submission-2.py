class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        values=[]

        for lst in lists:
            current=lst

            while current:
                values.append(current.val)
                current=current.next
        
        values.sort()

        dummy=ListNode()
        current=dummy
        for val in values:
            current.next= ListNode(val)
            current=current.next
        return dummy.next
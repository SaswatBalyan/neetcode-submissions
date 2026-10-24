class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldtocopy={None:None}
        cur = head
        while cur:
            copy=Node(cur.val)
            oldtocopy[cur]=copy
            cur=cur.next
        cur = head
        while cur:
            copy=oldtocopy[cur]
            copy.next=oldtocopy[cur.next]
            copy.random=oldtocopy[cur.random]
            cur=cur.next
        return oldtocopy[head]
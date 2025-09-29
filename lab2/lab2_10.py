class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def findMaxSum(n: int, head: ListNode) -> int:
    s = 0
    m = float('-inf')
    while head:
        s += head.val
        if s > m:
            m = s
        if s < 0:
            s = 0
        head = head.next
    return m

n = int(input())
a = list(map(int, input().split()))
head = ListNode(0)
tail = ListNode(0)

for i in range(n):
    tmp = ListNode(a[i])
    if i == 0:
        head = tmp
        tail = tmp
    else:
        tail.next = tmp
        tail = tmp

print(findMaxSum(n, head))

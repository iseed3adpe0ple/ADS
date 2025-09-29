


class Node(object):
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: Node = next


def insert(head: Node, node: Node, p: int):  # return new head of linked list
    if p == 0:
        node.next = head
        head = node
        return head
    current = head
    for _ in range(p-1):
        current = current.next
    node.next = current.next
    current.next = node

    return head

# write your code here

def remove(head: Node, p: int):  # return new head of linked list
    if p == 0:
        return head.next
    current = head
    for _ in range(p-1):
        current = current.next
    current.next = current.next.next
    return head

# write your code here

def printAll(head: Node):  # void function
    current = head
    while current:
        print(current.val, end=' ')
        current = current.next

# write your code here

def replace(head: Node, p1: int, p2: int):  # return new head of linked list
    current = head
    if p1 == p2:
        return head
    if p1 == 0:
        node = Node(head.val)
        head = head.next
    else:
        for _ in range(p1-1):
            current = current.next
        node = Node(current.next.val)
        current.next = current.next.next
    prev = head
    if p2 == 0:
        node.next = head
        head = node
        return head
    for _ in range(p2-1):
        prev = prev.next
    node.next = prev.next
    prev.next = node
    return head



# write your code here

def reverse(head: Node):  # return head of new linked list

    prev = None
    current = head
    while current:
        node = Node(current.val)
        node.next = prev
        prev = node
        current = current.next
    return prev


# write your code here

def cyclic_left(head: Node, x: int):  # return new head of linked list
    if x == 0:
        return head

    # for _ in range(x):
    #     node = head
    #
    #     head = head.next
    #     node.next = None
    #     current = head
    #     while current.next:
    #         current = current.next
    #     current.next = node
    # return head

    prev = head
    l = 1
    while prev.next:
        l += 1
        prev = prev.next
    x = x%l
    if x == 0:
        return head
    new_tail = head
    for _ in range(x-1):
        new_tail = new_tail.next
    new_head = new_tail.next
    new_tail.next = None
    prev.next = head

    return new_head




# write your code here

def cyclic_right(head: Node, x: int):  # return new head of linked list
    if x == 0:
        return head


    # prev = head
    # l = 1
    # while prev.next:
    #     l += 1
    #     prev = prev.next
    # x = x%l
    # if x == 0:
    #     return head
    # new_tail = head
    # for _ in range(x-1):
    #     new_tail = new_tail.next
    # new_head = new_tail.next
    # new_tail.next = None
    # prev.next = head


    head = reverse(head)
    head = cyclic_left(head, x)
    head = reverse(head)

    return head

# write your code here


head: Node = None

while (True):
    vals = [int(i) for i in input().split()]
    if (vals[0] == 0):
        break
    elif (vals[0] == 1):
        head = insert(head, Node(vals[1]), vals[2])
    elif (vals[0] == 2):
        head = remove(head, vals[1])
    elif (vals[0] == 3):
        printAll(head)
    elif (vals[0] == 4):
        head = replace(head, vals[1], vals[2])
    elif (vals[0] == 5):
        head = reverse(head)
    elif (vals[0] == 6):
        head = cyclic_left(head, vals[1])
    elif (vals[0] == 7):
        head = cyclic_right(head, vals[1])
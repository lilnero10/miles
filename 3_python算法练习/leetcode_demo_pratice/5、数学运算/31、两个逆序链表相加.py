class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0

    while l1 is not None or l2 is not None:
        x = l1.val if l1 is not None else 0
        y = l2.val if l2 is not None else 0
        total = carry + x + y
        carry = total // 10
        current.next = ListNode(total % 10)
        current = current.next

        if l1 is not None:
            l1 = l1.next
        if l2 is not None:
            l2 = l2.next

    if carry > 0:
        current.next = ListNode(carry)

    return dummy_head.next

    #  Python 列表转换为链表
def list_to_listnode(lst):
    dummy = ListNode()
    current = dummy
    for value in lst:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

# 链表转换为 Python 列表
def listnode_to_list(node):
    lst = []
    while node:
        lst.append(node.val)
        node = node.next
    return lst

# 创建两个链表 l1 = [2,4,3] 和 l2 = [5,6,4]
l1 = list_to_listnode([2, 4, 3])
l2 = list_to_listnode([5, 6, 4])
result = addTwoNumbers(l1, l2)
print(listnode_to_list(result))

# 打印列表中的节点值
# def printList(node):
#     while node:
#         print(node.val, end=" ")
#         node = node.next
#     print()
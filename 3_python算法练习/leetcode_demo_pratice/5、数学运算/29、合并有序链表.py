"""
chatgpt写的，有些逻辑还没看懂（2024年7月11日）
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1, l2):
    # 创建一个哑节点，作为结果链表的头部
    dummy = ListNode()
    # 创建一个指针指向哑节点，用于遍历结果链表
    current = dummy

    # 遍历两个链表，直到其中一个链表为空
    while l1 and l2:
        # 比较两个链表当前节点的值，将较小的节点接入结果链表，并向后移动对应的链表指针
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        # 移动结果链表指针
        current = current.next

    # 剩余未遍历完的链表接入结果链表
    if l1:
        current.next = l1
    else:
        current.next = l2

    # 返回哑节点的下一个节点，即合并后的链表头部
    return dummy.next


# List转ListNode方法
def list_to_listnode(lst):
    dummy = ListNode()
    current = dummy
    for value in lst:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


# ListNode转List方法
def listnode_to_list(node):
    lst = []
    while node:
        lst.append(node.val)
        node = node.next
    return lst

# 测试用例
l1 = list_to_listnode([1, 2, 4])
l2 = list_to_listnode([1, 3, 4])
merged_list = mergeTwoLists(l1, l2)
print(listnode_to_list(merged_list))


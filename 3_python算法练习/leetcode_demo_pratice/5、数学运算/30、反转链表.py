class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: ListNode) -> ListNode:
    prev = None
    curr = head

    while curr:
        next_temp = curr.next  # 暂存下一个节点
        curr.next = prev  # 当前节点的 next 指向前一个节点
        prev = curr  # 移动 prev 指针
        curr = next_temp  # 移动 curr 指针

    return prev  # prev 最终会指向新的头节点

def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# 输入链表
input_list = [1, 2, 3, 4, 5]
head = build_linked_list(input_list)
# 反转链表
reversed_head = reverseList(head)
# 输出反转后的链表
output_list = linked_list_to_list(reversed_head)
print(output_list)  # 输出: [5, 4, 3, 2, 1]
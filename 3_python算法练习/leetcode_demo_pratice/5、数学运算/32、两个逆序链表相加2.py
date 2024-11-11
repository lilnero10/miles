class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


    def reverseList(self, head):
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre


    def addTwo(self, l1, l2):
        cur = dummy = ListNode()  # 哨兵节点
        carry = 0  # 进位
        while l1 or l2 or carry:  # 有一个不是空节点，或者还有进位，就继续迭代
            if l1: carry += l1.val  # 节点值和进位加在一起
            if l2: carry += l2.val  # 节点值和进位加在一起
            cur.next = ListNode(carry % 10)  # 每个节点保存一个数位
            carry //= 10  # 新的进位
            cur = cur.next  # 下一个节点
            if l1: l1 = l1.next  # 下一个节点
            if l2: l2 = l2.next  # 下一个节点
        return dummy.next  # 哨兵节点的下一个节点就是头节点


    def addTwoNumbers(self, l1, l2):
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)  # l1 和 l2 反转后，就变成【2. 两数相加】了
        l3 = self.addTwo(l1, l2)
        return self.reverseList(l3)  # 计算完毕后再反转

# Helper functions to create a linked list from a list and vice versa
def list_to_listnode(lst):
    dummy = ListNode()
    current = dummy
    for value in lst:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

def listnode_to_list(node):
    lst = []
    while node:
        lst.append(node.val)
        node = node.next
    return lst

# Create two linked lists l1 = [7, 2, 4, 3] and l2 = [5, 6, 4]
l1 = list_to_listnode([7, 2, 4, 3])
l2 = list_to_listnode([5, 6, 4])

# Create an instance of ListNode and use addTwoNumbers method
ln = ListNode()
result = ln.addTwoNumbers(l1, l2)

print(listnode_to_list(result))

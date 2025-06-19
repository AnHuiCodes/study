# 下面是使用 Python 实现 K 个一组翻转链表的代码，代码中包含详细的注释以便理解算法逻辑。

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseKGroup(head: ListNode, k: int) -> ListNode:
    # 创建一个哑节点作为头节点的前一个节点
    dummy = ListNode(0)
    dummy.next = head
    prev_group_end = dummy  # 上一组的尾节点

    while True:
        # 检查剩余节点是否有k个
        group_start = prev_group_end.next  # 当前组的头节点
        kth_node = find_kth_node(group_start, k)

        if not kth_node:
            break  # 不足k个节点，退出循环

        next_group_start = kth_node.next  # 下一组的头节点

        # 翻转当前组的k个节点
        reversed_head = reverse_list(group_start, k)

        # 连接上一组和当前翻转后的组
        prev_group_end.next = reversed_head
        group_start.next = next_group_start  # 当前组的原头节点变为尾节点，连接到下一组

        # 更新prev_group_end为下一组的前一个节点
        prev_group_end = group_start

    return dummy.next


def find_kth_node(node: ListNode, k: int) -> ListNode:
    """找到从node开始的第k个节点，如果不足k个则返回None"""
    current = node
    while current and k > 1:
        current = current.next
        k -= 1
    return current


def reverse_list(head: ListNode, k: int) -> ListNode:
    """翻转前k个节点，返回新的头节点"""
    prev = None
    current = head
    while current and k > 0:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
        k -= 1
    return prev


# 辅助函数：将列表转换为链表
def list_to_linkedlist(lst):
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


# 辅助函数：将链表转换为列表
def linkedlist_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


# 测试示例
if __name__ == "__main__":
    # 示例输入: 1->2->3->4->5, k=2
    head = list_to_linkedlist([1, 2, 3, 4, 5])
    k = 2
    reversed_head = reverseKGroup(head, k)
    print(linkedlist_to_list(reversed_head))  # 输出: [2, 1, 4, 3, 5]

    # 测试k=3的情况
    head = list_to_linkedlist([1, 2, 3, 4, 5])
    k = 3
    reversed_head = reverseKGroup(head, k)
    print(linkedlist_to_list(reversed_head))  # 输出: [3, 2, 1, 4, 5]

'''
算法思路：
1、分组遍历：每次找到 K 个节点的组，如果剩余节点不足 K 个则不翻转。
2、组内翻转：对每个 K 节点组进行链表翻转操作。
3、连接各组：将翻转后的组与前后组正确连接，确保链表连续性。
关键点解释：
1、哑节点：用于简化边界处理，避免对头节点的特殊处理。
2、组的首尾节点：通过指针操作维护上一组的尾节点和当前组的头节点，确保翻转后正确连接。
3、组内翻转：使用迭代方法翻转链表，限制翻转次数为 K，确保不影响后续节点。

这个算法的时间复杂度是 O (n)，其中 n 是链表的长度，因为每个节点最多被遍历两次（一次查找 K 节点，一次翻转）。空间复杂度是 O (1)，只需要常数级的额外空间。
'''

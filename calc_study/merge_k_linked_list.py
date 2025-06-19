# 以下是合并有序链表的 Python 实现，包含递归和迭代两种方法：

# 方法一：递归实现
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    # 递归终止条件：其中一个链表为空
    if not l1:
        return l2
    if not l2:
        return l1

    # 比较当前节点值，选择较小的节点作为头节点
    if l1.val <= l2.val:
        l1.next = mergeTwoLists(l1.next, l2)  # 递归合并剩余部分
        return l1
    else:
        l2.next = mergeTwoLists(l1, l2.next)  # 递归合并剩余部分
        return l2


# 方法二：迭代实现（双指针）
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    # 创建哑节点和当前指针
    dummy = ListNode(-1)
    current = dummy

    # 双指针遍历两个链表
    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next  # 移动当前指针

    # 处理剩余节点
    current.next = l1 if l1 else l2

    return dummy.next


# 辅助函数（测试用）
# 列表转链表
def list_to_linkedlist(lst):
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


# 链表转列表
def linkedlist_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


# 测试示例
if __name__ == "__main__":
    # 示例输入: l1=[1,2,4], l2=[1,3,4]
    l1 = list_to_linkedlist([1, 2, 4])
    l2 = list_to_linkedlist([1, 3, 4])

    # 递归方法
    merged_recursive = mergeTwoLists(l1, l2)
    print(linkedlist_to_list(merged_recursive))  # 输出: [1,1,2,3,4,4]

    # 迭代方法
    l1 = list_to_linkedlist([1, 2, 4])  # 重新创建链表，因为递归方法已修改原链表
    l2 = list_to_linkedlist([1, 3, 4])
    merged_iterative = mergeTwoLists(l1, l2)
    print(linkedlist_to_list(merged_iterative))  # 输出: [1,1,2,3,4,4]

'''
算法解释
一、递归方法：
1、终止条件：当任一链表为空时，直接返回另一个链表。
2、递归逻辑：比较两个链表的当前节点，选择较小值的节点作为当前合并节点，并递归合并剩余部分。
3、时间复杂度：O (m+n)，其中 m 和 n 分别是两个链表的长度。
4、空间复杂度：O (m+n)（递归栈空间，最坏情况下每个节点递归一次）。
二、迭代方法：
1、哑节点：创建一个虚拟头节点，简化边界处理。
2、双指针：遍历两个链表，每次选择较小值的节点连接到结果链表。
3、剩余处理：任一链表遍历完后，直接连接另一个链表的剩余部分。
4、时间复杂度：O(m+n)。
5、空间复杂度：O (1)（只需要常数级额外空间）。

两种方法都能有效合并有序链表，迭代方法更节省空间，适合处理长链表。
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def list_to_linkedlist(lst: list) -> ListNode:
        dummy = ListNode(0)  # 创建哑节点
        current = dummy
        for i in lst:
            current.next = ListNode(i)
            current = current.next
        return dummy.next

    @staticmethod
    def linkedlist_to_list(linkedlist: ListNode) -> list:
        lst = []
        current = linkedlist
        while current:
            lst.append(current.val)
            current = current.next
        return lst

    @staticmethod
    def merge(lst1: ListNode, lst2: ListNode):
        if not any([lst1, lst2]):
            return None
        dummy = ListNode(-1)
        current = dummy
        while lst1 and lst2:
            if lst1.val <= lst2.val:
                current.next = ListNode(lst1.val)
                current = current.next
                current.next = ListNode(lst2.val)
                current = current.next
            else:
                current.next = ListNode(lst2.val)
                current = current.next
                current.next = ListNode(lst1.val)
                current = current.next
            lst1 = lst1.next
            lst2 = lst2.next
        current.next = lst1 if lst1 else lst2
        return dummy.next

    def mergeTwoLists(self):
        l1 = self.list_to_linkedlist([1, 2, 4])
        l2 = self.list_to_linkedlist([1, 3, 4])
        merge_linkedlist = self.merge(l1, l2)
        return self.linkedlist_to_list(merge_linkedlist)


if __name__ == '__main__':
    result = Solution().mergeTwoLists()
    print(result)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        head = dummy
        list1 = []
        list2 = []
        while l1 or l2:
            if l1:
                list1.append(l1.val)
                l1 = l1.next
            if l2:
                list2.append(l2.val)
                l2 = l2.next
        list1 = list1[::-1]
        list2 = list2[::-1]
        len1 = len(list1)
        len2 = len(list2)
        if len1 > len2:
            length = len1
        else:
            length = len2
        flag = 0
        res = 0
        list3 = []
        for i in range(0,length):
            sum1 = 0
            if i < len1:
                sum1 += list1[i]
            if i < len2:
                sum1 += list2[i]
            if flag == 1:
                sum1 = sum1 + res
                flag = 0
            if len(str(sum1)) > 1:
                temp = sum1
                sum1 = sum1%10
                res = temp//10
                flag = 1
            list3.append(sum1)
        if flag == 1:
            list3.append(res) 
        list3 = list3[::-1]
        for i in list3:
            dummy.next = ListNode(i)
            dummy = dummy.next
        return head.next



        
import random 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        list1 = []
        temp = self.head
        while self.head:
            list1.append(self.head.val)
            self.head = self.head.next
        self.head = temp
        n = len(list1)
        randIndex = random.randint(0, n-1) 
        return list1[randIndex]
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
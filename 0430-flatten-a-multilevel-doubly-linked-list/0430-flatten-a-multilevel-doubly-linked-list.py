"""# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child"""
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        list1 = []
        list2 = []
        list3 = []
        if head == None:
            return head
        while head != None:
            if head.child == None:
                list1.append(head.val)
                head = head.next
            else:
                list1.append(head.val)
                tail = head.next
                list2 = []
                while tail:
                    list2.append(tail.val)
                    tail = tail.next
                list2 = list2[::-1]
                list3.extend(list2)
                head = head.child
        list1.extend(list3[::-1])
        dummy = Node(list1[0]) 
        current = dummy
        for value in list1[1:]:
            new_node = Node(value)
            current.next = new_node  
            new_node.prev = current 
            current = current.next         
        return dummy


        
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l11 =""
        l12 =""
        for i in l1:
            l11= str(i)+l11
        for j in l2:
            l12= str(j) +l12

        out = int(l11) +int(l12) #807
        string = str(out)
        fin= []
        for k in string:
            fin.append(int(k))
        fin.reverse()
        return fin
obj=Solution()
print(obj.addTwoNumbers([2,4,3],[5,6,4]))
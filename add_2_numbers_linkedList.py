l1 = [2,3,5]
l2 = [4,7,2]

class Solution:
    def addTwoNumbers(self,l1,l2):
        resultList = curr = ListNode(0)
        carry = 0

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry +=l2.val
                l2 = l2.next

            curr.next = ListNode(carry%10)
            curr = curr.next
            carry = carry//10
        return resultList.next



s = Solution()
print(s.addTwoNumbers(l1,l2))


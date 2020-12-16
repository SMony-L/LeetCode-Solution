class ListNode:
    def __init__ (self, val = 0, next=None):
        self.val = val
        self.next = next
class Solution:
    def __init__(self):
        self.head = None

    def insertNode(self,data):
        newNode = ListNode(data)
        newNode.next = self.head
        self.head = newNode
    
    def addTwoNumbers(self, l1, l2):
        result = ListNode()
        current = result

        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            addVal = v1 + v2 + carry
            
            # carry = 1 if addVal > 10. Ex 15 // 10 = 1
            carry = addVal // 10
            # value = the sum % 10. Ex: 15 % 10 = 5
            addVal %= 10

            current.next = ListNode(addVal)
            current = current.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            # if this is the first node set it as head
            self.head = current if self.head is None else result.next
    
        return result.next
        
    def printLinkedList(self):
        curr = self.head
        while (curr):
            print(curr.val)
            curr = curr.next


firstList = Solution()
secondList = Solution()

firstList.insertNode(3)
firstList.insertNode(4)
firstList.insertNode(2)

firstList.printLinkedList()

secondList.insertNode(4)
secondList.insertNode(6)
secondList.insertNode(5)

secondList.printLinkedList()

res = Solution()
res.addTwoNumbers(firstList.head, secondList.head)
res.printLinkedList()
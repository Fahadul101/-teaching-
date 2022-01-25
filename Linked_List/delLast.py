class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        
def PrintList(head):
    curr = head
    while curr != None:
        print(curr.key)
        curr = curr.next 

        
def delLastNode(head):
    if head == None:
        return None
    if head.next == None:
        return None
    curr = head
    while curr.next.next != None:
        curr = curr.next
    curr.next = None
    return head            


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(60)
head = delLastNode(head)
print(PrintList(head))
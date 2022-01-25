class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        
def PrintList(head):
    cur = head
    while cur != None:
        print(cur.key)
        cur = cur.next 

def insertPos(head, data, pos):
    temp = Node(data)
    if pos == 1:
        temp.next = head
        return temp
    curr = head
    for i in range(pos-2):
        curr = curr.next
        if curr == None:
            return head
    temp.next = curr.next
    curr.next = temp
    return head                  

head = None
head = insertPos(head, 10, 1)
head = insertPos(head, 20, 2)
head = insertPos(head, 30, 3)
head = insertPos(head, 40, 4)
head = insertPos(head, 100, 3)
print(PrintList(head))
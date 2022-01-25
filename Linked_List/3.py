class LinkedList:
        def __init__(self):
                self.head=None

class Node:
        def __init__(self, data):
                self.data=data
                self.next=None


def addNumbers(head, array):
        newlist=LinkedList()        
        i=0                         
        prev=None                             
        temp=head
        while temp!=None:
                if(len(array)<=i):      
                        break
                if(array[i]%2!=0):          
                        node.next=None
                        if(i==0):          
                                node.next=temp
                                head=node
                        else:             
                                prev.next=node
                                node.next=temp
                                prev=node
                        i+=1
                else:
                        prev=temp
                        temp=temp.next
                        i+=1

        temp=head
        while temp!=None:            
                print(temp.data)
                temp=temp.next


n=int(input())      
array=[]
for i in range(n):
        array.append(int(input()))

temp=None

n=int(input())          
llist=LinkedList()          
for i in range(n):
        num=int(input())
        node=Node(num)      
        node.next=None       
        if i==0:
                llist.head=node
                temp=llist.head
        else:
                temp.next=node
                temp=temp.next
print("----------")
addNumbers(llist.head, array) 



# curr = head
#     for i in range(pos-2):
#         curr = curr.next
#         if curr == None:
#             return head
#     temp.next = curr.next
#     curr.next = temp
#     return head
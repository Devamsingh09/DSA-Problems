class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        
class SinglyLL:
    def __init__(self):
        self.head=None
    def append(self,val):
        new_node = Node(val)
        if self.head==None:
            self.head=new_node
        else:
            curr= self.head
            while curr.next!=None:
                curr = curr.next
            curr.next=new_node
    def traverse(self):
        if self.head==None:
            print("SLL is empty!")
        else:
            curr=self.head
            while curr!=None:
                print(curr.val,end = " ")
                curr = curr.next
    def inset_at(self,val,position):
        new_node=Node(val)
        if position==0:
            new_node.next=self.head
            self.head=new_node
        else:
            curr,count=self.head,0
            prev_node=None
            while curr is not None and count<position:
                prev_node=curr
                curr = curr.next
                count+=1
            new_node.next=curr
            prev_node.next=new_node
    def delete(self,val):
        
        if val==self.head.val:
            temp=self.head
            self.head=self.head.next
            del temp
        else:
            prev_node=None
            curr=self.head
            while curr.val!=val and curr.next!=None:
                prev_node=curr
                curr=curr.next
            prev_node.next=curr.next
            del curr
    
            
            
            
            
            
            
            
sll = SinglyLL()
sll.append(10)
sll.append(20)
sll.append(40)
sll.append(50)
sll.delete(40)
sll.traverse()

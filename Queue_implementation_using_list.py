class Queue:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items) == 0
    def enqueue(self,item):
        self.items.append(item)
    def dequeue(self,item):
        if len(self.items)==0:
            print("Cannot pop! Queue is empty.")
            return
        x=self.items.pop(0)
        return x
    def front(self):
        if len(self.items) == 0:
            print("Queue is empty!")
            return
        return self.items[0]
    def rear(self):
        if len(self.items) == 0:
            print("Queue is empty!")
            return
        return self.items[-1]
    def size(self):
        return len(self.items)
        
q = Queue()
q.enqueue(68)
q.enqueue(55)
q.enqueue(81)
q.enqueue(82)

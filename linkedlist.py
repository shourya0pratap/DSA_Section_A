class Node:
    def __init__(self, val):
        self.next=None
        self.val = val

class LinkedList:
    
    def __len__(self):
        n = 0
        curr = self.head
        while curr is not None:
            n += 1
            curr = curr.next
        return n

    def __init__(self):
        self.head = None
        
    def add(self,val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = newNode
            
    def remove(self, ind):
        if ind == 0:
            self.head = self.head.next
            return
        curr = self.head
        i = 0
        while(i<ind-1): 
            curr = curr.next
            i += 1
        curr.next = curr.next.next
        
    def elemAt(self, ind):
        curr = self.head
        i = 0
        while(i<ind): 
            curr = curr.next
            i += 1
        return curr.val

    def __str__(self):
        elements = []
        curr = self.head
        while curr:
            elements.append(str(curr.val))
            curr = curr.next
        return "[" + ", ".join(elements) + "]"

def main():
    lis = LinkedList()
    print(lis)
    for i in range(1,6):
        lis.add(i)
    print(lis)
    lis.remove(0)
    print(lis)
    print(len(lis))
    
if __name__ == "__main__":
    main()
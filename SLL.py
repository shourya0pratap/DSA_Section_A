class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class SLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def __str__(self):
        out = []
        curr = self.head
        while curr:
            out.append(str(curr.val))
            curr = curr.next
        return f"[{" , ".join(out)}]"
    def __len__(self):
        return self.size
    def insert(self, val, ind=None):
        if not ind:
            ind = self.size
        newNode = Node(val)
        if ind == 0:
            newNode.next = self.head
            self.head = newNode
            if self.size == 0:
                self.tail = newNode
        elif ind == self.size:
            self.tail.next = newNode
            self.tail = newNode
        else:
            curr = self.head
            for _ in range(ind-1):
                curr = curr.next
            newNode.next = curr.next
            curr.next = newNode
        self.size += 1
    def delete(self, ind=None):
        if not ind:
            ind = self.size-1
        if ind == 0:
            if self.size == 1:
                self.head = self.tail = None
        else:
            curr = self.head
            for _ in range(1,ind):
                curr = curr.next
            curr.next = curr.next.next
        self.size -= 1

def main():
    LL = SLL()
    for i in range(1, 6):
        LL.insert(i)
    print(LL)
    LL.delete()
    print(LL)

if __name__ == "__main__":
    main()
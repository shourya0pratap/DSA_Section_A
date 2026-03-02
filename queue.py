class QueueADT:
    def __init__(self):
        self.q = []
    
    def enqueue(self, elem):
        self.q.append(elem)
        
    def dequeue(self): 
        return "Underflow" if self.is_empty() else self.q.pop(0)
    
    def is_empty(self)->bool:
        return len(self.q) == 0

    def size(self)->int:
        return len(self.q)

    def display(self)->None:
        print(self.q)
        
    def clear(self):
        self.q.clear()
    
def main():
    q = QueueADT()
    for i in range(1,6):
        q.enqueue(i)
    q.display()
    print(q.dequeue())

if __name__ == "__main__":
    main()
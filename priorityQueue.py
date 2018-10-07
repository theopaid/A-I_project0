import heapq

class PriorityQueue:
    def __init__(self):
        self.items = []
        self.count = 0

    def isEmpty(self):
        if not self.items: #if theres nothing in 'items' list
            return True
        return False
    
    def push(self, item, priority):
        self.count += 1
        # The first variable inserted (priority), is the one responsible for the ordering 
        heapq.heappush(self.items, [priority,item])
        print(self.items)

    def pop(self):
        if self.isEmpty():
            print("Priority Queue is already empty!")
            return None
        self.count = self.count - 1
        return heapq.heappop(self.items)[1]

    def update(self, item, priority):
        counter = -1
        for i in self.items:
            counter = counter + 1
            if item == i[1]:
                if i[0] > priority:
                    self.items[counter][0] = priority
                    heapq.heapify(self.items)
                    print(self.items)
                    return None
                return None
        if counter + 1 == self.count:
            self.push(item, priority)
            print(self.items)

def PQSort(int_list):
    mypq = PriorityQueue()
    for value in int_list:
        mypq.push(value, value)
    return [mypq.pop() for i in range(mypq.count)]


#if __name__ == "__main__":
#    q = PriorityQueue()
#    q.push("task1", 1) 
#    q.push("task1", 2) 
#    q.push("task0", 0) 
#    t=q.pop() 
#    print(t) 
#    t=q.pop() 
#    print(t) 
#    q.push("task3", 3) 
#    q.push("task3", 4) 
#    q.push("task2", 0) 
#    t=q.pop()
#    print(t)
#    q.update("task4", 66)
#    print(PQSort([5,2,6,8,0,1,2,4]))
            

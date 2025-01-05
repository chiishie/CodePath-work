class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next
        
def count_racers(head):
    count = 0
    current = head
    while current:
        current = current.next
        count +=1
    
    return count

def last_place(head):
    current = head
    
    if current == None:
        return None
    else:
        while current.next:
            current = current.next
        
    return current.value

def remove(head, target):
    current = head
    prev = None
    
    if current is None:
        return head
    
    if target == 1:
        head = current.next
        return head
    
    for i in range(1, target):
        prev = current
        current = current.next
        
        if current is None:
            return head
        
    if current is not None:
        prev.next = current.next
        current.next = None
        return current
    

def increment_rank(head, target):
    current = head
    prev = None
    
    if current is None:
        return head
    
    if target == 1:
        head = current.next
        return head
    
    for i in range(1, target):
        prev = current
        current = current.next
        
        if current is None:
            return head
        
    if current is not None:
        prev.next = current.next
        current.next = None
        return current
    
    
    
racers1 = Node("Mario", Node("Peach", Node("Luigi", Node("Daisy"))))
racers2 = Node("Mario", Node("Luigi"))

print_linked_list(increment_rank(racers1, 3))
print_linked_list(increment_rank(racers2, 1))

daisy = Node("Daisy")
peach = Node("Peach")
luigi = Node("Luigi")
mario = Node("Mario")

daisy.next = peach
peach.next = luigi
luigi.next = mario

print_linked_list(daisy)

racers1 = Node("Mario", Node("Peach", Node("Luigi", Node("Daisy"))))
racers2 = Node("Mario")

print(count_racers(racers1))
print(count_racers(racers2))
print(count_racers(None))

racers1 = Node("Mario", Node("Peach", Node("Luigi", Node("Daisy"))))
racers2 = Node("Mario")

print(last_place(racers1)) 
print(last_place(racers2)) 
print(last_place(None))
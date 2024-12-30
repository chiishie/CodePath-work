def arrange_guest_arrival_order(arrival_pattern):
    n = len(arrival_pattern)
    guest_order = []
    stack = []

    for i in range(n + 1):
        stack.append(str(i + 1))
        if i == n or arrival_pattern[i] == 'I':
            while stack:
                guest_order.append(stack.pop())

    return ''.join(guest_order)
            
print(arrange_guest_arrival_order("IIIDIDDD"))  
print(arrange_guest_arrival_order("DDD"))  # Output: "1234"

def arrange_attendees_by_priority(attendees, priority):
    left = 0
    last = len(attendees) - 1
    i = 0
    
    while i <= last:
        if attendees[i] < priority:
            attendees[left], attendees[i] = attendees[i], attendees[left]
            left += 1
            i += 1
        elif attendees[i] > priority:
            attendees[last], attendees[i] = attendees[i], attendees[last]
            last -= 1
        else:
            i += 1
    return attendees

print(arrange_attendees_by_priority([9,12,5,10,14,3,10], 10)) 
print(arrange_attendees_by_priority([-3,4,3,2], 2)) 


def rearrange_guests(guests):
    above = []
    below = []
    res = []
    
    for i in guests:
        if i < 0:
            below.append(i)
            
    for i in guests:
        if i > 0:
            above.append(i)
            
    for i in range(len(above)):
        res.append(above[i])
        res.append(below[i])
    
    return res

print(rearrange_guests([3,1,-2,-5,2,-4]))  
print(rearrange_guests([-1,1]))

def min_changes_to_make_balanced(schedule):
    stack = []
    count = 0
    
    for i in schedule:
        if i is '(':
            stack.append(i)
        elif i is ')':
            if stack:
                stack.pop()
            else:
                count+=1
    
    return len(stack) + count

print(min_changes_to_make_balanced("())"))
print(min_changes_to_make_balanced("(((")) 
print(min_changes_to_make_balanced(")))")) 
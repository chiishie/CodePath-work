def count_suits_iterative(suits):
    count = 0
    for i in suits:
        count+=1
        
    return count

def count_suits_recursive(suits):
    
    
    if not suits:
        return 0
    else: 
        return 1 + count_suits_recursive(suits[1:])
    
print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III", "Mark IV"]))

def sum_stones(stones):
    
    count = 0
    
    if not stones:
        return 0
    else:
        return stones[0] + sum_stones(stones[1:])
    
print(sum_stones([5, 10, 15, 20, 25, 30]))
print(sum_stones([12, 8, 22, 16, 10]))
    
    

def count_suits_recursive(suits):
    if not suits:
        return 0
    if suits[0] in suits[1:]:
        return count_suits_recursive(suits[1:])
    else:
        return 1 + count_suits_recursive(suits[1:])

print(count_suits_recursive(["Mark I", "Mark I", "Mark IV"]))

def fibonacci_growth(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci_growth(n - 1) + fibonacci_growth(n - 2)

print(fibonacci_growth(5))
print(fibonacci_growth(8))
    
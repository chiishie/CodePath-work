def transpose(matrix):
    
    if not matrix or not matrix[0]:
        return []
    
    m = len(matrix)
    n = len(matrix[0])
    new_matrix = [[0 for x in range(m)] for y in range(n)]
    
    for i in range(m):
        for j in range(n):
            new_matrix[j][i] = matrix[i][j]
    
    return print(new_matrix)

def reverse_list(lst):
    p1 = 0
    p2 = len(lst) - 1
    temp = ""
    while p1 < p2:
        temp = lst[p1]   
        lst[p1] = lst[p2]
        lst[p2] = temp  
        p1+=1
        p2-=1
    
    return print(lst)
        
def remove_dupes(items):
    if not items:
        return 0
    
    i = 0  # Pointer for the position of the last unique element
    
    for j in range(1, len(items)):
        if items[j] != items[i]:
            i += 1
        items[i] = items[j]
    
    return print(i+1)

def sort_by_parity(nums):
    array = []
    count = 0
    for i in nums:
        if i % 2 == 0:
            array.append(i)
    
    for j in nums:
        if j % 2 != 0:
            array.append(j)
            
    return print(array)

def most_honey(height):
    left = 0
    right = len(height) - 1
    max_honey = 0
    
    while left < right:
        w = right - left
        h = min(height[left], height[right])
        a = w * h
        max_honey = max(max_honey, a)
        
        if height[left] < height[right]:
            left+=1
        else:
            right-=1
    
    return print(max_honey)
        
def add_matrices(matrix1, matrix2):
    n = len(matrix1)
    m = len(matrix1[0])
    new_matrix = [[0 for x in range (n)] for y in range (m)]
    
    for i in range(n):
        for j in range(m):
            new_matrix[i][j] = matrix1[i][j] + matrix2[i][j]
    
    return print(new_matrix)

def is_palindrome(s):
    p1 = 0
    p2 = len(s) -1
    
    while p1 < p2:
        if s[p1] == s[p2]:
            return print(True)
        p1+=1
        p2-=1
    return print(False)


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transpose(matrix)

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
transpose(matrix)

lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]
reverse_list(lst)

items = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
remove_dupes(items)

nums = [3, 1, 2, 4]
sort_by_parity(nums)

nums = [0]
sort_by_parity(nums)\


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
most_honey(height)

height = [1, 1]
most_honey(height)

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

add_matrices(matrix1, matrix2)

s = "winow"
is_palindrome(s)

s = "madam"
is_palindrome(s)

def squash_spaces(s):
    result = ""
    in_space = False
    
    for char in s:
        if char != " ":
            if in_space and result:
                result += " "
            result += char
            in_space = False
        else:
            in_space = True
    
    return print(result)
    

s = "   Up,     up,   and  away! "
squash_spaces(s)

s = "With great power comes great responsibility."
squash_spaces(s)
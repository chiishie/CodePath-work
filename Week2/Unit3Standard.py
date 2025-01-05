from collections import deque 


def is_valid_post_format(posts):
    brackets = {")": "(", "}": "{", "]": "["}
    
    stack = []
    for char in posts:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys():
            if stack and stack[-1] == brackets[char]:
                stack.pop()
            else:
                return False
    return len(stack) == 0

print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]"))

def reverse_comments_queue(comments):
    
    stack = []
    reversed_queue = []
    
    for comment in comments:
        stack.append(comment)
        
    while stack:
        reversed_queue.append(stack.pop())
    
    return reversed_queue

print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))

def is_symmetrical_title(title):
    
    clean_title = title.lower()
    left = 0
    right = len(clean_title) - 1
    
    while left < right:
        if clean_title[left] != clean_title[right]:
            return False
        left+=1
        right-=1
        return True
    
print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media"))
print(is_symmetrical_title("Madam, in Eden, I'm Adam"))  # True
print(is_symmetrical_title("Was it a car or a cat I saw"))  # True
print(is_symmetrical_title("No lemon, no melon"))  # True
print(is_symmetrical_title("Programming is fun")) 


def clean_post(post):
    stack = []
    
    for char in post:
        if char.islower():
            stack.append(char)
        if char.isupper() and stack[-1] == char.lower():
            stack.pop()
        
    return ''.join(stack)

print(clean_post("poOost")) 
print(clean_post("abBAcC")) 
print(clean_post("s")) 

def edit_post(post):
    
    post_list = post.split(" ")
    
    newWords = [word[::-1]for word in post_list]
    
    return " ".join(newWords)

print(edit_post("Boost your engagement with these tips")) 
print(edit_post("Check out my latest vlog")) 

def remove_space(s):
    
    stack = []
    
    for char in s:
        if char == "#":
            if stack:
                stack.pop()
        else:
            stack.append(char)
    
    return stack

def post_compare(draft1, draft2):
    return remove_space(draft1) == remove_space(draft2)

print(post_compare("ab#c", "ad#c"))
print(post_compare("ab##", "c#d#")) 
print(post_compare("a#c", "b"))


def manage_stage_changes(changes):
    stack = []
    l = []
    temp = ""
    
    for t in changes:
        if " " in t:
            temp = t.split(" ")
            l.append(temp[1])
        else:
            l.append(t)
    
    for i in l:
        if len(i) == 1:
            stack.append(i)
        elif i == "Cancel":
            temp = stack.pop()
        elif i == "Reschedule":
            stack.append(temp)
    
    return stack

def process_performance_requests(requests):
    
    max = 0
    queue = queue = deque(sorted(requests, reverse=True))
    result = []
    
    while queue:
        priority, perform = queue.popleft()
        result.append(perform)
    
    return result

def booth_navigation(clues):
    stack = []
    
    for c in clues:
        if stack and c == "back":
            stack.pop()
        elif not stack and c == "back":
            continue
        else:
            stack.append(c)
    
    return stack

def blueprint_approval(blueprints):
    
    queue = deque()
    
    for i in sorted(blueprints):
        queue.append(i)
    
    return list(queue)
    

print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 

print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))

clues = [1, 2, "back", 3, 4]
print(booth_navigation(clues)) 

clues = [5, 3, 2, "back", "back", 7]
print(booth_navigation(clues)) 

clues = [1, "back", 2, "back", "back", 3]
print(booth_navigation(clues)) 

print(blueprint_approval([3, 5, 2, 1, 4])) 
print(blueprint_approval([7, 4, 6, 2, 5])) 


def build_skyscrapers(floors):
    stack = []
    skyscrapers = 0

    for floor in floors:
        if not stack or stack[-1] >= floor:
            skyscrapers += 1
            stack.append(floor)
        else:
            while stack and stack[-1] < floor:
                stack.pop()
            stack.append(floor)

    return skyscrapers

# Example usage
print(build_skyscrapers([10, 5, 8, 3, 7, 2, 9]))  # Output: 4
print(build_skyscrapers([7, 3, 7, 3, 5, 1, 6]))  # Output: 4
print(build_skyscrapers([8, 6, 4, 7, 5, 3, 2]))
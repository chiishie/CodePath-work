def two_sum(nums, target):
    
    left = 0
    right = len(nums) - 1
    
    while left < right:
        sum = nums[left] + nums[right]
        
        if sum == target:
            return [left, right]
        elif sum < target:
            left+=1
        else: 
            right-=1

def three_sum(nums):
    res = []
    nums.sort()
    
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        j = i + 1
        k = len(nums) - 1
        
        while j < k:
            sum = nums[i] + nums[j] + nums[k]
            if sum == 0:
                res.append([nums[i], nums[j], nums[k]])
            
            while j < k and nums[j] == nums[j+1]:
                j+=1
            while j < k and nums[k-1] == nums[k]:
                k-=1
            
            j+=1
            k-=1
            if sum < 0:
                j+=1
            elif sum > 0:
                k-=1
    
    return print(res)
    
def words_with_char(words, x):
    
    res = []
    
    for i in range(len(words)):
        if x in words[i]:
            res.append(i)
    
    return print(res)


def hulk_smash(n):
    
    res = []
    
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            res.append("HulkSmash")
        elif i % 3 == 0 and i % 5 != 0:
            res.append("Hulk")
        elif i % 3 != 0 and i % 5 == 0:
            res.append("Smash")
        else:
            res.append(i)
    
    return print(res)

def shuffle(message, indices):
    
    res = [0] * len(message)
    count = 0
    
    for i in indices:
        res[i] = message[count]
        count+=1
    
    return print("".join(res))

nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))

nums = [2, 7, 11, 15]
target = 18
print(two_sum(nums, target))  

nums = [-1, 0, 1, 2, -1, -4]
three_sum(nums)

nums = [0, 1, 1]
three_sum(nums)

nums = [0, 0, 0]
three_sum(nums)

words = ["batman", "superman"]
x = "a"
words_with_char(words, x)

words = ["black panther", "hulk", "black widow", "thor"]
x = "a"
words_with_char(words, x)

words = ["star-lord", "gamora", "groot", "rocket"]
x = "z"
words_with_char(words, x)

n = 3
hulk_smash(n)

n = 5
hulk_smash(n)

n = 15
hulk_smash(n)

message = "evil"
indices = [3, 1, 2, 0]
shuffle(message, indices)

message = "findme"
indices = [0, 1, 2, 3, 4, 5]
shuffle(message, indices)



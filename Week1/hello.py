def welcome():
    print("Welcome to the Hundred Acre Wood!")
    
def print_catchphrase(character):
    if character == "Pooh":
        print("Oh bother")
    if character == "Tigger":
        print("TTFN: Ta-ta for now!")

def sum_honey(hunny_jars):
    sum = 0
    for i in hunny_jars:
        sum = sum + i
    return sum

hunny_jars = [2, 3, 4, 5]

def doubled(hunny_jars):
    for i in range (len(hunny_jars)):
        hunny_jars[i] = hunny_jars[i] *2
    return hunny_jars

def count_less_than(race_times, threshold): 
    count = 0
    for i in race_times:
        if i < threshold:
            count = count + 1
    return count
            

def print_todo_list(task):
    print("Pooh's To Dos")
    count = 1
    for tasks in task:
        print(str(count) + ". " + tasks)
        count+= 1

def can_pair(item_quantities):
    iseven = False
    for i in item_quantities:
        if i % 2 != 0:
            return False
    return True

def reverse_sentence(sentence):
    array = sentence.split()[::-1]
    new_array = []
    for i in array:
        new_array.append(i)
    return print(" ".join(new_array))
    
#1
def goldilocks_approved(nums):
    ans = 0
    for i in nums: 
        if i != min(nums) and i != max(nums): 
            ans = i
        if len(nums) < 3:
            ans = -1
    return print(ans)

#2
def delete_minimum_elements(hunny_jar):
    array = []
    while len(hunny_jar) != 0:
        array.append(min(hunny_jar))
        hunny_jar.remove(min(hunny_jar))
    
    return print(array)

def sum_of_digits(num):
    sum = 0
    i = num
    while i > 0:
        sum = sum + i % 10
        i  = int(i / 10)
    return print(sum)

def final_value_after_operations(operations):
    count = 1
    for i in operations:
        if i == "bouncy" or i == "flouncy":
            count+=1
        elif i == "trouncy" or i == "pouncy":
             count-=1
    return print(count)
    
#6

def is_acronym(words, s):
    l = list(s)
    
    if(len(words) != len(l)):
        return False
    
    for i in range (len(words)):
        if l[i] == words[i][0]:
            return True
    return False

#8

def exclusive_elemts(lst1, lst2):
    set1 = set(lst1)
    set2 = set(lst2)
    
    return print(list(set1.symmetric_difference(set2)))
    
#7

def make_divisible_by_3(nums):
    count = 0
    
    for i in nums:
        if i % 3 != 0:
            count+= 1
    
    return print(count)

#9

def merge_alternately(word1, word2):
    n = len(word1)
    m = len(word2)
    
    l = [n, m]
    
    s = ""
    for i in range(min(l)):
        s = s + word1[i] + word2[i]
        
    if n < m:
        s = s + word2[n:m]
    elif m < n:
        s = s + word1[m:n]
    
    return print(s)

#10

def good_pairs(pile1, pile2, k):
    count = 0
    for i in range(len(pile1)):
        for j in range(len(pile2)):
            if (pile1[i] % (pile2[j] * k)) == 0:
                count+= 1
    return print(count)

print(doubled(hunny_jars))

race_times = [1, 2, 3, 4, 5, 6]
threshold = 4
print(count_less_than(race_times, threshold))
task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
print_todo_list(task)

item_quantities = [2, 4, 6, 8]
print(can_pair(item_quantities))

item_quantities = [1, 2, 3, 4]
print(can_pair(item_quantities))

sentence = "tubby little cubby all stuffed with fluff"
reverse_sentence(sentence)

nums = [3, 2, 1, 4]
goldilocks_approved(nums)

nums = [1, 2]
goldilocks_approved(nums)

nums = [2, 1, 3]
goldilocks_approved(nums)

hunny_jar_sizes = [5, 3, 2, 4, 1]
delete_minimum_elements(hunny_jar_sizes)

hunny_jar_sizes = [5, 2, 1, 8, 2]
delete_minimum_elements(hunny_jar_sizes)

num = 423
sum_of_digits(num)

num = 4
sum_of_digits(num)

operations = ["trouncy", "flouncy", "flouncy"]
final_value_after_operations(operations)

operations = ["bouncy", "bouncy", "flouncy"]
final_value_after_operations(operations)

words = ["christopher", "robin", "milne"]
s = "crm"
print(is_acronym(words, s))

lst1 = ["pooh", "roo", "piglet"]
lst2 = ["piglet", "eeyore", "owl"]
exclusive_elemts(lst1, lst2)

lst1 = ["pooh", "roo"]
lst2 = ["piglet", "eeyore", "owl", "kanga"]
exclusive_elemts(lst1, lst2)

lst1 = ["pooh", "roo", "piglet"]
lst2 = ["pooh", "roo", "piglet"]
exclusive_elemts(lst1, lst2)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
make_divisible_by_3(nums)

nums = [3, 6, 9]
make_divisible_by_3(nums)

word1 = "wol"
word2 = "oze"
merge_alternately(word1, word2)

word1 = "hfa"
word2 = "eflump"
merge_alternately(word1, word2)

word1 = "eyre"
word2 = "eo"
merge_alternately(word1, word2)

pile1 = [1, 3, 4]
pile2 = [1, 3, 4]
k = 1
good_pairs(pile1, pile2, k)

pile1 = [1, 2, 4, 12]
pile2 = [2, 4]
k = 3
good_pairs(pile1, pile2, k)


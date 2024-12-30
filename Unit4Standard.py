def filter_meme_lengths(memes, max_length):
    
    res = []
    
    for meme in memes:
        if len(meme) <= max_length:
            res.append(meme)
        
    return res

def count_meme_creators(memes):
    
    count_map = {}
    
    for creators in memes:
        if creators["creator"] not in count_map:
            count_map[creators["creator"]] = 1
        else:
            count_map[creators["creator"]]+=1
    
    return count_map

def find_trending_memes(memes):
    
    map = {}
    res = []
    
    for meme in memes:
        if meme not in map:
            map[meme] = 1
        else:
            map[meme]+=1
            
    for key, value in map.items():
        if value > 1:
            res.append(key)
    
    return res

def reverse_memes(memes):
    left = 0
    right = len(memes) - 1
    temp = ""
    
    while left < right:
        temp = memes[left]
        memes[left] = memes[right]
        memes[right] = temp
        left+=1
        right-=1
    
    return memes

def find_task_pair(task_times, available_time):
    
    map = {}
    
    for times in task_times:
        diff = available_time - times
        if diff in map:
            return True
        
        map[times] = True
    
    return False

def convert_minutes(time):
    
    res = ((time//100)*60) + (time%100)
    
    return res

def find_smallest_gap(work_sessions):
    
    temp = float("inf")
    
    for i in range(1, len(work_sessions)):
        diff = convert_minutes(work_sessions[i][0]) - convert_minutes(work_sessions[i-1][1])

        temp = min(temp, diff)
        
    return temp
 
def calculate_expenses(expenses):
    
    map ={}
    temp = 0
    temp_s = ""
    
    for item in expenses:
        if item[0] not in map:
            map[item[0]] = item[1]
        else: 
            map[item[0]]+=item[1]
    
    for key, value in map.items():
        if value > temp:
            temp = value
            temp_s = key
        
    return (map, temp_s)

def word_frequency_analysis(text):
    text = text.lower()
    text_list = text.split(" ")
    temp = 0
    temp_s = ""
    map = {}
    for word in text_list:
        if word not in map:
            map[word] = 1
        else:
            map[word]+=1
    
    for key, value in map.items():
        if value > temp:
            temp = value
            temp_s = key
    
    return (map, temp_s)


memes = ["This is hilarious!", "A very long meme that goes on and on and on...", "Short and sweet", "Too long! Way too long!"]
memes_2 = ["Just right", "This one's too long though, sadly", "Perfect length", "A bit too wordy for a meme"]
memes_3 = ["Short", "Tiny meme", "Small but impactful", "Extremely lengthy meme that no one will read"]

print(filter_meme_lengths(memes, 20))
print(filter_meme_lengths(memes_2, 15))
print(filter_meme_lengths(memes_3, 10))

memes = [
    {"creator": "Alex", "text": "Meme 1"},
    {"creator": "Jordan", "text": "Meme 2"},
    {"creator": "Alex", "text": "Meme 3"},
    {"creator": "Chris", "text": "Meme 4"},
    {"creator": "Jordan", "text": "Meme 5"}
]

memes_2 = [
    {"creator": "Sam", "text": "Meme 1"},
    {"creator": "Sam", "text": "Meme 2"},
    {"creator": "Sam", "text": "Meme 3"},
    {"creator": "Taylor", "text": "Meme 4"}
]

memes_3 = [
    {"creator": "Blake", "text": "Meme 1"},
    {"creator": "Blake", "text": "Meme 2"}
]

print(count_meme_creators(memes))
print(count_meme_creators(memes_2))
print(count_meme_creators(memes_3))

memes = ["Dogecoin to the moon!", "One does not simply walk into Mordor", "Dogecoin to the moon!", "Distracted boyfriend", "One does not simply walk into Mordor"]
memes_2 = ["Surprised Pikachu", "Expanding brain", "This is fine", "Surprised Pikachu", "Surprised Pikachu"]
memes_3 = ["Y U No?", "First world problems", "Philosoraptor", "Bad Luck Brian"]

print(find_trending_memes(memes))
print(find_trending_memes(memes_2))
print(find_trending_memes(memes_3))

memes = ["Dogecoin to the moon!", "Distracted boyfriend", "One does not simply walk into Mordor"]
memes_2 = ["Surprised Pikachu", "Expanding brain", "This is fine"]
memes_3 = ["Y U No?", "First world problems", "Philosoraptor", "Bad Luck Brian"]

print(reverse_memes(memes))
print(reverse_memes(memes_2))
print(reverse_memes(memes_3))

task_times = [30, 45, 60, 90, 120]
available_time = 105
print(find_task_pair(task_times, available_time))

task_times_2 = [25, 15, 35, 45, 55]
available_time = 100
print(find_task_pair(task_times_2, available_time))

task_times_3 = [30, 20, 50, 70]
available_time = 60
print(find_task_pair(task_times_3, available_time))

work_sessions = [(900, 1100), (1300, 1500), (1600, 1800)]
print(find_smallest_gap(work_sessions))

work_sessions_2 = [(1000, 1130), (1200, 1300), (1400, 1500)]
print(find_smallest_gap(work_sessions_2))

work_sessions_3 = [(900, 1100), (1115, 1300), (1315, 1500)]
print(find_smallest_gap(work_sessions_3))

expenses = [("Food", 12.5), ("Transport", 15.0), ("Accommodation", 50.0),
            ("Food", 7.5), ("Transport", 10.0), ("Food", 10.0)]
print(calculate_expenses(expenses))

expenses_2 = [("Entertainment", 20.0), ("Food", 15.0), ("Transport", 10.0),
              ("Entertainment", 5.0), ("Food", 25.0), ("Accommodation", 40.0)]
print(calculate_expenses(expenses_2))

expenses_3 = [("Utilities", 100.0), ("Food", 50.0), ("Transport", 75.0),
              ("Utilities", 50.0), ("Food", 25.0)]
print(calculate_expenses(expenses_3))


text = "The quick brown fox jumps over the lazy dog. The dog was not amused."
print(word_frequency_analysis(text))

text_2 = "Digital nomads love to travel. Travel is their passion."
print(word_frequency_analysis(text_2))

text_3 = "Stay connected. Stay productive. Stay happy."
print(word_frequency_analysis(text_3))
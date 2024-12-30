from datetime import datetime


def filter_sustainable_brands(brands, criterion):
    
    res = []
    
    for i in range(len(brands)):
        if criterion in brands[i]["criteria"]:
            res.append(brands[i]["name"])
    
    return res

def count_unique_characters(script):
    unique = set()
    
    for c in script:
        unique.add(c)
        
    return len(unique)

def track_scene_transitions(scenes):
    stack = []
    
    for item in scenes:
        if not stack:
            stack.append(item)
        else:
            print("Transition from " + str(stack.pop()) + " to " + item)
            stack.append(item)

def organize_scene_data_by_date(scene_records):
    
    for i in scene_records:
        datetime.strptime(i[0], "%Y-%m-%d")
    
    scene_records.sort()

    return scene_records
    
scenes = ["Opening", "Rising Action", "Climax", "Falling Action", "Resolution"]
track_scene_transitions(scenes)

scenes = ["Introduction", "Conflict", "Climax", "Denouement"]
track_scene_transitions(scenes)

script = {
    "Alice": ["Hello there!", "How are you?"],
    "Bob": ["Hi Alice!", "I'm good, thanks!"],
    "Charlie": ["What's up?"]
}
print(count_unique_characters(script)) 

script_with_redundant_keys = {
    "Alice": ["Hello there!"],
    "Alice": ["How are you?"],
    "Bob": ["Hi Alice!"]
}
print(count_unique_characters(script_with_redundant_keys)) 
brands = [
    {"name": "EcoWear", "criteria": ["eco-friendly", "ethical labor"]},
    {"name": "FastFashion", "criteria": ["cheap materials", "fast production"]},
    {"name": "GreenThreads", "criteria": ["eco-friendly", "carbon-neutral"]},
    {"name": "TrendyStyle", "criteria": ["trendy designs"]}
]

brands_2 = [
    {"name": "Earthly", "criteria": ["ethical labor", "fair wages"]},
    {"name": "FastStyle", "criteria": ["mass production"]},
    {"name": "NatureWear", "criteria": ["eco-friendly"]},
    {"name": "GreenFit", "criteria": ["recycled materials", "eco-friendly"]}
]

brands_3 = [
    {"name": "OrganicThreads", "criteria": ["organic cotton", "fair trade"]},
    {"name": "GreenLife", "criteria": ["recycled materials", "carbon-neutral"]},
    {"name": "FastCloth", "criteria": ["cheap production"]}
]

print(filter_sustainable_brands(brands, "eco-friendly"))
print(filter_sustainable_brands(brands_2, "ethical labor"))
print(filter_sustainable_brands(brands_3, "carbon-neutral"))

scene_records = [
    ("2024-08-15", "Climax"),
    ("2024-08-10", "Introduction"),
    ("2024-08-20", "Resolution"),
    ("2024-08-12", "Rising Action")
]
print(organize_scene_data_by_date(scene_records))

scene_records = [
    ("2023-07-05", "Opening"),
    ("2023-07-07", "Conflict"),
    ("2023-07-01", "Setup"),
    ("2023-07-10", "Climax")
]
print(organize_scene_data_by_date(scene_records))
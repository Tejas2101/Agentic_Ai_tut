import json

# Open it with file as read only
with open ('tutorial.json','r') as file:
    info = json.load(file)

print(info)

# Write
person = {"name": "Tejas", "age": 25, "advisor": None, "skills": ["Python", "VHDL"]}

with open("person.json", "w", encoding="utf-8") as f:
    json.dump(person, f, indent=2)

# python -> text
text = '{"name": "Tejas", "skills": ["Python", "VHDL"], "active": true}'
data = json.loads(text)

print(type(data))          
print(data["name"])        
print(data["skills"][0])   
print(data["active"]) 
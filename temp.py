import json
with open("loader.json") as f:
    loader = json.load(f)

for i in loader["loader"]:
    print(i)

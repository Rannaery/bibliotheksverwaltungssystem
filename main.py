import json

print("Hello World")

with open('Nutzer.JSON') as f:
    d = json.load(f)
    print(d)
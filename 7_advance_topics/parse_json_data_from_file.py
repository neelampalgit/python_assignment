import json

def parse_json(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
        print(data)

parse_json("data.json")

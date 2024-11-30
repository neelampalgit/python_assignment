# Write a list of dictionaries to a CSV file
import csv

def write_to_csv(data, file_name):
    with open(file_name, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

data = [
    {"name": "John", "age": 30, "city": "New York"},
    {"name": "Jane", "age": 25, "city": "Los Angeles"},
]
write_to_csv(data, "people.csv")

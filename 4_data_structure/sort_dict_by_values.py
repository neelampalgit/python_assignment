def sort_dict_by_values(d):
    return {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}

d = {'apple': 5, 'banana': 2, 'cherry': 8}
print(sort_dict_by_values(d))

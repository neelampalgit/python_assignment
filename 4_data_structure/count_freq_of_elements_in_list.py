def count_frequency(lst):
    return {item: lst.count(item) for item in lst}

lst = [1, 2, 2, 3, 3, 3, 4]
print(count_frequency(lst))

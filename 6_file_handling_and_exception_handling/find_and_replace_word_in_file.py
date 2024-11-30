def find_and_replace(file_name, old_word, new_word):
    with open(file_name, 'r') as file:
        data = file.read()

    data = data.replace(old_word, new_word)

    with open(file_name, 'w') as file:
        file.write(data)

find_and_replace("sample.txt", "old_word", "new_word")

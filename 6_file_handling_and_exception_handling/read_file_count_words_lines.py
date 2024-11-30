# Read a file and count the number of words and lines
def count_words_and_lines(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        word_count = sum(len(line.split()) for line in lines)
        line_count = len(lines)
    return word_count, line_count

word_count, line_count = count_words_and_lines("sample.txt")
print(f"Word Count: {word_count}, Line Count: {line_count}")

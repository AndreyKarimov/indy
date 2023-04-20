from string import punctuation


def longest_word_in_file(file_name):
    with open(file_name, encoding='UTF-8') as file:
        return max([word.strip(punctuation) for word in file.read().split()][::-1], key=len)


print(longest_word_in_file('test.txt'))

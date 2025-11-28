def count_words(string):
    word_count = list(filter(None,string.replace('\n',' ').split(' ')))
    return len(word_count)
    # return len(string.split(' '))

def count_each_character(string):
    string = string.lower()
    output_dict = {}
    for character in set(list(string)):
        output_dict[character] = string.count(character)
    return output_dict
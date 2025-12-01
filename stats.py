def count_words(string):
    print("----------- Word Count ----------")
    word_count = list(filter(None,string.replace('\n',' ').split(' ')))
    return len(word_count)

def count_each_character(string):
    print("--------- Character Count -------")
    string = string.lower()
    output_dict = {}
    for character in set(list(string)):
        if character.isalpha():
            output_dict[character] = string.count(character)
    output_dict = dict(sorted(output_dict.items(),key=lambda item: item[1],reverse=True))
    return output_dict

def get_sorted_list_of_dict(dict):
    output_list_of_dict = []
    for k,v in dict.items():
        if k.isalpha():
            output_list_of_dict.append({'char':k,'num':v})
    output_list_of_dict.sort(reverse=True,key=lambda items: items["num"])
    return output_list_of_dict


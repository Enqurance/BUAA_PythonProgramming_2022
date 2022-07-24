if __name__ == "__main__":
    words_set = set(map(str, input().split()))
    words_list = list(words_set)
    article = list(map(str, input().split()))
    words_list.extend(article)
    words_list.sort()
    map_dic = {}
    cur_word = ""
    for item in words_list:
        if item in words_set:
            map_dic.update({item: item})
            cur_word = item
        else:
            map_dic.update({item: cur_word})
    for item in article:
        print(map_dic.get(item), end=" ")

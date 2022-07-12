import re

if __name__ == "__main__":
    article = str(input())
    str1 = re.compile("\\.\\.\\.")
    str2 = re.compile("~")
    article = str1.sub("~", article)
    article = article.replace("..", ".")
    article = str2.sub("...", article)
    cuts = []
    length = len(article)
    i = 0
    while True:
        if i >= length:
            break
        if str.isalpha(article[i]):
            word = ""
            while True:
                if i >= length or not str.isalpha(article[i]):
                    break
                word += article[i]
                i += 1
            cuts.append(word)
        else:
            other = ""
            while True:
                if i >= length or str.isalpha(article[i]):
                    break
                other += article[i]
                i += 1
            cuts.append(other)
    new_cuts = []
    for item in cuts:
        if item == "u":
            new_cuts.append("you")
        elif item == "english":
            new_cuts.append("English")
        else:
            new_cuts.append(item)
    final_cuts = []
    flag = True
    for item in new_cuts:
        if flag:
            final_cuts.append(item.title())
            flag = False
        else:
            final_cuts.append(item)
        if item.find(".") != -1 or item.find("?") != -1 or item.find("!") != -1:
            flag = True
    print("".join(final_cuts))

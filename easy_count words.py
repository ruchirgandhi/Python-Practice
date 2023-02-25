
from collections import Counter
path = "document1.txt"

def count_words(path):
    with open(path, "r") as f:
        words = f.readlines()
        print(words)
        f.close()

        wlist = []

        for word in words:
            words_list = word.split(" ")
            #print(words_list)
            for w in words_list:
                wlist.append(w)
                #print(wlist)

        print(wlist)

        x = Counter(wlist)
        y = x.most_common(3)



    for each in y:
        print("Word {} is present {} times".format(each[0],each[1]))

    return " "



print(count_words(path))







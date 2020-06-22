import wikipedia as wiki

def get_wiki_data(search_item):
    ########## getiing sentance from wikipedia################################
    result = wiki.page(wiki.search(search_item)[0])
    result_list = result.summary
    count = 0
    words = " "
    for i in range(len(result_list)):
        if count>=3:
            break      
        else:
             words = words+result_list[i]
        if result_list[i] == '.':
            count +=1

    if words != " ":
        return words
    else:
        return "failed"


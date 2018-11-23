from recipedb import Search
import mlab

mlab.connect()
def most_search():
    keyword_list = []
    search_documents = Search.objects()
    for item in search_documents:
        keyword_values = item.keyword
        for keyword in keyword_values:
            keyword = keyword.strip()
            keyword_list.append(keyword)

    word_counter = {}
    for word in keyword_list:
        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1

    popular_words = sorted(word_counter, key = word_counter.get, reverse = True)
    top_5 = popular_words[:5]
    return top_5


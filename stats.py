def get_num_words(book):
    words = book.split()
    count = 0
    for word in words:
        count += 1

    return count

def char_count(book):
    letters = {}
    book = book.lower()
    for letter in book:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1

    letters = dic_sort(letters)

    return letters

def dic_sort(dic):
    return dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
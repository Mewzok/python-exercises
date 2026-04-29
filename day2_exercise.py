def count_words(text):
    words = text.lower().split()
    counts = {}

    for word in words:
        counts[word] = counts.get(word, 0) + 1

    return counts

text = "The cat sat on the mat and the cat slept"

print(count_words(text))
from .words import count_words

def summarize(text):
    word_count = count_words(text)
    longest = max(text.split(), key=len)

    return f"{word_count} words; longest: {longest}"
    
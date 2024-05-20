def count_words(text):
    words = text.split()
    return len(words)
text = input("Enter the text: ")
word_count = count_words(text)
print("The number of words in the given text is:" word_count)
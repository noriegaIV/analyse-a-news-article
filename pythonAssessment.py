import re
from collections import Counter
def read_article(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        return file.read()
def get_words(text):
    return re.findall(r"[a-z0-9']+", text.lower())
def count_specific_word(text, search_word):
    return get_words(text).count(search_word.lower())
def identify_most_common_word(text):
    words = get_words(text)
    if not words:
        return None
    return Counter(words).most_common(1)[0][0]
def calculate_average_word_length(text):
    words = [re.sub(r"[^A-Za-z0-9]", "", word) for word in text.split()]
    words = [word for word in words if word]
    if not words:
        return 0
    return sum(len(word) for word in words) / len(words)
def count_paragraphs(text):
    if not text.strip():
        return 1
    paragraphs = re.split(r"\n\s*\n", text.strip())
    return len([p for p in paragraphs if p.strip()])
def count_sentences(text):
    if not text.strip():
        return 1
    sentences = re.split(r"[.!?]+", text)
    return len([s for s in sentences if s.strip()])
def main():
    file_name = input("Enter the article file name (e.g. article.txt): ")
    try:
        text = read_article(file_name)
    except FileNotFoundError:
        print("File not found. Check the file name and try again.")
        return

    search_word = input("Enter the word you want to count: ")

    print("Occurrences of '" + search_word + "':", count_specific_word(text, search_word))
    print("Most common word:", identify_most_common_word(text))
    print("Average word length:", round(calculate_average_word_length(text), 2))
    print("Number of paragraphs:", count_paragraphs(text))
    print("Number of sentences:", count_sentences(text))


if __name__ == "__main__":
    main()
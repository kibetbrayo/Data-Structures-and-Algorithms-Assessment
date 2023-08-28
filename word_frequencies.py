from collections import Counter


def word_frequencies(words):
    return dict(Counter(words.split(" ")))


if __name__ == '__main__':
    words = input("Enter a sentence: ")
    your_dictionary = word_frequencies(words)
    sorted_keys = sorted(your_dictionary.keys())
    for key in sorted_keys:
        print(key + ': ' + str(your_dictionary[key]))
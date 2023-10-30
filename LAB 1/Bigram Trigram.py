import nltk, os
from nltk.util import ngrams

PATH = r'C:\Users\bholu\OneDrive\Documents\Python\IR\LAB 1\mails'

bigrams = list()
trigrams = list()

for file in os.listdir(PATH):
    if file.endswith('.txt'):
        file_path = os.path.join(PATH, file)
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
            
            words = nltk.word_tokenize(text)
            bigrams.extend(list(ngrams(words,2)))
            trigrams.extend(list(ngrams(words,3)))

# Generate text using bigram language model
search_word = 'Kartavya'
generated_bigram_text = [search_word]

for _ in range(50):
    next_word_candidates = [bigram[1] for bigram in bigrams if bigram[0] == search_word]
    if next_word_candidates:
        next_word = nltk.FreqDist(next_word_candidates).max()
        generated_bigram_text.append(next_word)
        search_word = next_word
    else:
        break

# Generate text using trigram language model
words = ["Time", "to"]
generated_trigram_text = words

for _ in range(50):
    trigram_candidates = [trigram[2] for trigram in trigrams if trigram[0] == words[-2]]
    if trigram_candidates:
        next_word = nltk.FreqDist(trigram_candidates).max()
        generated_trigram_text.append(next_word)
        words.append(next_word)
    else:
        break

# Print separate outputs for bigrams & trigrams
print("Generated Bigram Text:")
print(' '.join(generated_bigram_text))

print('\nGenerated Trigram Text:')
print(' '.join(generated_trigram_text))
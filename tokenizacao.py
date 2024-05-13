import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

nltk.download('punkt')

texto = "O processamento de linguagem natural (NLP) é uma área da inteligencia artificial"

tokens = word_tokenize(texto)
print(tokens)

stop_words = set(stopwords.words('portuguese'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
print(filtered_tokens)

freq_dist = FreqDist(filtered_tokens)
print(freq_dist.most_common(5))







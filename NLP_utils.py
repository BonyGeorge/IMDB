import string, re, nltk

class NLP_utils:

    def __init__(self):
        self.stopwords = set(nltk.corpus.stopwords.words('english'))
        self.ps = nltk.PorterStemmer()
        self.wn = nltk.WordNetLemmatizer()

    def remove_punc(self, text):
        return "".join([char for char in text if char not in string.punctuation])

    def tokenize(self, text):
        return re.split(r'\W+', text)

    def remove_stopwords(self, tokenized_list):
        return [word for word in tokenized_list if word not in self.stopwords]

    def stemming(self, tokenized_list):
        return [self.ps.stem(word) for word in tokenized_list]

    def lemmatizing(self, tokenized_list):
        return [self.wn.lemmatize(word) for word in tokenized_list]
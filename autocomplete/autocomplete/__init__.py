import pickle

word_dict ={}
with open('word_dict.pickle', 'rb') as handle:
    word_dict = pickle.load(handle)

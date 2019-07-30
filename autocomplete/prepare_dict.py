import sys
import pickle

in_file = open(sys.argv[1])
pickle_out = open(sys.argv[2], 'wb')

word_dict = {}
for line in in_file:
    line = line.split()
    word_dict[line[0]] = line[1]
pickle.dump(word_dict, pickle_out)
pickle_out.close()

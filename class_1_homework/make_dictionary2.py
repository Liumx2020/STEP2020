import numpy as np

def lettercount(words):
    count = np.zeros(26,dtype=int)
    for letter in words:
        if ord(letter) < 91:
            # capital letter
            count[ord(letter) - ord('A')] += 1
        else:
            # small letter
            count[ord(letter) - ord('a')] += 1
    return count

# change dictionary to lettter-count vector
lines =  open('dictionarywords.txt')
dictionary = lines.readlines()
lettercount_list = np.zeros((len(dictionary),26),dtype=int)
i = 0
for w in dictionary: 
    w = w.strip('\n')
    lettercount_list[i,:] = lettercount(w)
    i += 1
lines.close()

np.savetxt("dictionary2.txt",lettercount_list,fmt="%i")



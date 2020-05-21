def lettercount(words):
    count = [0] * 26
    for letter in words:
        if ord(letter) < 91:
            # capital letter
            count[ord(letter) - ord('A')] += 1
        else:
            # small letter
            count[ord(letter) - ord('a')] += 1
    return count


# 辞書を読み込んで、'\n'を取り除く
lines =  open('dictionarywords.txt')
dictionary = lines.readlines()
dictionary1 = []
for i in dictionary: 
    i=i.strip('\n')
    dictionary1.append(i)
lines.close()

lines =  open('dictionary2.txt')
dictionary = lines.readlines()
dictionary2 = []
for i in dictionary: 
    i=i.strip('\n')
    dictionary2.append(i)
lines.close()

def anagram(inputword):
    outputword=[]
    for i in range(len(dictionary2)):
        if dictionary2[i] == str(lettercount(inputword)):
            outputword.append(dictionary1[i])
    if  len(outputword) > 0:
        return outputword
    else:
        return -1
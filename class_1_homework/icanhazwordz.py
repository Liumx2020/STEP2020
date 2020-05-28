from anagram import dictionary1,dictionary2,lettercount
import numpy as np


d = np.loadtxt("dictionary2")


def anagram2(inputword):
    outputword=[]
    for i in range(len(dictionary2)):
        if dictionary2[i] == str(inputword):
            outputword.append(dictionary1[i])
    if  len(outputword) > 0:
        return outputword
    else:
        return -1


letter_option = "cat"

def icanhazwordz(letter_option):
    point3 = ["J","K","Q","X","Z"] #"Qu"="Q" in this dictionary
    point2 = ["C","F","H","L","M","P","V","W","Y"]
    point1 = ["A","B","D","E","G","I","N","O","R","S","T","U"]

    point_option = lettercount(letter_option)

    LCpoint3 = []
    for letter in point3:
        LCpoint3.append(lettercount(letter))

    LCpoint2 = []
    for letter in point2:
        LCpoint2.append(lettercount(letter))

    LCpoint1 = []
    for letter in point1:
        print(letter)
        LCpoint1.append(lettercount(letter))


    # ruduce one letter from 1 point letter
    for letter in letter_option:
        if lettercount(letter) in LCpoint1:
            if ord(letter) < 91:
                point_option[ord(letter) - ord('A')] -= 1
            else:
                point_option[ord(letter) - ord('a')] -= 1
        
        if anagram2(point_option) == -1:
            return anagram2(point_option)

    # ruduce one letter from 2 point letter
    for letter in letter_option:
        if lettercount(letter) in LCpoint1:
            if ord(letter) < 91:
                point_option[ord(letter) - ord('A')] -= 1
            else:
                point_option[ord(letter) - ord('a')] -= 1
        
        if anagram2(point_option) == -1:
            return anagram2(point_option)



    

# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 14:38:58 2018

@author: Dyass
"""

"""
    Topics:
        Examples with a Dictionary:
         1:Create a frequency distribution mapping str:int
         2:Find a word that occurs the most and how many times:
             use a list,in case there is mote than one word
             returns a tuple(list,int) for (words_list,highest_freq)
        3:Find the word that occur at least X times:
            let user choose "at least X times,"so allow as parameters
            returns a list of tuples,each tuple is a (list,int)
            containing the list of words ordered by their frequency
            IDEA:
                From song dictionary,find most frequent word.Delete the most common
                word.Repeat,it works because you are mutating the song
                dictionary
"""
def lyrics_to_frequencies(lyrics):
    myDict={}
    for word in lyrics:
        if word in myDict:
            myDict[word]+=1
        else:
            myDict[word]=1
    return myDict
def most_common_words(freqs):
    values=freqs.values()
    best =max(values)
    words=[]
    for i in freqs:
        if freqs[i]==best:
            words.append(i)
    return(words,best)
def words_often(freqs,minTimes):
    result=[]
    done=False
    while not done:
        temp=most_common_words(freqs)
        if temp[1]>=minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])
        else:
            done=True
    return result
    
she_loves_you = ['she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',

'you', 'think', "you've", 'lost', 'your', 'love',
'well', 'i', 'saw', 'her', 'yesterday-yi-yay',
"it's", 'you', "she's", 'thinking', 'of',
'and', 'she', 'told', 'me', 'what', 'to', 'say-yi-yay',

'she', 'says', 'she', 'loves', 'you',
'and', 'you', 'know', 'that', "can't", 'be', 'bad',
'yes', 'she', 'loves', 'you',
'and', 'you', 'know', 'you', 'should', 'be', 'glad',

'she', 'said', 'you', 'hurt', 'her', 'so',
'she', 'almost', 'lost', 'her', 'mind',
'and', 'now', 'she', 'says', 'she', 'knows',
"you're", 'not', 'the', 'hurting', 'kind',

'she', 'says', 'she', 'loves', 'you',
'and', 'you', 'know', 'that', "can't", 'be', 'bad',
'yes', 'she', 'loves', 'you',
'and', 'you', 'know', 'you', 'should', 'be', 'glad',

'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',

'you', 'know', "it's", 'up', 'to', 'you',
'i', 'think', "it's", 'only', 'fair',
'pride', 'can', 'hurt', 'you', 'too',
'pologize', 'to', 'her',

'Because', 'she', 'loves', 'you',
'and', 'you', 'know', 'that', "can't", 'be', 'bad',
'Yes', 'she', 'loves', 'you',
'and', 'you', 'know', 'you', 'should', 'be', 'glad',

'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',
'yeah', 'yeah', 'yeah',
'yeah', 'yeah', 'yeah', 'yeah'
]
song=lyrics_to_frequencies(she_loves_you)
print(words_often(song,5))




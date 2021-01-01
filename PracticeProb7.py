'''
Author: Mounika Seeram
Date: 01/01/2021
Purpose: Practice Problem7 from CodeWithHarry, Search Engine 
'''
import re

def matchingWords(string1,string2):
    score = 0 
    words1 = string1.split(" ")
    words2 = string2.split(" ")
    for word1 in words1:
        for word2 in words2:
            if word1.lower() == word2.lower():
                score +=1
    return score



sentences = ['This is good','Python is good','Python python is not that good','python super python python good']
query_str = input("Please enter your query String\n")
#print(matchingWords(query_str,sentences[1]))
# for i in range(0,len(sentences)):
#     if query_str.lower() in sentences[i].lower():
#         search_results.append(sentences[i])
scores = [matchingWords(query_str,sentence) for sentence in sentences]
search_results = [result for result in sorted(zip(scores,sentences),reverse=True)]
print('PFB Search results ')
for score,item in search_results:
    if score > 0:
        print(f'"{item}"" with score of {score}')
#print(search_results)

# * Import a text file filled with a paragraph of your choosing.
import csv
import os
import re
txtPath = "input.txt"
# sentence count
with open(txtPath, 'r') as paragraph:
    oneLineParagraph = ' '.join(paragraph.read().split())
    # print (oneLineParagraph)
    sentences = re.split("(?<=[.!?]) +", oneLineParagraph)
    numberOfSentences = len(sentences)
    print (numberOfSentences)

#  * Approximate word count and number of letters
with open(txtPath, newline='',encoding='utf-8') as txtfile:
    wordReader = csv.reader(txtfile, delimiter=' ')
    for words in wordReader:
    # print (words)
        numberOfWords = len(words)
        print (numberOfWords)
        numberOfLetters = 0
        for letters in words:
            numberOfLetters = numberOfLetters + len(letters)
        print (numberOfLetters)

print ("Paragraph Analysis for " + str(txtPath) + "\n" + 
"--------------------------------\n" +
"Approximate Word Count: " + str(numberOfWords) + "\n" +
"Approximate Sentence Count: " + str(numberOfSentences) + "\n" +
"Average Letter Count per Word: " + str(round(numberOfLetters/numberOfWords,2)) + "\n" +
"Average Words per Sentence: " + str(round(numberOfWords/numberOfSentences,2)))

with open('output.txt', 'w') as f:
    f.write ("Paragraph Analysis for " + str(txtPath) + "\n" + 
    "--------------------------------\n" +
    "Approximate Word Count: " + str(numberOfWords) + "\n" +
    "Approximate Sentence Count: " + str(numberOfSentences) + "\n" +
    "Average Letter Count per Word: " + str(round(numberOfLetters/numberOfWords,2)) + "\n" +
    "Average Words per Sentence: " + str(round(numberOfWords/numberOfSentences,2)))

#   * Average sentence length (in words)
# * As an example, this passage:

# > “Adam Wayne, the conqueror, with his face flung back and his mane like a lion's, stood with his great sword point upwards, the red 
#   raiment of his office flapping around him like the red wings of an archangel. And the King saw, he knew not how, something new and overwhelming. The great green trees and the great red robes swung together in the wind. The preposterous masquerade, born of his own mockery, towered over him and embraced the world. This was the normal, this was sanity, this was nature, and he himself, with his rationality, and his detachment and his black frock-coat, he was the exception and the accident - a blot of black upon a world of crimson and gold.”

# ...would yield these results:

# ```
# Paragraph Analysis
# -----------------
# Approximate Word Count: 122
# Approximate Sentence Count: 5
# Average Letter Count: 4.56557377049
# Average Sentence Length: 24.4
# ```


 
# A span comment is defined as a text containing following keywords:
"""
Make a lot of money, buy now, subscribe this, click this
"""

spam_words = ["Make a lot of money", "buy now", "subscribe this", "click this"]

word = input("Enter the spam word: ")

flag = True

for i in spam_words:
    if(i == word):
        flag = False

if(flag):
    print("its not spam")
else:
    print("its spam")
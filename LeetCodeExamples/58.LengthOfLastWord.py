s="Hello World    "
words=s.split(" ")
words_without_spaces=[]
last_word=[]
last_word_separated=[]
for i in words:
    if len(i)>=1:
        words_without_spaces.append(i)
print(len(words_without_spaces[-1]))

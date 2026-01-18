sentence = 'I completely agree with you'
result = f"No. of letters in words: {list(map(lambda word: len(word) , sentence.split()))}"
print(sentence,"\n",result)
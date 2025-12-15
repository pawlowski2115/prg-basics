translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}
word = input("Enter the word to translation: ")

if word in translations:
    word_translated = translations[word]
    print(word,":",word_translated)
else:
    print("The translation is unavailable")
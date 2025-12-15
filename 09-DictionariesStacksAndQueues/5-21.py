import json

book={
        "title": "Pan Tadeo",
        "IBAN": "123456789",
        "author": "Olek",
        "date": "1985-05-15",
        "pages": 129,
}

with open('favourite.json','w',encoding='utf-8') as file:
    json.dump(book, file, indent=4)
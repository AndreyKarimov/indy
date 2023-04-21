import json


def decode(text: str) -> None:
    new_text = ''
    with open('Alphabet.json', encoding='UTF-8') as decode_file:
        decode = json.load(decode_file)
        for letter in text.read():
            new_text += decode[letter] if letter.isalpha() else letter
    print(new_text)

with open('Abracadabra__1_.txt', encoding='UTF-8') as file:
    decode(file)

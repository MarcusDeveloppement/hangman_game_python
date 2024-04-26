import random

words= ["balance","espace","squelette","substitution","poing","cauchemar","minuscule","baignade","anniversaire","chagrin"]
secret = random.randint(0,len(words) -1)
secret_word = words[secret]
game = {
    "secret_word": secret_word ,
    "gess_word": "_" * len(secret_word),
    "life_point":10,
}

print(f"{game['gess_word']} | vie: {game['life_point']}")

while True: 
    letter =input('enter letter: ')
    print(letter)
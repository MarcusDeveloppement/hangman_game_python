import random

words= ["balance","espace","squelette","substitution","poing","cauchemar","minuscule","baignade","anniversaire","chagrin"]
secret = random.randint(0,len(words) -1)
secret_word = words[secret]
game = {
    "secret_word": secret_word ,
    "guess_word": "_" * len(secret_word),
    "life_point":10,
}

print(f"{game['guess_word']} | vie: {game['life_point']}")

while True: 
    letter =input('enter letter: ')
    if letter in game["secret_word"] and letter not in game["guess_word"]:
        guess_word_list = list(game["guess_word"])
        for index, current_letter in enumerate(game["secret_word"]):
            if current_letter == letter:
                guess_word_list[index] =letter
        game["guess_word"] = "".join(guess_word_list)
    elif letter not in game["secret_word"]:
        game["life_point"]-=1
    print(f"{game['guess_word']} | vie: {game['life_point']}")
    if '_' not in game["guess_word"]:
        print("gagné !") 
        break
    elif game["life_point"] <= 0:
        print("Perdu !")
        break
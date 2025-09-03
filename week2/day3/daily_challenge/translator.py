# from googletrans import Translator

# translator = Translator

# french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]

# # translate принимает список и вернёт список объектов Translation
# translated = translator.translate(french_words, src='fr', dest='en')

# for trans in translated:
#     print(f'{trans.origin} -> {trans.text}')

from deep_translator import GoogleTranslator

translator = GoogleTranslator(source='fr', target='en')
french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]

for w in french_words:
    print(f"{w} -> {translator.translate(w)}")
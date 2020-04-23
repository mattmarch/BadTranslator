import sys, random
from googletrans import Translator
from languages import LANGUAGES

START_END_CODE = 'en'


def translate_n_times(input_phrase, number_times):
    translator = Translator()

    translation_languages = random.sample(LANGUAGES.keys(), number_times - 1)
    translation_languages.append(START_END_CODE)

    output = input_phrase
    phrase_in_current_language = input_phrase
    current_language = START_END_CODE
    for next_language in translation_languages:
        phrase_in_current_language = translator.translate(phrase_in_current_language, src=current_language, dest=next_language).text
        output += f'\n\n[{LANGUAGES[current_language]} -> {LANGUAGES[next_language]}]\n\n{phrase_in_current_language}'
        current_language = next_language
    return output        

if __name__ == '__main__':
    filename = sys.argv[1]
    number_translations = int(sys.argv[2])
    with open(filename) as f:
        phrase = ''.join(f.readlines())
        print(translate_n_times(phrase, number_translations))
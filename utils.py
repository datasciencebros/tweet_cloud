# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import codecs
import re

def remove_mentions(text):
    words = []
    for w in text.split():
        if not w.startswith('@'):
            words.append(w)

    words = ' '.join(words)
    return words

def remove_links(text):
    words = []
    for w in text.split():
        if not w.startswith('http'):
            words.append(w)

    words = ' '.join(words)
    return words

def remove_stop_words(text, stop_words):
    words = []
    for w in text.split():
        if w not in stop_words:
            words.append(w)

    words = ' '.join(words)
    return words

def normalize_letters(text):
    # lowercase
    text = text.replace('á', 'a')
    text = text.replace('é', 'e')
    text = text.replace('í', 'i')
    text = text.replace('ó', 'o')
    text = text.replace('ú', 'u')
    text = text.replace('ü', 'u')
    text = text.replace('ô', 'o')
    text = text.replace('õ', 'o')
    text = text.replace('ã', 'a')
    text = text.replace('â', 'a')
    text = text.replace('à', 'a')

    text = text.replace('ê', 'e')
    text = text.replace('ç', 'c')

    # uppercase
    text = text.replace('Á', 'A')
    text = text.replace('É', 'E')
    text = text.replace('Í', 'I')
    text = text.replace('Ó', 'O')
    text = text.replace('Ú', 'U')
    text = text.replace('Ü', 'u')
    text = text.replace('Ô', 'O')
    text = text.replace('Õ', 'O')
    text = text.replace('Ã', 'A')
    text = text.replace('Â', 'A')

    return text

def get_stop_words(filename):
    stop_words = set()

    # Codecs is necessary to open the file using utf-8 as encoding.
    stop_words_file = codecs.open(filename, mode='r', encoding='utf-8')
    for stop_word in stop_words_file:
        # By default open add EOL (\n) at the end of each line.
        stop_words.add(stop_word.rstrip('\n'))

    return stop_words

def remove_non_letters(text):
    tokens = text.split()
    regex = re.compile(r'[^a-zA-ZáéíóúÁÉÍÓÚüÜÔôÕõÇçÃãÂâàñÑ@]')

    new_text = []

    for token in tokens:
        if token.strip():
            new_token = regex.sub('', token)
            if new_token.strip():
                new_text.append(new_token)

    return ' '.join(new_text)

def normalize_space(text):
    return re.sub(r' +', ' ', text)


def clean_text(text):
    text = text.lower()
    text = remove_mentions(text)
    text = remove_links(text)
    text = remove_non_letters(text)
    text = remove_stop_words(text, get_stop_words('stopwords/spanish.txt'))
    text = remove_stop_words(text, get_stop_words('stopwords/custom_stopwords.txt'))
    text = normalize_space(text)
    text = normalize_letters(text)
    return text

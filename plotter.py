# -*- coding: utf-8 -*-

import click
import codecs
from os import path
from PIL import Image
import numpy as np

from wordcloud import WordCloud


class Plotter:
    @staticmethod
    def plot(username):
        d = path.dirname(__file__)
        twitter_mask = np.array(Image.open(path.join(d, 'masks/twitter.png')))

        text = codecs.open('output/' + username + '.csv', encoding='utf-8').read()
        words = text.split()

        frequency = {}

        for word in words:
            count = frequency.get(word, 0)
            frequency[word] = count + 1

        wordcloud = WordCloud(
            font_path='fonts/RobotoCondensed-Regular.ttf',
            background_color='white',
            width=1800,
            height=1400,
            margin=10,
            mask=twitter_mask,
        ).generate_from_frequencies(frequency.items())

        wordcloud.to_file('output/wordcloud-' + username + '.png')

@click.command()
@click.argument('username', nargs=1)
def make_wordcloud(username):
    Plotter.plot(username)


if __name__ == '__main__':
   make_wordcloud()

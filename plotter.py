# -*- coding: utf-8 -*-

import click
import codecs
import re

from wordcloud import WordCloud


class Plotter:
    @staticmethod
    def plot(username):
        text = codecs.open('output/' + username + '.csv', encoding='utf-8').read()
        match_pattern = re.findall(r'\b\w{3,15}\b', text, re.UNICODE)

        frequency = {}

        for word in match_pattern:
            count = frequency.get(word, 0)
            frequency[word] = count + 1

        wordcloud = WordCloud(
            font_path='fonts/RobotoCondensed-Regular.ttf',
            background_color='white',
            width=1800,
            height=1400,
            margin=10,
        ).generate_from_frequencies(frequency.items())

        wordcloud.to_file('output/wordcloud-' + username + '.png')

@click.command()
@click.argument('username', nargs=1)
def make_wordcloud(username):
    Plotter.plot(username)


if __name__ == '__main__':
   make_wordcloud()

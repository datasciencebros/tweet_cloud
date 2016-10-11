# -*- coding: utf-8 -*-

import click
import codecs

from wordcloud import WordCloud


class Plotter:
    @staticmethod
    def plot(username):
        text = codecs.open('output/' + username + '.csv', encoding='utf-8').read()

        wordcloud = WordCloud(
            font_path='fonts/RobotoCondensed-Regular.ttf',
            background_color='white',
            width=1800,
            height=1400,
        ).generate(text)

        wordcloud.to_file('output/wordcloud-' + username + '.png')

@click.command()
@click.option('--username', help='The twitter username.')
def make_wordcloud(username):
    Plotter.plot(username)


if __name__ == '__main__':
   make_wordcloud()

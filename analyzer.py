# -*- coding: utf-8 -*-

import click
from backports import csv
import io

from utils import clean_text


TWEET_INDEX = 3

class Analyzer:
    @staticmethod
    def analyze(username):
        with io.open('data/' + username + '.csv', 'rt') as filename:
            reader = csv.reader(filename)

            with io.open('output/' + username + '.csv', 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                reader.next()
                for row in reader:
                    tweet = row[TWEET_INDEX]
                    # Exclude tweets.
                    if not tweet.startswith('RT'):
                        writer.writerow([clean_text(tweet)])


@click.command()
@click.option('--username', help='The twitter username.')
def analyzer(username):
    Analyzer.analyze(username)


if __name__ == '__main__':
    analyzer()

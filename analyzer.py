# -*- coding: utf-8 -*-

import click
from backports import csv
import io

from utils import clean_text


TWEET_INDEX = 3

class Analyzer:
    @staticmethod
    def analyze(username, exclude_rt):
        with io.open('data/' + username + '.csv', 'rt') as filename:
            reader = csv.reader(filename)

            with io.open('output/' + username + '.csv', 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                reader.next()
                for row in reader:
                    tweet = row[TWEET_INDEX]
                    # Exclude tweets.
                    if exclude_rt:
                        if not tweet.startswith('RT'):
                            writer.writerow([clean_text(tweet)])
                    else:
                        writer.writerow([clean_text(tweet)])


@click.command()
@click.option('--exclude-rt', default=True)
@click.argument('username', nargs=1)
def analyzer(username, exclude_rt):
    Analyzer.analyze(username, exclude_rt)


if __name__ == '__main__':
    analyzer()

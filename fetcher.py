# -*- coding: utf-8 -*-
from __future__ import print_function

import subprocess

import click


NUMBER_OF_TWEETS = 3200


class TwitterFetcher:

    @staticmethod
    def fetch(username):
        with open('data/' + username + '.csv', 'w') as filename:
            process = subprocess.Popen(
                    ['t', 'timeline', username, '-n', str(NUMBER_OF_TWEETS), '--csv'],
                    stdout=filename, stderr=subprocess.PIPE)
            _, stderr = process.communicate()
            if stderr:
                TwitterFetcher._handle_error(stderr, username)

    @staticmethod
    def _handle_error(stderr, username):
        if 'Sorry, that page does not exist' in stderr:
            print('The {} username does not exists.').format(username)
        elif 'Failed to open TCP connection to' in stderr:
            print('There was a internet problem. Please check if you are online.')
        else:
            print(stderr)

@click.command()
@click.argument('username', nargs=1)
def retrieve_tweets(username):
    TwitterFetcher.fetch(username)


if __name__ == '__main__':
    retrieve_tweets()

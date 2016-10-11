# -*- coding: utf-8 -*-

import unittest

from utils import (
    remove_mentions,
    remove_links
)

class UtilsTestCase(unittest.TestCase):

    def test_remove_mentions(self):
        tweet = 'This is a mention to @me'
        expected = 'This is a mention to'

        self.assertEqual(expected, remove_mentions(tweet))

    def test_remove_links(self):
        tweet = 'SCALABLE SCRAPING USING MACHINE LEARNING https://t.co/WZFCMy7tNz'
        expected = 'SCALABLE SCRAPING USING MACHINE LEARNING'

        self.assertEqual(expected, remove_links(tweet))

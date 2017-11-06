from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt
from redis import StrictRedis

class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()

    def process(self, tup):
        word = tup.values[0]

        # Increment the word count in redis 
        self.redis.zincrby("wordcount", word)

        # increase the word count locally
        self.counts[word] += 1
        self.emit([word, self.counts[word]])

        # log the count for displaying
        self.log('%s: %d' % (word, self.counts[word]))

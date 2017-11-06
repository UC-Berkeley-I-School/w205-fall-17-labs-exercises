"""
Using Twitter stream API, print all the tweets in the stream containing the term "Hello" in a 1 min period

"""
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from Twittercredentials import *
from time import time,ctime
import simplejson

class StdOutListener(StreamListener):
   
    def __init__(self,timer):
        self.inc = 0
        StreamListener.__init__(self)
        # report the start of data collection...
        print "Gathering data at %s"%(str(ctime()))
        self.startTime = time()
        print "Start Time = %s"%(str(ctime()))
        self.timer = timer
        self.count = 0
        

    def on_data(self, data):
        try:
            self.endTime = time()
            self.elapsedTime = self.endTime - self.startTime
            if self.elapsedTime <= self.timer:
                self.dataJson =simplejson.loads(data[:-1])
                self.dataJsonText = self.dataJson["text"].lower()
                self.count += 1
                if "Hello" in self.dataJsonText:
                    print self.dataJsonText

            else:
                print "Count== ",self.count
                print "End Time = %s"%(str(ctime()))
                print "Elapsed Time = %s"%(str(self.elapsedTime))



                return False
            return True
        except Exception, e:
            # Catch any unicode errors while printing to console
            # and just ignore them to avoid breaking application.
            pass

    def on_error(self, status):
        print ("ERROR :",status)

if __name__ == '__main__':
    # to collect the data for 1 min
    l = StdOutListener(60)
    mystream = tweepy.Stream(auth, l, timeout=60)
    mystream.sample()




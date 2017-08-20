"""
Start a daemon to send tweets to Kinesis

Example: start the daemon
--------
python stream_to_stream/sender_daemon.py start &>/dev/null &

Example: stop the daemon
--------
python stream_to_stream/sender_daemon.py stop &>/dev/null &
"""

import datetime as dt
import os

from utils.logger import configure_logger
from utils.daemon import UnixDaemon
from send_tweets_to_kinesis import TweetsCollector


class Sender(UnixDaemon):
    def __init__(self):
        super().__init__()
        self.daemon_description = 'Daemon to start morning tasks scheduler'
        self.logger = configure_logger()

    def add_parse_arguments(self, parser):
        super().add_parse_arguments(parser)

    def run(self):
        self.logger.info('Started at {}'.format(dt.datetime.now()))
        keywords = os.environ['TWITTER_KEYWORDS'].split(',')
        self.logger.info(keywords)
        TweetsCollector.run(keywords=keywords)

if __name__ == '__main__':
    Sender().action()

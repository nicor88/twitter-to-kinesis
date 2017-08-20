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

# just to test
# os.environ["AWS_DEFAULT_REGION"] = "eu-west-1"
# os.environ["AWS_PROFILE"] = "nicor88-aws-dev"
# os.environ['STREAM_NAME'] = 'DevStreamES'
# os.environ['PRODUCER_NAME'] = 'TestProducerWithDaemon'
# os.environ['TWITTER_KEYWORDS'] = 'python'


class Sender(UnixDaemon):
    def __init__(self):
        super().__init__()
        self.daemon_description = 'Daemon to start morning tasks scheduler'
        self.logger = configure_logger()

    def add_parse_arguments(self, parser):
        super().add_parse_arguments(parser)

    def run(self):
        self.logger.info('Started at {}'.format(dt.datetime.now()))
        stream_name = os.environ['STREAM_NAME']
        producer_name = os.environ['PRODUCER_NAME']
        keywords = os.environ['TWITTER_KEYWORDS'].split(',')
        self.logger.info(keywords)
        TweetsCollector.run(stream_name=stream_name, producer=producer_name, keywords=keywords)

if __name__ == '__main__':
    Sender().action()

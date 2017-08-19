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

if os.environ['ENV'] == 'dev':
    os.environ["AWS_DEFAULT_REGION"] = "eu-west-1"
    os.environ["AWS_PROFILE"] = "nicor88-aws-dev"


class Sender(UnixDaemon):
    def __init__(self):
        super().__init__()
        self.daemon_description = 'Daemon to start morning tasks scheduler'
        self.app_name = 'daily_tasks_scheduler'
        self.logger = configure_logger()

    def add_parse_arguments(self, parser):
        super().add_parse_arguments(parser)

    def run(self):
        self.logger.info(f'Started at {dt.datetime.now().isoformat()}')
        keywords = os.environ['TWITTER_KEYWORDS'].split(',')
        self.logger.info(keywords)
        TweetsCollector.run(keywords=keywords)

if __name__ == '__main__':
    Sender().action()

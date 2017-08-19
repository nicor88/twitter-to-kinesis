#!/bin/bash

export AWS_DEFAULT_REGION="eu-west-1"
export PYTHONPATH=/opt/twitter-to-kinesis

# create or update conda env
conda env update -n twitter-to-kinesis -f /opt/twitter-to-kinesis/conda-dev-env.yml
source activate twitter-to-kinesis


cp /root/configs.yml /opt/twitter-to-kinesis/settings
cd /opt/twitter-to-kinesis/

pwd >> more_log.log

# start producer
python /opt/twitter-to-kinesis/sender_daemon.py --pid_file /tmp/twitter_sender.pid start &>/opt/twitter-to-kinesis/all_start.log &

#!/bin/bash

source /root/.bashrc

export AWS_DEFAULT_REGION="eu-west-1"
export PYTHONPATH=/opt/twitter-to-kinesis

# create or update conda env
conda env update -n twitter-to-kinesis -f /opt/twitter-to-kinesis/conda-dev-env.yml
source activate twitter-to-kinesis

# copy secrets from S3, to remove in the future
/usr/bin/aws s3 cp s3://nicor-dev/secrets/configs.yml /opt/twitter-to-kinesis/settings >> more.log

cd /opt/twitter-to-kinesis/

# start producer
python /opt/twitter-to-kinesis/sender_daemon.py --pid_file /tmp/twitter_sender.pid start &>/dev/null &

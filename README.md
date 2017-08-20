[![Build Status](https://travis-ci.org/nicor88/twitter-to-kinesis.svg?branch=master)](https://travis-ci.org/nicor88/twitter-to-kinesis)

# twitter-to-kinesis
Producer to send tweets to a Kinesis Stream

## Dependencies

* Conda

## Setup Conda
<pre>conda env create -f conda-dev-env.yml
source activate twitter-to-kinesis
</pre>

After installing a new package update the env file:
<pre>conda env export > conda-dev-env.yml
</pre>


## Deployment
The application is zipped and push to S3 using Travis

### AWS CodeDeploy

It's possible to the deploy the application to an EC2 instance using CodeDeploy.

Change these files to change the setup:
*  appsepc.yml
*  scripts
    * start_producer.sh
    * stop_producer.sh
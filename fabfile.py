from fabric.decorators import task
from fabric.api import local, cd, run, puts, settings, lcd, env


@task
def backup():
    """backup the backfeed dynamodb databases"""

    # assume your AWS access key and secret key is present in ~/.boto
    REGION = 'us-east-1'
    SRCTABLE = '*'  # all tables
    LOG = 'DEBUG'  # DEBUG|INFO|WARNING|ERROR|CRITICAL
    local('./dynamodump/dynamodump.py -m backup -r {REGION} -s "{SRCTABLE}" --log {LOG}'.format(**locals()))

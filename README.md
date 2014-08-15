api-replay
==========

An HTTP replay, proxy, routing service with queuing in Python, Flask, and Redis

###Installing

`pip install git+https://github.com/easypairings/api-replay.git`

###Configuring

The following environment variables are required:

```
DEBUG # default: True
REDIS_URL # e.g. redis://localhost
RQ_DEFAULT_URL # most likely same as REDIS_URL
SECRET_KEY
API_REPLAY_BASE # the base for the exponential backoff for retries (in seconds), default: 2
API_REPLAY_RETRIES # the number of retries that should be attempted if the endppoint fails, default: 10
```

###Running

Running the application (for development) requires the following processes:

```
redis-server
api-replay runserver
rqworker
rqscheduler
```

A note about rqscheduler: the default interval for scheduling tasks is 60 seconds. This means that retries will be scheduled on the minute. To override the default behavior, use `rqscheduler -i X`, where `X` is the scheduling interval in seconds.

###Contributing

Pull requests are very welcome. In your first pull request, please add your name to [AUTHORS.md](https://github.com/easypairings/api-replay/blob/master/AUTHORS.md).
